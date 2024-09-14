#!/bin/sh

# Ejecutar el script de multi monitor
sh ~/.screenlayout/multi_monitor.sh &

# Ejecutar el script de cambio de fondo de pantalla
sh ~/Imagenes/imagenes.sh &

# Ejecutar la app bluetooth blueman
blueman-applet &

# iconos del sistema y otros servicios
cbatticon &
udiskie -t &
nm-applet &

