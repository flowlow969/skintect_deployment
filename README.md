# Skintect
Skintect ist ein Semesterprojekt, bei dem Hautkrebs mittels eines neuronalen Netzes erkannt werden soll. Dieses Netz wurde mit dem HAM10000 Datensatz trainiert.

### Ausführen
Zum Ausprobieren runterladen, [Docker](https://docs.docker.com/get-docker/) installieren, im Terminal in den Ordner navigieren, dort mit dem Befehl: (der Punkt im nächsten Befehl ist wichtig)
```docker
docker image build -t skintect .
```
WICHTIG: Unter Windows muss das Windows Subsystem für Linux (WSL) installiert werden. Dazu wird folgender Befehl zur Installation benötigt:

```
wsl --install
```
 in docker laden und mit :
 ```docker
 docker run -p 5000:5000 -d skintect 
 ```
Nun kann die Website unter: lockalhoste:5000 aufgerufen werden. 
Viel Spaß beim Ausprobieren.


