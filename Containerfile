FROM python:3.9-alpine3.19

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./src /opt/

WORKDIR /opt/

CMD [ "python", "/opt/main.py" ]