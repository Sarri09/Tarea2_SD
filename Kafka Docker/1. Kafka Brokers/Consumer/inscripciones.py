from confluent_kafka import Consumer, KafkaError
import csv
import os

# Configura el consumidor de Kafka
conf = {
    'bootstrap.servers': '172.18.0.3:9092',  # Tu dirección de broker
    'group.id': 'proceso-de-aprobacion',
    'auto.offset.reset': 'earliest'
}

c = Consumer(conf)

# Suscríbete al topic 'inscripciones'
c.subscribe(['inscripciones'])

# Verifica si el archivo CSV ya existe
csv_filename = '/usuarios.csv'
if not os.path.exists(csv_filename):
    # Si no existe, crea un archivo CSV con encabezados
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nombre', 'Apellido', 'Nombre de Tienda', 'Direccion', 'Paid'])

# Función para guardar datos en el archivo CSV
def guardar_en_csv(data):
    with open(csv_filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Consumir mensajes de Kafka y guardarlos en el archivo CSV
while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('No más mensajes de partición')
        else:
            print('Error en el consumidor: {}'.format(msg.error()))
    else:
        # Procesa el mensaje y extrae los datos
        message_data = msg.value().decode('utf-8')
        nombre, tienda, es_pago = message_data.split(', ')
        nombre = nombre.split(': ')[1]
        tienda = tienda.split(': ')[1]
        es_pago = es_pago.split(': ')[1]

        # Divide los datos en una lista
        datos = [nombre, tienda, es_pago]

        # Imprime el mensaje
        print('Solicitud aceptada:', message_data)

        # Guarda los datos en el archivo CSV
        guardar_en_csv(datos)

# Cierra el consumidor de Kafka al final
c.close()

