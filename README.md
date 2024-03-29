# tweet-on-time

A bot that will tweet for you at a specific time

## Installation

```console
$ git clone git@github.com:zachtylr21/tweet-on-time.git
```

## Set up

There are a few things you need to do before you can run the application.

### 1) Set up a virtual environment

It is highly recommended that you use virtual environments when working with python. You can set one up with

```console
$ python3 -m venv env
```

then activate it with

```console
$ source env/bin/activate
```

### 2) Install required packages

Install required packages with

```console
$ pip install -r requirements.txt
```

### 3) Get Twitter API credentials

You will need to [apply](https://developer.twitter.com/en/apply-for-access) for a Twitter developer account. Once your application is accepted,
you should get an API key and secret, bearer token, and an access token and secret. You should pass these values to the application through environment
variables or in a `.env` file at the root of the project. For example:

```text
API_KEY=<api_key>
API_SECRET_KEY=<api_secret>
BEARER_TOKEN=<bearer_token>
ACCESS_TOKEN=<access_token>
ACCESS_TOKEN_SECRET=<access_token_secret>
```

## Run

To run the application, do

```console
$ flask run
```

## Run in production with Docker

First, you need to build the image

```console
$ docker build -t tweetontime:latest .
```

Once the image is built, you can run the contianer. I recommend storing the necessary environment variables in a `.env` file at the root of the project. You must pass all Twitter API credentials and a `SECRET_KEY` which Flask uses for computing session cookies. You can either put the `SECRET_KEY` in the `.env` file or pass it as a separate environment variable.

```console
$ docker run --name tweetontime -d -p 8080:8080 -v /absolute/path/to/.env:/app/.env -e SECRET_KEY=<random_secret_key> tweetontime:latest
```

## Built with

This application is built with Flask and SQLite. The front end is built with Jinja templates served by Flask.
