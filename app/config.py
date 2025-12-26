# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
    TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")

    if TURSO_DATABASE_URL and TURSO_AUTH_TOKEN:
        # .env에 값이 있을 시에만 Turso를 사용하도록 설정
        SQLALCHEMY_DATABASE_URI = f"sqlite+{TURSO_DATABASE_URL}?secure=true"
        CONNECT_ARGS = {"auth_token": TURSO_AUTH_TOKEN}
    else:
        print("\n[INFO] No Turso Setup: Use temporary local db...\n")
        
        # 서버리스 환경에서는 /tmp 폴더만 쓰기가 가능합니다.
        INSTANCE_DIR = "/tmp/instance" 
        os.makedirs(INSTANCE_DIR, exist_ok=True)

        SQLALCHEMY_DATABASE_URI = f"sqlite:///{INSTANCE_DIR}/reviews.db"
        CONNECT_ARGS = {"check_same_thread": False}