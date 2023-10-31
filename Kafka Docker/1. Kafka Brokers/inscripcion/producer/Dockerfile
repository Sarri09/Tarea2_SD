FROM python:3

COPY ./producer.py /app/producer.py

WORKDIR /app

RUN pip install confluent-kafka

CMD ["python", "producer.py"]

