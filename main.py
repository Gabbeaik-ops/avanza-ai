import yfinance as yf
import requests
import time
from datetime import datetime
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

AKTIER = [
    "VOLV-B.ST",
    "ERIC-B.ST",
    "SSAB-B.ST",
    "SINCH.ST",
    "SBB-B.ST",
    "KINV-B.ST",
    "TELIA.ST"
]

send("🤖 Avanza-AI startad")

while True:
    for aktie in AKTIER:
        try:
            data = yf.download(aktie, period="1d", interval="5m", progress=False)

            if len(data) < 6:
                continue

            close = float(data["Close"].iloc[-1])
            high_prev = float(data["High"].iloc[-6:-1].max())

            if close > high_prev:
                send(
                    f"🚀 BREAKOUT\n\n"
                    f"Aktie: {aktie}\n"
                    f"Pris: {close:.2f} kr\n"
                    f"Tid: {datetime.now().strftime('%H:%M')}"
                )

        except:
            pass

    time.sleep(300)
