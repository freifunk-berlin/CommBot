# CommBot – Dein Community-Bot

In diesem Repository hosten wir den Code von CommBot. Aktuell ist Commbot ein Python-Script, dass Einladungen für die monatlichen "großen Treffen" auf der c-base verschickt.

## Deployment

Für maximale convenience sind die CommBot-Scripte in einen Alpine-Docker-Container mit eigenem crond verpackt. Dieser Container verschickt dann am Sonntagabend vor dem Treffen die Einladung.

Vor dem Deployment müssen in der `credentials.py` unbedingt die Daten des Mailserver korrekt eingetragen werden. Die Beispielstruktur findet sich in der `credentials_example.py`.

Container mit `podman` bauen. Dabei als Version am besten das aktuelle Datum angeben. So kann man die Images später auch auseinanderhalten:

```sh
podman build -t commbot:23-09-18 .
```

Die Ausgabe könnte dann in etwa so aussehen (oder auch etwas länger, wenn Alpine erstmal heruntergeladen werden muss):

```sh
STEP 1/5: FROM python:3-alpine
STEP 2/5: WORKDIR /usr/src/app
--> Using cache b6ecd19d51448208a1d23387c7bb54ad4f33c48e6df1e9dba34ae6e5dfa26f19
--> b6ecd19d5144
STEP 3/5: COPY wednesday.py main.py .
--> 36943560a6d6
STEP 4/5: RUN echo "00 18 * * 0 /usr/local/bin/python /usr/src/app/main.py" >> /var/spool/cron/crontabs/root
--> 5e7ab54ecab4
STEP 5/5: CMD [ "crond", "-f" ]
COMMIT commbot:23-09-18
--> 4d6fc9ca1334
Successfully tagged localhost/commbot:23-09-18
4d6fc9ca1334442bd8653c98e82347805c55842aa9abc859128b87ce3dedf30c
```

Den Hashwert des fertigen Images aus der letzten Zeile benutzen wir, um den Container in ein tar-Archiv zu exportieren:

```sh
$ podman save -o commbot.tar 4d6fc9ca1334442bd8653c98e82347805c55842aa9abc859128b87ce3dedf30c
Copying blob 4693057ce236 done
Copying blob 9ad60c84bfbe done
Copying blob ce0f4c80e9b7 done
Copying blob 7acf52b2a13c done
Copying blob 08928985481f done
Copying blob 79aeca5fc8df done
Copying blob f5956e81f11f done
Copying config 4d6fc9ca13 done
Writing manifest to image destination
```

Danach wird das tar-Archiv auf die Deployment-Maschine geladen. Dort kann man es mit dem `load` Komanndo importieren:

```sh
$ docker load -i commbot.tar
79aeca5fc8df: Loading layer [==================================================>]  8.704kB/8.704kB
f5956e81f11f: Loading layer [==================================================>]  8.192kB/8.192kB
Loaded image ID: sha256:4d6fc9ca1334442bd8653c98e82347805c55842aa9abc859128b87ce3dedf30c
```

Um das Image besser wiederzufinden, sollten wir es umbenennen. Als Versions-tag bietet sich das aktuelle Datum an:

```sh
docker image tag 4d6fc9ca1334442bd8653c98e82347805c55842aa9abc859128b87ce3dedf30c freifunk/commbot:23-09-18
```

Dann wird es auch vernünftig mit einem Namen in listings angezeigt:

```sh
$ docker images
REPOSITORY         TAG        IMAGE ID       CREATED          SIZE
freifunk/commbot   23-09-18   4d6fc9ca1334   13 minutes ago   52.1MB
```

Abschließend kann man den Container starten:

```sh
$ docker run -d --restart always freifunk/commbot:23-09-18
77ea2d6b77a8f7de9b1cc396f8845ae9f5a910b0fc39fa84ab929dad989cd2ef
```
