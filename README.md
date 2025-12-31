# MarketPulse 📊  
**Real-Time Financial Sentiment Dashboard**

MarketPulse is a real-time stock monitoring dashboard that streams live price movements and market sentiment using WebSockets.

Built to demonstrate **frontend engineering (Vue 3)** and **backend systems (FastAPI)** skills for banking and fintech roles, with TD Bank stock used as a realistic placeholder.

---

## What It Does

- Streams live stock price updates every second  
- Simulates market sentiment scores (−1 to +1)  
- Pushes data in real time via WebSockets (no polling)  
- Visualizes trends with a responsive line chart  
- Highlights sentiment instantly with clear visual cues  

---

## Tech Stack

**Frontend**
- Vue 3 (Composition API)
- Chart.js (via vue-chartjs)
- Tailwind CSS
- Vite

**Backend**
- FastAPI
- WebSockets
- Async Python

---

## How It Works (Simple)

1. FastAPI opens a WebSocket connection per stock symbol  
2. Backend simulates a price random walk + sentiment score  
3. Data is pushed every second to connected clients  
4. Vue listens to the stream and updates the UI instantly  
5. Chart and sentiment badge react in real time  

---

## WebSocket Payload

```json
{
  "symbol": "TD",
  "timestamp": "2026-01-01T12:00:00Z",
  "price": 81.42,
  "sentiment_score": 0.31
}
