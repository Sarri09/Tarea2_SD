import sys
from confluent_kafka import Producer

config = {
    'bootstrap.servers': 'ipdekafka2:9093',  
    'client.id': 'ingredient-producer'
}

producer = Producer(config)

topic = 'stock'

def delivery_report(err, msg):
    if err is not None:
        print('Error al enviar el mensaje: {}'.format(err))
    else:
        print('Mensaje enviado a {} [{}]'.format(msg.topic(), msg.partition()))

while True:
    ingredient = input('Ingresa un ingrediente o "salir" para finalizar: ')
    
    if ingredient.lower() == 'salir':
        break

    producer.produce(topic, key=None, value=ingredient, callback=delivery_report)

producer.flush()

