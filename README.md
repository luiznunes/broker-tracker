# Setup steps
### Prepare environment file
1) Copy sample file and edit the fields
  - `cp .env.sample .env`
```
PG_HOST=
PG_PORT=
PG_DATABASE=
PG_USER=
PG_PASSWD=
MQTT_HOST=
MQTT_PORT=
```

2) Run all services with docker-compose
  - `docker-compose up -d`
