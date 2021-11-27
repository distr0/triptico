## Scripts para captura de imagen

### Configuración
* Los archivos deben ser copiados al directorio home del usuario pi (/home/pi/).
* Modificar archivo upload.sh incluyendo nombre de usuario, ip y password del servidor sftp
* Ejecutar setup.sh con sudo para crear los directorios necesarios e instalar servicios y paquetes
```
sudo setup.sh
```
* Iniciar servicios o reiniciar raspberry para comenzar
```
sudo systemctl start apagado.service upload.service rec.service
```

### Explicación del funcionamiento
1- foto.service ejecuta y mantiene foto.sh quien captura imagenes en fotos/
2- fupload.service ejecuta y mantiene fupload.sh quien revisa fotos/ y sube al servidor sftp
3- apagado.service ejecuta y mantiene apagado.py quien escucha el puerto GPIO 16. Cuando este es activado apaga el equipo