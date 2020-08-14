FROM python:alpine3.12

LABEL Maintainer="Aakash Garg"

WORKDIR /usr/src/app

COPY hostName.py .

CMD [ "python", "hostName.py" ]