# Docker

## Build

```console
docker build -t kafka_consumer_inscription .
```

## Run

- Para inscribir a un nuevo usuario ejecutar con 

```console
docker run -it --network 1kafkabrokers_default kafka_consumer_inscription
```
## Verificar ip del broker
```console
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' kafka1
```
