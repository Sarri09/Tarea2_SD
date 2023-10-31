# Docker

## Modulo de pruebas para lanzar brokers en modo clouster

 ```
    docker compose up -d
 ```
## Modulo de pruebas para crear topicos
```
    docker exec -it kafkaX /bin/sh
    kafka-topics.sh --create --bootstrap-server kafkaX:9092 --topic nombre_del_topico --partitions 3 --replication-factor 3

```
### Cambiar kafkaX por el numero del broker que se desea utilizar.

- kafka1: Topico de Inscripciones.
```
kafka-topics.sh --create --bootstrap-server kafka1:9092 --topic inscripciones --partitions 3 --replication-factor 3
```
- kafka2: Topico de Stock
```
kafka-topics.sh --create --bootstrap-server kafka2:9093 --topic stock --partitions 3 --replication-factor 3
```
- Kafka3: Topico de Contabilidad
```
kafka-topics.sh --create --bootstrap-server kafka3:9094 --topic contabilidad --partitions 3 --replication-factor 3
```
### List Topics

```
kafka-topics.sh --list --bootstrap-server localhost:9092
```

### Describe Topic

```
kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic mytopic
```
# Creditos 
  - https://hub.docker.com/r/bitnami/kafka


