from confluent_kafka import Consumer, KafkaError

# Configura el consumidor de Kafka
consumer = Consumer({
    'bootstrap.servers': 'kafka1:9092',
    'group.id': 'mi-grupo',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe(['inscripciones'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    print('Recibido: {}'.format(msg.value()))

    # Procesa los datos y envía una confirmación (implementa tu lógica aquí)

consumer.close()

