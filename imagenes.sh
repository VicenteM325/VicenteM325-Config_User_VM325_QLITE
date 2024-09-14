directorio=~/Imagenes

# Función para obtener la resolución de cada monitor
function resoluciones() {
    xrandr | grep ' connected' | while read -r line; do
        # Extrae el nombre del monitor (e.g., HDMI-0)
        monitor=$(echo $line | cut -d ' ' -f 1)
        # Extrae la resolución actual del monitor (e.g., 1920x1080)
        res=$(echo $line | grep -o '[0-9]\+x[0-9]\+')
        echo "$monitor $res"
    done
}

# Función para seleccionar una imagen aleatoria
function rand_imagen(){
    imagen=$(ls -1 -b -R "$directorio" | grep -i -e ".png" -e ".jpg" -e ".jpeg" | sort --random-sort | head -1)
    dir_imagen=$(find "$directorio" -iname "$imagen")
}

# Función para aplicar el fondo de pantalla a cada monitor
function escalar(){
    resoluciones | while read -r monitor res; do
        ancho_monitor=$(echo $res | cut -d 'x' -f 1)
        alto_monitor=$(echo $res | cut -d 'x' -f 2)
        
        rand_imagen
        
        imagen_ancho=$(identify -format "%w" "$dir_imagen")
        imagen_alto=$(identify -format "%h" "$dir_imagen")
        
        proporcion_ancho=$(echo "$imagen_ancho / $ancho_monitor" | bc -l)
        proporcion_alto=$(echo "$imagen_alto / $alto_monitor" | bc -l)
        
        if [ $(echo "$proporcion_ancho > 1" | bc) -eq 1 ] || [ $(echo "$proporcion_alto > 1" | bc) -eq 1 ]; then
            nitrogen --head=$(xrandr --listmonitors | grep -w "$monitor" | cut -d':' -f1 | xargs) --set-zoom-fill "$dir_imagen"
        else
            nitrogen --head=$(xrandr --listmonitors | grep -w "$monitor" | cut -d':' -f1 | xargs) --set-centered "$dir_imagen"
        fi
    done
}

escalar
exit
