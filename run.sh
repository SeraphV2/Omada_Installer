#!/bin/bash

sudo apt update && sudo apt upgrade -y

echo "Updated sucessfully! Running Omada Controller Installer....."

python3 omada_installer.py
