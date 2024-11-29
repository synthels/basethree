FROM python:3.10

WORKDIR /server

COPY . .

RUN python -m pip install -r requirements.txt

CMD ["flask", "--app", "src/server.py", "run", "--host", "0.0.0.0"]
