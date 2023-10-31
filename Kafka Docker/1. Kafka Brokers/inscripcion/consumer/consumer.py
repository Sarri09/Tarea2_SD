from confluent_kafka import Consumer, KafkaError
import base64

broker = '172.18.0.4:9092'

consumer = Consumer({
    'bootstrap.servers': broker,
    'group.id': 'my-group',  
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['inscripciones'])  

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Fin de partición alcanzado')
        else:
            print('Error en el mensaje: {}'.format(msg.error()))
    else:
        mensaje = msg.value()

        mensaje_encriptado = base64.b64encode(mensaje.encode()).decode()

        print('Mensaje encriptado: {}'.format(mensaje_encriptado))
