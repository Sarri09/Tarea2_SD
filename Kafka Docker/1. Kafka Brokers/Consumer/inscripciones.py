from confluent_kafka import Consumer, KafkaError
import csv
import os

conf = {
    'bootstrap.servers': 'kafka1:9092', 
    'group.id': 'proceso-de-aprobacion',
    'auto.offset.reset': 'earliest'
}

c = Consumer(conf)

c.subscribe(['inscripciones'])

csv_filename = '/usuarios.csv'
if not os.path.exists(csv_filename):
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nombre', 'Apellido', 'Nombre de Tienda', 'Direccion', 'Paid'])

# Función para guardar datos en el archivo CSV
def guardar_en_csv(data):
    with open(csv_filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

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
        message_data = msg.value().decode('utf-8')
        nombre, tienda, es_pago = message_data.split(', ')
        nombre = nombre.split(': ')[1]
        tienda = tienda.split(': ')[1]
        es_pago = es_pago.split(': ')[1]

        datos = [nombre, tienda, es_pago]

        print('Solicitud aceptada:', message_data)

        guardar_en_csv(datos)

c.close()

