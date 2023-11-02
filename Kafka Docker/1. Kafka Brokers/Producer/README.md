# Docker

## Build

```console
docker build -t kafka_producer .
```

## Run

- Para inscribir a un nuevo usuario ejecutar con 

```console
docker run -it --network 1kafkabrokers_default kafka_producer
```
## Verificar ip del broker
	
	- Para inscripciones utilizamos el broker kafka1
```console
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' kafka1
```
	- Para Stock utilizamos el broker kafka2
```console
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' kafka2
```
	- Para contabilidad utilizamos el broker kafka3
```console
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' kafka3
```
