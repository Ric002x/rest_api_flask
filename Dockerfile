FROM python:3.12.7-alpine3.20

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .

CMD [ "python", "run.py" ]
