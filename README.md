# Sustav upravljanja saksofonskim jezičcima (SUJSJ)

Ovaj projekt je jednostavna Flask aplikacija za upravljanje saksofonskim jezičcima. Omogućuje korisnicima dodavanje, pregledavanje, ažuriranje i brisanje jezičaka. Aplikacija je kontejnerizirana pomoću Dockera, što olakšava njezino postavljanje i pokretanje.

## Preduvjeti

- Python 3.9+
- Flask-SQLAlchemy
- Docker (za kontejnerizaciju)
- Git

## Instalacija

Kloirajte ovaj repozitorij na svoje računalo: 

git clone https://github.com/Jocodesip/susj.git
cd reed1

## Gradnja Docker slike

Otvorite cmd unutar direktorija reed1 kako bi se skinuli potrebni dependency

docker build -t my-flask-app .

## Pokretanje Docker kontejnera

docker run -d -p 8000:8000 --name flask-app-container -v C:\Put\Do\Tvog\Direktorija\instance:/app/instance my-flask-app

Napomena: Zamijenite C:\Put\Do\Tvog\Direktorija sa stvarnom putanjom do direktorija gdje ste klonirali repozitorij.

#Pristup aplikaciji

http://localhost:8000


## Pokretanje Aplikacije Lokalno

Kako bi se skinuli svi depedency iz "requirments.txt"

docker build -t my-flask-app .


## Korištenje Aplikacije

Aplikacija pruža web sučelje za upravljanje jezičcima. Možete dodavati, uređivati i brisati jezičke kroz obrazac na glavnoj stranici.

### Dodavanje Jezička

1. Otvorite aplikaciju u svom web pregledniku.
2. Ispunite podatke o jezičku u obrascu.
3. Kliknite na gumb "Add Reed".

### Uređivanje Jezička

1. Kliknite na gumb "Edit" pored jezička kojeg želite urediti.
2. Unesite nove podatke u prompt.
3. Potvrdite promjene.

### Brisanje Jezička

1. Kliknite na gumb "Delete" pored jezička kojeg želite izbrisati.
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
