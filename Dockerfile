# ---- Base image ----
FROM python:3.11-slim

# ---- Set working directory ----
WORKDIR /app

# ---- Environment setup ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- Install system dependencies ----
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ---- Install Python dependencies ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy app source ----
COPY app ./app
COPY alembic ./alembic
COPY .env ./

# ---- Expose FastAPI port ----
EXPOSE 5000

# ---- Run FastAPI using Uvicorn ----
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
