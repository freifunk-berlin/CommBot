FROM python:3-alpine

WORKDIR /usr/src/app

# Commbot-Files
COPY credentials.py main.py message.py wednesday.py .

# Cool resource for cron in alpine-docker:
# https://mixu.wtf/cron-in-docker-alpine-image/
RUN echo "00 18 * * 0 /usr/local/bin/python /usr/src/app/main.py" >> /var/spool/cron/crontabs/root

# Debugging-line: Should print output of script
CMD [ "crond", "-f" ]
