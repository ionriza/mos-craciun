# 🎅 Lista Mosului 2024 🎄

Acest proiect este o aplicație web construită cu Django pentru a aduce bucurie copiilor în perioada sărbătorilor de iarnă. Platforma permite utilizatorilor să adopte dorințele unui copil, să doneze și să creeze experiențe memorabile pentru cei mici. De asemenea, oferă un panou de administrare pentru gestionarea scrisorilor și a donatorilor (numiți „spiriduși”).

---

## 🚀 Funcționalități
- **Listă de Dorințe**: Afișează scrisorile copiilor cu dorințele lor de Crăciun.
- **Devino un Moș Crăciun**: Utilizatorii pot adopta o scrisoare, trimite detaliile lor și deveni Moș Crăciun.
- **Secțiune de Donații**: Oferă posibilitatea de a dona rapid prin Revolut pentru a susține inițiativa.
- **Experiență de Karting**: Promovează un eveniment special pentru copii, care include curse de karting, pizza, burgeri și băuturi răcoritoare.
- **Gestionare Admin**: Administrează scrisorile copiilor, urmărește adoptarea dorințelor și monitorizează starea donațiilor.
- **Tracking și Timestamps**:
  - Fiecare scrisoare și intrare a unui spiriduș urmărește data creării și actualizării.
  - Spiridușii pot marca dacă un cadou a fost trimis.

---

## 🛠️ Tehnologii Utilizate
- **[Django](https://www.djangoproject.com/)** 🐍: Framework backend pentru construirea aplicației.
- **[Bulma CSS](https://bulma.io/)** 🎨: Framework CSS pentru design și responsivitate.
- **[Vercel](https://vercel.com/)** 🚀: Platformă de hosting pentru aplicație.
- **[ChatGPT](https://openai.com/chatgpt)** 🤖: A asistat în crearea conținutului și funcționalităților.

---

## 🎄 Cum Funcționează

### 1. Listă de Dorințe
- Afișează scrisorile copiilor, categorisite după starea lor de adopție (`NOT_APPLIED`, `APPLIED`, `CONFIRMED`).
- Utilizatorii pot vedea detalii precum numele copilului, vârsta și dorințele sale.

### 2. Devino un Moș Crăciun
- Utilizatorii pot adopta o scrisoare completând detaliile lor (nume, număr de telefon și email).
- După trimitere, starea scrisorii devine **APPLIED**, iar informațiile donatorului sunt stocate.

### 3. Secțiune de Donații
- O secțiune dedicată încurajează utilizatorii să doneze prin Revolut, cu detaliile IBAN și referințele furnizate.

### 4. Experiența de Karting
- O secțiune specială descrie o zi de neuitat cu curse de karting, mâncare și distracție pentru copii.

---

## 🧑‍💻 Instalare și Configurare

### Cerințe Prealabile
- Python 3.8+
- pip (Managerul de pachete Python)
- PostgreSQL (sau orice bază de date suportată)
- [Vercel CLI](https://vercel.com/docs/cli) (pentru deployment)

### Pași

1. **Clonați Repozitoriul**:
   ```bash
   git clone https://github.com/ionriza/santa-clauss.git
   cd santa-clauss
   ```

2. **Configurați un Mediu Virtual**:
   ```bash
    python -m venv venv
    source venv/bin/activate  # Pe Windows: venv\Scripts\activate
    ```

3. **Instalați Dependențele**:
    ```bash
    pip install -r requirements.txt
    ```
   
4. **Configurați Variabilele de Mediu: Creați un fișier `.env` în rădăcina proiectului:**
    ```bash
    SECRET_KEY=your-django-secret-key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_URL=postgres://username:password@localhost:5432/dbname
    ```

5. **Aplicați Migrațiile:**
    ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Rulați Serverul de Dezvoltare:**
    ```bash
    python manage.py runserver
    ```
---

## 📜 Licență
Acest proiect este open-source și disponibil sub Licența MIT.

---

Dacă aveți nevoie de asistență suplimentară, nu ezitați să întrebați! 🎅✨