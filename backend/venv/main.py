# --- Modülleri içe aktar ---
import os
import json
import requests
import ast  # Güvenli string -> liste çevirme
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# --- Ortam değişkenlerini yükle (.env dosyasından) ---
load_dotenv()

# --- Gemini API anahtarını oku ---
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_KEY:
    raise RuntimeError("GEMINI_API_KEY .env dosyasında tanımlı değil!")

# --- FastAPI uygulaması oluştur ---
app = FastAPI(title="InstaFlash Backend")

# --- CORS middleware: Flutter uygulamasından istek almak için ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Geliştirme aşamasında tüm kaynaklara izin
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Kullanıcıdan alınacak JSON verisinin modeli ---
class TopicIn(BaseModel):
    topic: str

# --- Gemini API'ye istek gönderen yardımcı fonksiyon ---
def ask_gemini(topic: str) -> list[dict]:
    """
    Verilen konu başlığına göre Gemini API'den 5 adet flashcard oluşturur.
    Cevabı liste formatında döner.
    """

    # --- Gemini API endpoint URL ---
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

    # --- HTTP başlıkları ---
    headers = {"Content-Type": "application/json"}

    # --- URL parametreleri (API anahtarı) ---
    params = {"key": GEMINI_KEY}

    # --- Gemini'ye gönderilecek prompt ---
    prompt = (
        "Create exactly 5 flashcards as a JSON array. "
        "Each flashcard must be an object with 'question' and 'answer' keys only. "
        "Do not include any extra text or formatting. "
        "Return only the JSON array."
    )

    # --- İstek gövdesi ---
    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt + f" Topic: {topic}"}
                ]
            }
        ]
    }

    try:
        # --- Gemini API'ye POST isteği gönder ---
        resp = requests.post(
            url,
            headers=headers,
            params=params,
            json=body,
            timeout=20
        )

        # --- Hata kodu varsa exception fırlat ---
        resp.raise_for_status()

        # --- JSON formatındaki cevabı al ---
        data = resp.json()

        # --- Debug çıktısı: API'den dönen tam veri ---
        print("DEBUG: Full Gemini API response:")
        print(json.dumps(data, indent=2))

        # --- Yalnızca text kısmını al ---
        raw_text = data["candidates"][0]["content"]["parts"][0]["text"]

        print("DEBUG: Gemini raw response repr():")
        print(repr(raw_text))

        # Markdown kod bloğu varsa temizle
        if raw_text.startswith("```"):
         lines = raw_text.strip().split("\n")
         raw_text = "\n".join(lines[1:-1])
         
        # --- Texti güvenli şekilde Python listesine çevir ---
        cards = json.loads(raw_text)

        # --- Kontrol: liste değilse hata ver ---
        if not isinstance(cards, list):
            raise ValueError("Gemini JSON formatı hatalı")

        return cards

    except Exception as e:
        # --- Hata durumunda HTTP 500 dön ---
        raise HTTPException(status_code=500, detail=str(e))

# --- Ana endpoint: Flashcard üretir ---
@app.post("/generate-cards")
def generate_cards(payload: TopicIn):
    """
    Flutter uygulamasından gelen konu başlığını alır,
    Gemini'den flashcard üretip JSON formatında döner.
    """
    cards = ask_gemini(payload.topic)
    return {"cards": cards}

# --- Basit sağlık kontrol endpoint'i ---
@app.get("/")
def read_root():
    """
    Sunucunun çalışıp çalışmadığını test etmek için basit mesaj döner.
    """
    return {"message": "Merhaba InstaFlash!"}
