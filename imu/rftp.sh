reupload_dir="/home/pi/reUpload/RPiIMU"
if [ ! -z "$(ls -A $reupload_dir)" ]
then
	sshpass -p <password> sftp -r -o ConnectTimeout=10 <user>@<ip>:/triptico/tripticoEdge <<< $"put '$reupload_dir'" && rm $reupload_dir/*
fi
