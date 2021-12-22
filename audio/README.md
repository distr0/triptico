## Scripts para grabación de audio

### Configuración
* Los archivos deben ser copiados al directorio home del usuario pi (/home/pi/).
* Modificar archivo upload.sh incluyendo nombre de usuario, ip y password del servidor sftp
* Ejecutar setup.sh con sudo para crear los directorios necesarios e instalar servicios
```
sudo setup.sh
```
* Iniciar servicios o reiniciar raspberry para comenzar
```
sudo systemctl start apagado.service upload.service rec.service
```

### Explicación del funcionamiento
* rec.service ejecuta y mantiene sox_rec.sh quien graba audio en temp/
* upload.service ejecuta y mantiene upload.sh quien revisa temp/ y sube con upload.sh. Si falla mueve los archivos a fail/
* apagado.service ejecuta y mantiene apagado.py quien escucha el puerto GPIO 16. Cuando este es activado apaga el equipo