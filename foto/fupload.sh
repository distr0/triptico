tempDir="/home/pi/fotos/"

while true
do
if [ "$(ls -A $tempDir*.jpg)" ]
then
        for f in $tempDir*.jpg
        do
            ready=""
            ready=$(fuser -f $f) # Revisa si el archivo está siendo grabado

            if [  -z "$ready" ]
            then
                echo Uploading $f
		sshpass -p <password> sftp -o ConnectTimeout=10 <user>@<ip>:/triptico/tripticoEdge/RPiFotos <<< $"put '$f'" && rm $f
	else
                echo $f esta siendo grabado
            fi
        done
fi
        sleep 5
done
