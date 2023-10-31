from confluent_kafka import Producer

broker = '172.18.0.4:9092' // verificar ip no siempre se abre aqui

producer = Producer({'bootstrap.servers': broker})
topic = 'inscripciones'

nombre = input("Ingresa un nombre: ")
nombre_tienda = input("Ingresa un nombre de tienda: ")

mensaje = f"Nombre: {nombre}, Tienda: {nombre_tienda}"

producer.produce(topic, key=None, value=mensaje)

producer.flush()

