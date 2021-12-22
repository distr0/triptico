## Scripts para uso de IMU(s) MPU6050

### Configuración
* Los archivos deben ser copiados al directorio home del usuario pi (/home/pi/).
* Modificar archivos sftp.sh y rftp.sh incluyendo nombre de usuario, ip y password del servidor sftp
* [OPCIONAL] Modificar archivo imu.py para agregar más de un IMU si fuese necesario (en "Device_Address")
* Ejecutar setup.sh con sudo para crear los directorios necesarios, instalar servicios y configurar el disco ram.
```
sudo setup.sh
```
* Configurar crontab para que ejecute shtp.sh cada un minuto
```
* * * * * /usr/bin/bash /home/pi/sftp.sh
```
* Iniciar servicios o reiniciar raspberry para comenzar
```
sudo systemctl start apagado.service imu.service sftp.service
```

### Explicación del funcionamiento
* imu.service ejecuta y mantiene imu.py quien registra los datos del IMU(s) en ramdisk/ inicialmente y luego en upload/
* sftp.service ejecuta y mantiene sftp.py quien revisa upload/ y sube con sftp.sh. Si falla mueve los archivos a reUpload/RPiIMU/
* Cron ejecuta rftp.sh cada un minuto para subir lo que exista en reUpload/RPiIMU/ 
* apagado.service ejecuta y mantiene apagado.py quien escucha el puerto GPIO 16. Cuando este es activado apaga el equipo