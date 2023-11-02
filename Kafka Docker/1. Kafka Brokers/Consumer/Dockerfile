FROM python:3
COPY ./inscripciones.py /app/inscripciones.py
COPY ./stock.py /app/stock.py
WORKDIR /app
RUN pip install confluent-kafka
CMD ["/bin/bash"]

