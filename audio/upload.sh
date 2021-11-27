tempDir="/home/pi/temp/"
failDir="/home/pi/fail/"

while true
do
if [ "$(ls -A $tempDir*.mp3)" ] # Revisa si hay mp3s en el directorio
then
        for f in $tempDir*.mp3
        do
            ready=""
            ready=$(fuser -f $f) # Revisa si el archivo está siendo grabado

            if [  -z "$ready" ]
            then
                if [[ $(find $f -type f -size +0c 2>/dev/null) ]] # Revisa que el peso no sea cero
                then
                    echo Uploading $f
                    sshpass -p <password> sftp -o ConnectTimeout=10 <usuario>@<ip>:/triptico/tripticoEdge/RPiREC <<< $"put '$f'" && rm $f
                else
                    echo $f está corrupto
                    mv $f $failDir
                fi
            else
                echo $f esta siendo grabado
            fi
        done
fi
        sleep 25 
done
