if [ "$(id -u)" -ne 0 ]; then
        echo 'Este script se debe ejecutar con sudo o como root' >&2
        exit 1
fi

sudo apt update
sudo apt install sox sshpass

folders=("temp" "fail")
for f in "${folders[@]}"
do
    sudo -u $SUDO_USER mkdir -p $f
done

sudo cp rec.service upload.service apagado.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable rec.service upload.service apagado.service