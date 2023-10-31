from confluent_kafka import Producer

broker = '172.18.0.4:9092' # verificar, la ip no siempre abre aqui
producer = Producer({'bootstrap.servers': broker})
topic = 'inscripciones'

nombre = input("Ingresa un nombre: ")
nombre_tienda = input("Ingresa un nombre de tienda: ")
is_paid = input("¿PAID? (True/False): ").lower()

mensaje = f"Nombre: {nombre}, Tienda: {nombre_tienda}, Es un cliente pago: {is_paid}"

if is_paid == "true":
    producer.produce(topic, key="paid", value=mensaje)
else:
    producer.produce(topic, key="not_paid", value=mensaje)

producer.flush()


