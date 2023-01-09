# Skintect
Skintect ist ein Semesterprojekt, bei dem Hautkrebs mittels eines neuronalen Netzes erkannt werden soll. Dieses Netz wurde mit dem HAM10000 Datensatz trainiert.

### Ausführen
**WICHTIG**: Unter Windows muss zunächst das Windows Subsystem für Linux (WSL) installiert werden, um  eine Linux-Distribution zu installieren und Linux-Anwendungen, Dienstprogramme und Bash-Befehlszeilentools direkt unter Windows unverändert verwenden zu können, ohne den Overhead einer herkömmlichen virtuellen Maschine oder eines Dual-Boot-Setups. Windows 10 version 2004 oder eine aktuellere Version wird vorausgesetzt.<br> 
Dazu wird folgender Befehl zur Installation benötigt:

```
wsl --install
```

Zum Ausprobieren das [skintect_deployment](https://github.com/flowlow969/skintect_deployment) Repository runterladen, [Docker](https://docs.docker.com/get-docker/) installieren, im Terminal in den Ordner navigieren, dort mit dem folgenden Befehl den Dockercontainer erstellen: (der Punkt im am Ende des Befehls ist wichtig). 

```docker
docker image build -t skintect .
```

Mit dem folgenden Befehl wird der Container in Docker geöffnet:

 ```docker
 docker run -p 5000:5000 -d skintect 
 ```
Nun kann die Website entweder über das Docker-Desktop Programm geöffnet oder unter: localhost:5000 im Browser aufgerufen werden. 
# Viel Spaß beim Ausprobieren!


