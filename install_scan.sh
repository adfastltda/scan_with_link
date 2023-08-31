#!/bin/bash
apt update -y > /dev/null
apt upgrade -y > /dev/null
pkg install python -y > /dev/null
pip install requests > /dev/null
pkg install git > /dev/null

# Clonar o repositório do GitHub
git clone https://github.com/adfastltda/scan_with_link.git

# Navegar para o diretório do repositório
cd scan_with_link

# Executar o script scan.py
python scan.py
