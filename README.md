# 🚀 Mobile-First Python Portfolio Web App

**Author**: Advanced Level (A/L) Physical Science Student  
**Target Goal**: B.Sc. Hons in Computer Engineering  
**Stack**: Python (FastAPI), HTML5/CSS3 (Glassmorphism), Vanilla JS, PWA (Progressive Web App)

---

## 📱 Features

1. **Mobile-First Glassmorphism Design System**:
   - Ambient light glows, glass cards, and micro-interactions.
   - Built specifically for mobile viewports while looking great on desktop.

2. **Fixed Bottom Navigation Bar**:
   - 🏠 **Home**: Profile status pill, bio summary, core focus areas.
   - 🎓 **Academics**: A/L Physical Science subjects breakdown (Combined Maths, Physics, Chemistry, ICT) & Computer Engineering Roadmap.
   - 💻 **Projects & Skills**: Code showcases, embedded systems / microcontroller projects, skills matrix.
   - 📬 **Contact**: Interactive AJAX form, social links, resume download.

3. **Floating Action Button (FAB) & Radial Popup Menu**:
   - Quick **Academic CV Download** (FastAPI generated `.txt` / `.pdf` format).
   - **Dark / Light Glassmorphism Mode** persistent theme toggle.
   - **PWA Installation Prompt** for installing as a mobile phone app.

4. **FastAPI Python Backend**:
   - `/api/profile` - Profile JSON payload.
   - `/api/academics` - Academic stream data.
   - `/api/projects` - Portfolio project portfolio.
   - `/api/contact` - Asynchronous contact form processor.
   - `/api/download-cv` - Dynamic resume generator endpoint.

---

## 🛠️ How to Run Locally

### 1. Install Dependencies
```bash
cd d:/root/student-portfolio-app
pip install -r requirements.txt
```

### 2. Start the FastAPI Dev Server
```bash
python -m uvicorn app.main:app --reload --port 8000
```
Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## ☁️ 100% Free Hosting Step-by-Step Guide

### Option 1: Render.com (Recommended for FastAPI - 100% Free)
1. Push your repository to **GitHub**.
2. Sign up at [Render.com](https://render.com) (Free account).
3. Click **New +** -> **Web Service**.
4. Connect your GitHub repository.
5. Set:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Click **Create Web Service**. Your app is live with a free SSL domain!

### Option 2: Vercel (100% Free)
1. Install Vercel CLI or connect via GitHub on [Vercel.com](https://vercel.com).
2. Import project folder containing `vercel.json`.
3. Deploy instantly!
