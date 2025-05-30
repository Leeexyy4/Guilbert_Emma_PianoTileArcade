#!/bin/bash

# Crée le virtualenv
if [ ! -d ".venv" ]; then
    echo "🔧 Création de l'environnement virtuel..."
    python3.12 -m venv .venv || { echo "❌ Échec du venv"; exit 1; }
fi

# Active le virtualenv
source .venv/bin/activate || { echo "❌ Impossible d'activer le venv"; exit 1; }

# Installe pygame avec --break-system-packages
pip install pygame --break-system-packages || { echo "❌ Installation de pygame échouée"; exit 1; }

# Vérifie que pygame est bien installé
pip show pygame > /dev/null 2>&1 || pip install pygame --break-system-packages

# Lance ton script avec le bon interpréteur
python Game.py
