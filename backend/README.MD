# InstaFlash Backend

FastAPI tabanlı backend uygulaması.  
Gemini API üzerinden flashcard (soru-cevap kartı) üretir.  
Flutter mobil uygulaması bu servisi kullanır.

---

## 🚀 Kurulum Adımları

### 1️⃣ Proje klasörünü klonlayın veya indirin

```bash
git clone <repo-adresi>
cd instaflash_backend
```

Veya klasörü ZIP olarak alıp açın.

---

### 2️⃣ Sanal ortam oluşturun

Windows:
```powershell
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Gerekli paketleri yükleyin

```bash
pip install -r requirements.txt
```

Eğer `requirements.txt` yoksa:

```bash
pip install fastapi uvicorn python-dotenv requests
```

---

### 4️⃣ Ortam değişkenlerini tanımlayın

Proje kök klasöründe `.env` dosyası oluşturun:

> `.env.example` dosyasını kopyalayın:

Windows:
```powershell
copy .env.example .env
```

Mac/Linux:
```bash
cp .env.example .env
```

`.env` dosyasını açıp kendi API anahtarınızı yazın:

```
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Her ekip üyesi **kendi API key'ini kullanmalıdır.**

---

### 5️⃣ Sunucuyu başlatın

```bash
uvicorn main:app --reload
```

Başarılı başladığında şu çıkışı görürsünüz:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## 🧪 API Testi

Tarayıcıda açın:
```
http://127.0.0.1:8000/docs
```

Swagger arayüzünde `POST /generate-cards` endpointini deneyin.

Örnek istek:

```json
{
  "topic": "Photosynthesis"
}
```

Örnek yanıt:

```json
{
  "cards": [
    {"question": "...", "answer": "..."},
    ...
  ]
}
```

---

## ⚙️ Dosya Yapısı

```
instaflash_backend/
├── main.py              # FastAPI uygulaması
├── .env                 # API anahtarınız (repoya koymayın)
├── .env.example         # Şablon dosya
├── requirements.txt     # Gerekli Python paketleri
└── README.md            # Bu dosya
```

---

## ⚠️ Önemli Notlar

- `.env` dosyanızı repoya eklemeyin.
- Her ekip üyesi kendi Google API key'ini oluşturabilir:
  [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
- Ortak API key kullanılacaksa Google Cloud Console'da kota limiti belirleyin.
- Yanlışlıkla key'i paylaşırsanız hemen silip yeni key oluşturun.

---


