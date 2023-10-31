from confluent_kafka import Consumer, KafkaError

conf = {
    'bootstrap.servers': 'kafka1:9092',  # Cambia a la dirección y puerto correctos si es necesario
    'group.id': 'proceso-de-aprobacion',
    'auto.offset.reset': 'earliest'  # Inicializar desde el principio del topic
}

consumer = Consumer(conf)

consumer.subscribe(['inscripciones'])

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('No more messages')
            else:
                print('Error al recibir mensaje: {}'.format(msg.error()))
        else:
            message_str = msg.value().decode('utf-8')

            parts = message_str.split(',')
            if len(parts) >= 2:
                user_name = parts[0].strip()
                store_name = parts[1].strip()

                print(f'Usuario: {user_name[8:]}')
                print(f'Clave: {store_name[8:]}')
                print('---')  # Separador entre mensajes

except KeyboardInterrupt:
    pass

finally:
    consumer.close()

