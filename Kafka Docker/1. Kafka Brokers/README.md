# Docker

## Modulo de pruebas para lanzar brokers en modo clouster

 ```console
 docker compose up -d
 ```
## Modulo de pruebas para crear topicos
```console
docker exec -it kafkaX /bin/sh
kafka-topics.sh --create --bootstrap-server kafkaX:9092 --topic nombre_del_topico --partitions 3 --replication-factor 3
```
### Cambiar kafkaX por el numero del broker que se desea utilizar.

- kafka1: Topico de Inscripciones.
```console
kafka-topics.sh --create --bootstrap-server kafka1:9092 --topic inscripciones --partitions 3 --replication-factor 3
```
- kafka2: Topico de Stock
```console
kafka-topics.sh --create --bootstrap-server kafka2:9093 --topic stock --partitions 3 --replication-factor 3
```
- Kafka3: Topico de Contabilidad
```console
kafka-topics.sh --create --bootstrap-server kafka3:9094 --topic contabilidad --partitions 3 --replication-factor 3
```
### List Topics

```console
kafka-topics.sh --list --bootstrap-server localhost:9092
```

### Describe Topic

```console
kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic mytopic
```
# Creditos 
  - https://hub.docker.com/r/bitnami/kafka


