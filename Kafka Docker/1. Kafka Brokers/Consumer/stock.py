from confluent_kafka import Consumer, KafkaError

# Configuración del consumidor de Kafka
config = {
    'bootstrap.servers': 'kafka2:9092',  
    'group.id': 'distribuidores',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(config)

consumer.subscribe(['stock'])

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('No más mensajes en esta partición')
            else:
                print('Error al recibir mensaje: {}'.format(msg.error()))
        else:
            print('Reponer {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass

finally:
    consumer.close()

