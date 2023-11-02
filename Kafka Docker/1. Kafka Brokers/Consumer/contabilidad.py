from confluent_kafka import Consumer, KafkaError

config = {
    'bootstrap.servers': 'kafka3:9092', 
    'group.id': 'contabilidad',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(config)

consumer.subscribe(['contabilidad'])

venta_count = 0
total_ganancias = 0.0

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
            venta_count += 1
            ganancia = float(msg.value().decode('utf-8'))
            total_ganancias += ganancia
            print(f'Venta del dia {venta_count}: Ganancia ${ganancia:.2f}')

            if venta_count % 7 == 0:
                print(f'Suma total de ganancias de la ultima semana: ${total_ganancias:.2f}')

except KeyboardInterrupt:
    pass

finally:
    consumer.close()

