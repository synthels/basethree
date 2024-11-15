FROM python:3.10

WORKDIR /server

COPY . .

RUN python -m pip install -r requirements.txt

CMD ["flask", "--app", "src/server.py", "--debug", "run"]
