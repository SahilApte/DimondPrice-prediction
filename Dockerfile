FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app

RUN apt-get update 
RUN apt-get install -y awscli
RUN apt-get update 

RUN apt-get install -y ffmpeg libsm6 libxext6 unzip -y

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
