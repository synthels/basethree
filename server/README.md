# server

Flask REST API.

## Run

To run in dev mode, create a virtual environment with

```sh
python3 -m venv .env
source .env/bin/activate
```

install all dependencies

```sh
pip install -r requirements.txt
```

and finally

```sh
flask --app src/server.py --debug run
```
