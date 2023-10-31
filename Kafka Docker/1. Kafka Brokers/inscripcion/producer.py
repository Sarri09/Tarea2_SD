from confluent_kafka import Producer

# Configura el productor de Kafka
producer = Producer({'bootstrap.servers': 'kafka1:9092'})  

# Solicitar al usuario que ingrese los datos del formulario de inscripción
nombre = input("Nombre del usuario: ")
puesto = input("Nombre del puesto: ")

# Envia los datos al tema "inscripciones"
producer.produce('inscripciones', key=None, value=f'Nombre: {nombre}, Puesto: {puesto}')
producer.flush()

