import os
import subprocess

def cambiar_nombre_usb(nuevo_nombre):
    try:
        # Listar los dispositivos montados en /media/unl/
        dispositivos_usb = [os.path.join("/media/unl", nombre) for nombre in os.listdir("/media/unl")]

        # Cambiar el nombre de cada dispositivo USB
        for dispositivo in dispositivos_usb:
            # Desmontar el dispositivo
            subprocess.run(["sudo", "e2label", "-i", dispositivo, "-s ::"], check=True)
            
            # Cambiar el nombre de la etiqueta del sistema de archivos
            subprocess.run(["sudo", "e2label", "-i", nombre, nuevo_nombre], check=True)
            print(f"Nombre del dispositivo {dispositivo} cambiado a {nuevo_nombre}.")
            
            # Volver a montar el dispositivo
            subprocess.run(["sudo", "udisksctl", "mount", "--block-device", dispositivo], check=True)
    except subprocess.CalledProcessError as e:
        print("Error al cambiar el nombre del USB:", e)

# Nuevo nombre para los dispositivos USB
nuevo_nombre_usb = "UNL-device"

# Cambiar el nombre de todos los dispositivos USB disponibles en /media/unl/
cambiar_nombre_usb(nuevo_nombre_usb)
