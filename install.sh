#!/bin/sh 

echo "Instalando virtualenv..."
pip install -q virtualenv

echo -e "\nCreando el directorio..."
mkdir entorno

echo -e "\nCreando el entorno..."
python3 -m virtualenv entorno -q
source entorno/bin/activate 

echo -e "\nInstalando requisitos.."
pip install -r ./requirements.txt -q 

echo -e "\nSe acab la instalación"
