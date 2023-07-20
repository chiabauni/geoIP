# Geolocalización de IPs

## Para correr localmente
1. Clonar el repositorio
2. Estando dentro de la carpeta del repositorio, correr los siguientes comandos:
```
cd back
python3 -m pip install -r requirements.txt
python3 -m uvicorn src.main:app --reload
```
3. En otra terminal, correr los siguientes comandos:
```
cd front 
npm install
npm start
```
4. Abrir el navegador en la dirección http://localhost:3000/

## Para correr los tests
1. Clonar el repositorio
2. Estando dentro de la carpeta del repositorio, correr los siguientes comandos:
```
cd back
python3 -m pytest ./tests
```

## Para correr con Docker
1. Clonar el repositorio
2. Estando dentro de la carpeta del repositorio, correr los siguientes comandos:
```
docker-compose build
docker-compose up
```
3. Abrir el navegador en la dirección http://localhost:3000/
