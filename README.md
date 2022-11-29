# Embyes

![repo-size-badge](https://img.shields.io/github/repo-size/Zielin0/embyes?style=flat-square)
![license-badge](https://img.shields.io/github/license/Zielin0/embyes?style=flat-square)
![stars-badge](https://img.shields.io/github/stars/Zielin0/embyes?style=flat-square)
![activity-badge](https://img.shields.io/github/commit-activity/m/Zielin0/embyes?style=flat-square)

## Create your custom Open Graph Embed

## Table of Contents

1. [General info](#general-info)
2. [Features](#features)
3. [Installing](#installing)
4. [Configuring](#configuring)
5. [Running](#running)
6. [License](#license)
7. [Notes](#notes)

## General info

This project was done for learning and creative purposes. I just wanted to create a full-stack app with docker.

## Features

- Backend
  - Creating a new row with data in the database
  - Deleting a row when it expired
  - Showing data from the database
  
- Frontend
  - Simple form with [picocss](https://picocss.com/)
  - Calling the API to create the row in DB

## Installing

  ```shell
  $ git clone https://github.com/Zielin0/embyes.git

  $ cd embyes
  ```

## Configuring

- Database .env file

  ```shell
  $ cp .env.example .env
  ```

  Change the `POSTGRES_PASSWORD` to your password.

- Website .env file

  ```shell
  $ cp website/.env.example website/.env
  ```

  If you wish to use a different URL than the default just change it in the `website/.env` file.

## Running

You will need the [docker](https://www.docker.com/) for this.

If you are running for the first time:

```shell
$ docker compose up -d --build
```

If you want to close the docker containers and keep data from the database run the following:

```shell
$ ./dump_db.bat && docker compose down
```

If you want to run again and restore the database just do:

```shell
$ docker compose up -d && ./restore_db.bat
```

You will need [ngork](https://ngrok.com/) if you want to test it.

Run ngrok with http method on port `6969`.

Open another terminal window and run:

```shell
$ ngrok http 6969
```

Copy the URL from ngrok and paste it to `website/.env`.

Now visit `127.0.0.1:8080` and create a test embed.

## License

This project is under the [MIT](./LICENSE) License.

## Notes

If `docker compose` is not working for you then try `docker-compose`