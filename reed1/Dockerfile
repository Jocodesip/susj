# Koristi službenu Python sliku s Docker Huba
FROM python:3.9-slim

# Postavi radni direktorij
WORKDIR /app

# Kopiraj sadržaj trenutnog direktorija u kontejner na /app
COPY . /app

# Instaliraj potrebne pakete navedene u requirements.txt
RUN pip install Flask==2.0.2 Werkzeug==2.0.3

# Omogući port 5000 za vanjski pristup ovom kontejneru
EXPOSE 5000

# Definiraj varijablu okruženja
ENV FLASK_APP=run.py

# Pokreni app.py kada se kontejner pokrene
CMD ["flask", "run", "--host=0.0.0.0"]
