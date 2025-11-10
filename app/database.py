import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv('app/.env')

DATABASE_URL = os.environ.get("DATABASE_URL")

Base = declarative_base()

if not DATABASE_URL or DATABASE_URL.strip() in ["", "postgres database"]:
    print("⚠️ No valid DATABASE_URL found. Running in NO-DB mode.")
    engine = None
    SessionLocal = None
else:
    print(f"✅ Using database: {DATABASE_URL}")
    if DATABASE_URL.startswith("sqlite"):
        engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    else:
        engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
