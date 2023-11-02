from confluent_kafka import Consumer, KafkaError

# Configuración del consumidor de Kafka
config = {
    'bootstrap.servers': '172.18.0.5:9092',  # Cambia esto por la dirección de tu servidor Kafka
    'group.id': 'distribuidores',
    'auto.offset.reset': 'earliest'
}

# Crea una instancia del consumidor
consumer = Consumer(config)

# Subscríbete al tema 'stock'
consumer.subscribe(['stock'])

try:
    while True:
        # Lee mensajes del tema 'stock'
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('No más mensajes en esta partición')
            else:
                print('Error al recibir mensaje: {}'.format(msg.error()))
        else:
            # Imprime el mensaje recibido con el mensaje "reponer"
            print('Reponer {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass

finally:
    # Cierra el consumidor al salir
    consumer.close()

