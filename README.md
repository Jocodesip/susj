# Sustav upravljanja saksofonskim jezičcima (SUJSJ)

Ovaj projekt je jednostavna Flask aplikacija za upravljanje saksofonskim jezičcima. Omogućuje korisnicima dodavanje, pregledavanje, ažuriranje i brisanje jezičaka. Aplikacija je kontejnerizirana pomoću Dockera, što olakšava njezino postavljanje i pokretanje.



## Preduvjeti

- Python 3.9+
- Docker (za kontejnerizaciju)
- Git

## Instalacija

### Kloniranje Repozitorija

1. Klonirajte repozitorij:

    ```sh
    git clone https://github.com/vaše_korisničko_ime/flask_app.git
    cd flask_app
    ```

### Postavljanje Virtualnog Okruženja

2. Kreirajte virtualno okruženje i aktivirajte ga:

    ```sh
    python -m venv venv
    source venv/bin/activate  # Na Windowsu koristite `venv\Scripts\activate`
    ```

3. Instalirajte ovisnosti:

    ```sh
    pip install -r requirements.txt
    ```

## Pokretanje Aplikacije Lokalno

Za pokretanje aplikacije lokalno bez Dockera:

1. Provjerite je li virtualno okruženje aktivirano.

2. Pokrenite Flask aplikaciju:

    ```sh
    python run.py
    ```

Aplikacija će biti dostupna na `http://localhost:5000`.

## Pokretanje Aplikacije s Dockerom

Za izgradnju i pokretanje aplikacije koristeći Docker:

1. Izgradite Docker sliku:

    ```sh
    docker build -t reed1 .
    ```

2. Pokrenite Docker kontejner:

    ```sh
    docker run -p 5000:5000 reed1
    ```

Aplikacija će biti dostupna na `http://localhost:5000`.

## Korištenje Aplikacije

Aplikacija pruža web sučelje za upravljanje jezičcima. Možete dodavati, uređivati i brisati jezičke kroz obrazac na glavnoj stranici.

### Dodavanje Jezička

1. Otvorite aplikaciju u svom web pregledniku.
2. Ispunite podatke o jezičku u obrascu.
3. Kliknite na gumb "Dodaj jezičak".

### Uređivanje Jezička

1. Kliknite na gumb "Uredi" pored jezička kojeg želite urediti.
2. Unesite nove podatke u prompt.
3. Potvrdite promjene.

### Brisanje Jezička

1. Kliknite na gumb "Izbriši" pored jezička kojeg želite izbrisati.
2. Potvrdite brisanje.

## Doprinosi

Doprinosi su dobrodošli! Slijedite ove korake kako biste doprinijeli:

1. Forkajte repozitorij.
2. Kreirajte novu granu (`git checkout -b feature-branch`).
3. Napravite svoje promjene.
4. Commitajte svoje promjene (`git commit -m 'Dodaj neku značajku'`).
5. Pushajte na granu (`git push origin feature-branch`).
6. Otvorite pull request.

## Licenca

Ovaj projekt je licenciran pod MIT licencom - pogledajte [LICENSE](LICENSE) datoteku za detalje.

## Kontakt

Za sva pitanja ili prijedloge, otvorite issue ili kontaktirajte vlasnika repozitorija.

