FROM python:3.11-slim

WORKDIR /web_app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000 & \
    streamlit run web_app.py --server.port=8501 --server.address=0.0.0.0
