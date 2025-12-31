from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import random
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws/{symbol}")
async def stream_stock_data(websocket: WebSocket, symbol: str):
    await websocket.accept()
    price = 80.0  # starting price for TD (placeholder)

    try:
        while True:
            price += random.uniform(-0.5, 0.5)
            sentiment = random.uniform(-1, 1)

            payload = {
                "symbol": symbol,
                "timestamp": datetime.utcnow().isoformat(),
                "price": round(price, 2),
                "sentiment_score": round(sentiment, 3),
            }

            await websocket.send_json(payload)
            await asyncio.sleep(1)

    except WebSocketDisconnect:
        print(f"Disconnected from {symbol}")
