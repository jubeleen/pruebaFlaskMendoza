# pruebaFlaskMendoza

## Entorno virtual

crear entorno virtual:

```
python -m venv .venv
```

activar el entorno virtual:

```
source .venv/bin/activate
```

para instalar las dependencias:
```
pip install flask
```

## Para corrrer el programa

Solo la maquina local :

```
flask run
```

Desde cualquier maquina de la red :

```
flask run -h 0.0.0.0
```

## para correr el debuger

```
flask run --debug
```