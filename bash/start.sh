#!/bin/bash

###### EJECUTAR E-READER ############

#Asignar el modulo de audio
pacmd set-default-sink alsa_output.usb-Solid_State_System_Co._Ltd._USB_PnP_Audio_Device_000000000000-00.analog-stereo

#Contraseña de root
echo "UNL.2024" 
set timeout -1
spawn sudo su
expect "contraseña para *"
send "UNL.2024\r"
interact  

#Activación del entorno
echo "Activando entorno virtual Python 3.11"
source .venv/bin/activate

#Ejecución del Programa
echo "Ejecutando Programa"
python tk.py
