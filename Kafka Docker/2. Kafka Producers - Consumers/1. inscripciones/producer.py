from confluent_kafka import Producer

# Configura el productor de Kafka
producer = Producer({'bootstrap.servers': 'kafka1:9092'})

# Datos del formulario de inscripción
nombre = 'Nombre del usuario'
puesto = 'Nombre del puesto'

# Envia los datos al tema "inscripciones"
producer.produce('inscripciones', key=None, value=f'Nombre: {nombre}, Puesto: {puesto}')
producer.flush()

