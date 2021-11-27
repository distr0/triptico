export AUDIODEV=hw:1,0 # Tarjeta de sonido
rec_folder=/home/pi/temp
test=true
while $test # Espera a que la tarjeta de sonido esté presente
do
        ls /dev/hidraw0
        if [ $? -eq 0 ]
        then
                echo si esta
                test=false # Sale del loop
        else
                echo nonada
                ts=$(date "+%Y-%m-%y %H:%M:%S")
                echo $ts >> /home/pi/fail.record # Guarda timestamp del fallo

        fi
        sleep 5
done
while true
do
	fname=$(($(date +%s%N)/1000000))".mp3" 
	rec $rec_folder"/"$fname trim 0 30 # guarda mp3s de 30 segundos
done