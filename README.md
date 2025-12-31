# 📊 MarketPulse – Real-Time Financial Sentiment Dashboard

MarketPulse is a real-time financial dashboard that visualizes live stock price movements and market sentiment using WebSockets.

Built to demonstrate **frontend (Vue.js)** and **backend (FastAPI)** skills for banking and fintech internships, with TD Bank stock used as a placeholder symbol.

---

## 🚀 Features

- Real-time stock price streaming via WebSockets
- Simulated market sentiment scoring (-1 to +1)
- Live updating line chart using Chart.js
- Clean, responsive UI with Tailwind CSS
- Modern Vue 3 Composition API architecture

---

## 🛠 Tech Stack

**Frontend**
- Vue.js 3
- Chart.js + vue-chartjs
- Tailwind CSS (CDN)
- Vite

**Backend**
- FastAPI
- WebSockets
- Python asyncio

---

## ▶️ How to Run

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
