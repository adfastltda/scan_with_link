#!/bin/bash
pkg install python -y
pip install requests
pkg install git

# Clonar o repositório do GitHub
git clone https://github.com/adfastltda/scan_with_link.git

# Navegar para o diretório do repositório
cd scan_with_link

# Executar o script scan.py
python scan.py
