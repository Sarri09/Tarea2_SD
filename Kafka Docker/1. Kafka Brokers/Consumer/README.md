# Docker

## Build

```console
docker build -t kafka_consumer .
```

## Run

- Para inscribir a un nuevo usuario ejecutar con 

```console
docker run -it --network 1kafkabrokers_default kafka_consumer
```
## Verificar ip del broker
```console
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' kafka1
```
```console
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' kafka2
```
```console
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' kafka3
```
