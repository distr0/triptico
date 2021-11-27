if [ "$(id -u)" -ne 0 ]; then
        echo 'Este script se debe ejecutar con sudo o como root' >&2
        exit 1
fi

apt update
apt install sshpass

folders=("upload" "ramdisk" "reUpload/RPiIMU")
for f in "${folders[@]}"
do
    sudo -u $SUDO_USER mkdir -p $f
done

echo "tmpfs       /home/$SUDO_USER/ramdisk tmpfs nodev,nosuid,noexec,nodiratime,size=10m">>/etc/fstab
mount -a

cp sftp.service imu.service apagado.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable sftp.service imu.service apagado.service