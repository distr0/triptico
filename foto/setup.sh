if [ "$(id -u)" -ne 0 ]; then
        echo 'Este script se debe ejecutar con sudo o como root' >&2
        exit 1
fi

apt update
apt install sshpass

folders=("fotos")
for f in "${folders[@]}"
do
    sudo -u $SUDO_USER mkdir -p $f
done

sudo cp foto.service fupload.service apagado.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable foto.service fupload.service apagado.service