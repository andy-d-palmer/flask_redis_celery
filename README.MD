# RabbitMQ Redis Celery
This repo produces a bare-bones celery cluster with
 * rabbitmq as the broker
 * redis as the results backend
 * two celery workers consuming from one queue
 
docker-compose is used to launch the whole stack