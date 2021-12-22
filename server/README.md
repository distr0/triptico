## Scripts para servidor intermedio

### Configuración
* Los archivos deben ser copiados al directorio home/triptico del usuario (/home/<user>/triptico).
* Ejecutar setup.sh con sudo para crear los directorios necesarios e instalar dependencias.
* Configurar el cron de root para ejecutar los scripts:

```
*/5 * * * * /usr/bin/python3.7 /home/<user>/triptico/preupload.py && chown <user>:<user> /home/<user>/triptico/log.csv ```
```
### Funcionamiento
* Cron ejecuta preupload.py quien revisa cambios en los archivos subidos por los equipos remotos en /var/sftp/triptico/
* Si los archivos no tienen cambios, los mueve a las carpetas correpondientes en /home/<user>/triptico/tripticoEdge/ 
* preupload.py ejecuta upload.sh quien sube las carpetas completas al servidor web por sftp
* preupload.py escribe el log en /home/<user>/triptico/log.csv