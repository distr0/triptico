if [ "$(id -u)" -ne 0 ]; then
        echo 'Este script se debe ejecutar con sudo' >&2
        exit 1
fi

sudo apt update
sudo apt install sshpass

folders=("/home/$SUDO_USER/triptico/tripticoEdge" "/var/sftp/triptico/")
for f in "${folders[@]}"
do
    sudo -u $SUDO_USER mkdir -p $f
done