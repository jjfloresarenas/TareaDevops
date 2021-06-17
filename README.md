
# Tarea Postulación Desarrollador DevOps. Jr.
[![Bors enabled](https://bors.tech/images/badge_small.svg)](https://app.bors.tech/repositories/34601)

## Instrucciones iniciales para correr el proyecto

### Instalaciones necesarias

[Docker](https://docs.docker.com/engine/install/)  
[Docker-compose](https://docs.docker.com/compose/install/)

### Clonar proyecto

````
git clone https://github.com/jjfloresarenas/TareaDevops && cd TareaDevops

````
Una vez tengamos listo lo anterior ejecutamos en la carpeta raíz, el siguiente comando

```
docker-compose build

```

Docker iniciará la construcción de la imagen, esperamos a que termine

Y levantamos el proyecto con el siguiente comando


````
docker-compose up

````

Puedes chequear en el navegador ingresando al siguiente link [http://localhost:3005](http://localhost:3005)

Además podemos correr el proyecto en segundo plano con

````
docker-compose start

````

Y lo detenemos con el siguiente comando

````
docker-compose stop

````

Todos los comandos relacionados a docker-compose, deben realizarse posicionado en el directorio RAÍZ del Proyecto

