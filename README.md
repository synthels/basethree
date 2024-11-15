# basethree

Competitive math app built on vue with a flask backend. 

## Cloning

Make sure to clone the repo recursively, like so

```
git clone --recursive https://github.com/synthels/basethree.git
```

## Running in dev mode

First, you'll need to create a file named `.config` in the `server` directory. This file should contain the following variables.

* `SESSION_SECRET`: Used in signing session and CSRF tokens. See
[here](https://flask.palletsprojects.com/en/stable/config/#SECRET_KEY).
* `PG_MIN_CONNECTIONS`: Minimum connections for pooling.
* `PG_MAX_CONNECTIONS`: Maximum connections for pooling.
* `PG_DATABASE`: Database name.
* `PG_HOST`: Database hostname (should probably be `postgres`, not `localhost`).
* `PG_USER`: Database admin username.
* `PG_PASSWORD`: Database admin password.
* `PG_PORT`: Should be set to `5432`.
* `NODE_PORT`: Should be set to `5173`.
* `BACKEND_PORT`: Should be set to `5000`.

From then on, make sure you have [Docker](https://docker.com) installed. In the root directory, do

```
docker-compose --env-file ./server/.config up
```

once this step is done, both the frontend, the backend and the database should be running in separate containers.
