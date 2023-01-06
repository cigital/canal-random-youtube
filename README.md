<!-- Add banner here -->
![Banner](https://github.com/cigital/canal-random-youtube/blob/main/banner.png)

# Canal random de Youtube
![Github](https://img.shields.io/github/last-commit/cigital/canal-random-youtube)
![Github](https://img.shields.io/github/license/cigital/canal-random-youtube)

Este script sirve para obtener un canal "random" de youtube mediante peticiones por la API de Youtube y usando el modulo random de python.

!! ADVERTENCIA, este script solo esta probado en arch linux !!

## Instalación
Clona el repositorio
```bash
git clone https://github.com/cigital/canal-random-youtube/
```
Dale permisios de ejecución al archivo de instalación y desinstalación

```bash
chmod +x ./install.sh ./uninstall.sh
```

Ejecuta el archivo de instalación

```bash
./install.sh
```

## Desinstalación
Para desinstalar simplemente ejecuta el archivo de desinstalación
```bash
./uninstall.sh
```

## Como usar
Entra en el entorno

```bash
source entorno/bin/activate
```

Con python ejecuta el archivo canal_random.py
```python
python3 canal_random.py
```
Y cuando te pregunte, pega tu credencial de api.
