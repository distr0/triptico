while true
do
        ls /dev/video0
        if [ $? -eq 0 ] # Revisa si la cámara está conectada
        then
		ts=$(($(date +%s%N)/1000000))
		raspistill -w 1280 -h 800 -q 30 -o /home/pi/fotos/$ts.jpg 
		sleep 15
        else # cámara no conectada, escribe log
                echo nonada
                ts=$(date "+%Y-%m-%y %H:%M:%S")
                echo $ts >> /home/pi/fail.record
		sleep 2
        fi

done
