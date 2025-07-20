## 🚀 Gelişim Süreci

<details>
  <summary>✅ Sprint 1 – Proje Kurulumu ve MVP Backend</summary>

#### 🎯 Hedef:
Projenin temel yapısını oluşturmak ve Gemini API ile çalışan bir backend ortaya çıkarmak.

#### 🔧 Yapılanlar:
- ✅ Proje fikri ve görev paylaşımı tamamlandı (backend: Ataman)
- ✅ Flutter ile mobil uygulama yapılmasına karar verildi
- ✅ Python + FastAPI backend için ortam hazırlandı:
  - Python, VS Code, Flutter, Android Studio kurulumları
  - Virtual environment (`venv`) oluşturuldu
- ✅ Gerekli kütüphaneler yüklendi:
  - `fastapi`, `uvicorn`, `python-dotenv`, `requests`, `pydantic`
- ✅ `.env` ile gizli API anahtarı yönetimi sağlandı
- ✅ Gemini API ile entegrasyon kuruldu
- ✅ `/generate-cards` POST endpoint’i geliştirildi
- ✅ CORS middleware ile Flutter bağlantısı için izin verildi
- ✅ Swagger arayüzü üzerinden test edildi (`/docs`)
- ✅ Git'e özel dosyalar eklendi:
  - `.gitignore`, `.env.example`, `README.md`
- ✅ Backend GitHub reposuna yüklendi (`/backend` dizini)

#### 📦 Çıktı:
- MVP backend başarıyla çalışır hale getirildi.
- Gemini API’den flashcard alan servis yayında.

</details>

<details>
  <summary>✅ Sprint 2 – Kullanıcı Arayüzü Senaryosu ve Entegrasyon Hazırlığı</summary>

#### 🎯 Hedef:
Kullanıcının arayüzden butonla konu seçerek kart alacağı deneyimi tasarlamak ve API’yi buna uygun hale getirmek.

#### 🔧 Yapılanlar:
- ✅ Kullanıcı deneyimi senaryosu tasarlandı:
  - Kullanıcı “Genel Kültür” gibi bir butona tıklayacak
  - API'den 5 flashcard dönecek
  - Kartlar tıklanınca arkası dönecek (soru/cevap yapısı)
- ✅ Flutter tarafında kullanılabilirlik için planlama yapıldı
- ✅ API testleri gerçek kullanım senaryosuyla tekrarlandı
- ✅ Prompt yapısı genel konular için esnekleştirildi
- ✅ FastAPI’nin stateless olduğu tespit edildi
- ✅ Firebase ve dosyaya kayıt gibi ileri adımlar planlandı (Sprint 3’e)

#### 📦 Çıktı:
- Kullanıcı senaryosuna uygun çalışan API hazırlandı
- Flutter ile uyumlu yapı kuruldu

</details>

<details> <summary>🗺️ Yol Haritası (Güncel)</summary>
🔜 Planlanan Geliştirmeler
 Sprint 3 – Flashcard’ların kalıcı gösterimi

Butonlar üzerinden sabit konu başlıklarıyla kart üretimi (örn. “Genel Kültür”)

Kartların soru–cevap olacak şekilde çevrilebilir yapıda gösterimi

 Flutter ile tam entegrasyon

Flutter üzerinden API’ye istek atma

Kartların görsel olarak listelenmesi

 Konu kategorilerinin artırılması (Tarih, Bilim, Sanat vs.)

 Kartlara animasyonlu “çevirme” efekti eklenmesi

 Offline mod desteği (isteğe bağlı olarak önbellekleme ile)

 (Opsiyonel) Kullanıcının cihazına veri kaydedilmesi (local storage)

</details>

🚀 (English) Development Timeline
<details> <summary>✅ Sprint 1 – Project Setup and MVP Backend</summary>
#### 🎯 Goal:
Establish the project foundation and build a working backend integrated with the Gemini API.

#### 🔧 Tasks Completed:
✅ Defined the project idea and team responsibilities (backend: Ataman)

✅ Decided to build the mobile app using Flutter

✅ Set up the development environment for Python + FastAPI:

Installed Python, VS Code, Flutter, Android Studio

Created a virtual environment (venv)

✅ Installed required packages:

fastapi, uvicorn, python-dotenv, requests, pydantic

✅ Set up environment variable management using .env

✅ Integrated Gemini API

✅ Developed a POST endpoint /generate-cards

✅ Enabled CORS middleware for Flutter integration

✅ Successfully tested the backend via Swagger UI (/docs)

✅ Added project essentials:

.gitignore, .env.example, README.md

✅ Pushed the backend code to GitHub (/backend directory)

#### 📦 Outcome:
A working MVP backend was delivered

Gemini API successfully generates flashcards via API

</details> <details> <summary>✅ Sprint 2 – UI Scenario Planning and API Integration Prep</summary>
#### 🎯 Goal:
Design a user interaction flow where pressing a button fetches topic-based flashcards, and ensure the backend supports this.

#### 🔧 Tasks Completed:
✅ Created the user experience scenario:

User clicks on a button (e.g., "General Knowledge")

API returns 5 flashcards

Cards show the question on the front and answer on the back (flip effect)

✅ Planned how the Flutter frontend will consume the API

✅ Re-tested the API in a real-world scenario

✅ Improved the prompt structure to handle general topics more flexibly

✅ Confirmed the backend is stateless

✅ Planned future features like data persistence (for Sprint 3)

#### 📦 Outcome:
API is now compatible with the planned UI experience

Flutter-ready backend completed
</details>

<details> <summary>🗺️ Roadmap (Updated)</summary>
🔜 Planned Features
 Sprint 3 – Persistent Flashcard Display

Generate flashcards based on fixed topics (e.g., “General Knowledge”)

Display cards with front/back flip (question → answer)

 Full Flutter integration

Send API requests from Flutter

Visually display cards in a scrollable list

 Expand topic categories (History, Science, Art, etc.)

 Add card flip animation and smooth transitions

 Offline mode support (optional: local cache)

 (Optional) Store flashcards locally on the device (no login required)

</details
