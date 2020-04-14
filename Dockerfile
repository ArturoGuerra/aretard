FROM python:3.8-buster

WORKDIR /app
ADD requirements.txt .
RUN apt update && apt install build-essential -y
RUN pip install -r ./requirements.txt

ADD . .

CMD ["python3.8", "./main.py"]