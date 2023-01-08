# Skintect
Skintect ist ein Semester Projekt bei dem Hautkrebs mittels eines Neuronalennetz erkannt werden soll. Dieses Netz wurde mit HAM10000 Datensatz Trainiert

### Ausführen
zum Ausprobieren Runterladen, [Docker](https://docs.docker.com/get-docker/) instalieren, im Terminal in den Ordner navigieren, dort mit dem Befehl: (der punkt im nächsten befehl ist wichtig)
```docker
docker image build -t skintect .
```
 in docker laden und mit :
 ```docker
 docker run -p 5000:5000 -d skintect 
 ```
Nun kann die Website unter: lockalhoste:5000 aufgerufen werden. 
Viel spass beim Ausprobieren.
