FROM python:3


WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
WORKDIR /app/backend
RUN chmod +x ./runserver.sh

ENTRYPOINT [ "sh", "runserver.sh" ]