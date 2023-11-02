from confluent_kafka import Producer

broker = '172.18.0.3:9092' # verificar, la ip no siempre abre aqui
producer = Producer({'bootstrap.servers': broker})
topic = 'inscripciones'

nombre = input("Nombre: ")
apellido = input("Apellido: ") 
nombre_tienda = input("Nombre de tienda: ")
Direccion = input("Direccion de la tienda: ")
is_paid = input("¿Desea pagar para que su solicitud entre a una cola de prioridad? (True/False): ").lower()

mensaje = f"Nombre: {nombre}, Tienda: {nombre_tienda}, Es un cliente pago: {'Sí' if is_paid else 'No'}"

if is_paid == "true":
    producer.produce(topic, key="paid", value=mensaje)
else:
    producer.produce(topic, key="not_paid", value=mensaje)

producer.flush()


