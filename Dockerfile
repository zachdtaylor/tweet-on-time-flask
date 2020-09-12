FROM python:3.7-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

EXPOSE 8080

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=tweetontime

RUN flask init-db

CMD ["waitress-serve", "--call", "tweetontime:create_app"]
