FROM python:3.7

WORKDIR /app

COPY . /app

ADD . /app/output

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python", "./main.py"]