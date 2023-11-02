from confluent_kafka import Producer

config = {
    'bootstrap.servers': 'kafka3:9092',
    'client.id': 'contabilidad-producer'
}

producer = Producer(config)

topic = 'contabilidad'

while True:
    ganancia = input('Monto ganado ("exit" para salir): ')
    
    if ganancia.lower() == 'exit':
        break

    try:
        ganancia = float(ganancia)

        producer.produce(topic, key=None, value=str(ganancia))
        print(f'Datos enviados exitosamente: {ganancia}')

    except ValueError:
        print('Entrada no válida. Ingresa un número decimal.')

producer.flush()

