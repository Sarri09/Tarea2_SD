FROM python:3
COPY ./consumer.py /app/consumer.py
WORKDIR /app
RUN pip install confluent-kafka
CMD ["python", "consumer.py"]

