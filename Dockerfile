FROM python:3.11-slim

# Skapa arbetskatalog
WORKDIR /app

# Kopiera filer
COPY . .

# Installera beroenden
RUN pip install --no-cache-dir -r requirements.txt

# Kör bot.py
CMD ["python", "bot.py"]
