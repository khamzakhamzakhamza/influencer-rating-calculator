# ---------- FRONTEND (Vite React) ----------
FROM node:18 AS frontend-build

WORKDIR /frontend

COPY node/package*.json .
RUN npm install

COPY node/ .
RUN npm run build

# ---------- BACKEND (FastAPI) ----------
FROM python:3.11-slim AS backend-build

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY python/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY python /app

COPY --from=frontend-build /frontend/dist ../node/dist

RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
