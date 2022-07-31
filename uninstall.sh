#!/bin/sh 

echo -e "\nDesinstalando requisitos.."
pip uninstall -r ./requirements.txt -q 

echo "Desinstalando virtualenv..."
pip uninstall -q virtualenv

echo -e "\Eliminando el directorio..."
rm -rf entorno

echo -e "\nSe acabó la desinstalación"
