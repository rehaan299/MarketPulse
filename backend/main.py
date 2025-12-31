from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import random
from datetime import datetime

app = FastAPI(title="MarketPulse API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws/{symbol}")
async def market_stream(websocket: WebSocket, symbol: str):
    await websocket.accept()

    price = 80.0  # TD stock placeholder

    try:
        while True:
            price += random.uniform(-0.4, 0.4)
            sentiment = random.uniform(-1, 1)

            await websocket.send_json({
                "symbol": symbol,
                "timestamp": datetime.utcnow().isoformat(),
                "price": round(price, 2),
                "sentiment_score": round(sentiment, 3)
            })

            await asyncio.sleep(1)

    except WebSocketDisconnect:
        print(f"WebSocket disconnected for {symbol}")
