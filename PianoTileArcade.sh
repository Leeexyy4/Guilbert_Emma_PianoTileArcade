#!/bin/bash

# Cree le virtualenv
if [ ! -d ".venv" ]; then
    echo "🔧 Creation de l'environnement virtuel..."
    python3.12 -m venv .venv || { echo "❌ echec du venv"; exit 1; }
fi

# Active le virtualenv
source .venv/bin/activate || { echo "❌ Impossible d'activer le venv"; exit 1; }

# Installe pygame avec --break-system-packages
pip install pygame --break-system-packages || { echo "❌ Installation de pygame echouee"; exit 1; }

# Verifie que pygame est bien installe
pip show pygame > /dev/null 2>&1 || pip install pygame --break-system-packages

# Lance ton script avec le bon interpreteur
python Game.py
