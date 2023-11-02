FROM python:3.11-slim-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY main.py .

CMD ["python", "main.py"]
