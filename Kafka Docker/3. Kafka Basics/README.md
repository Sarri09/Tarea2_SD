# Docker
  - Crear Topics
```
    docker exec -it kafkaX kafka-topics.sh --create --bootstrap-server localhost:9092 --topic nombre-del-tema --partitions 3 --replication-factor 3
```
Lo esto proporcionará para cada clouster (kafkaX) un topico. 
