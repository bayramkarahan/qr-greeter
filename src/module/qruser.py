import json
def qr_json_action(data):
    print(data,file=sys.stderr)


def create_user(username,password):
    os.system("""
        user='{0}'
        pass='{1}'
        if ! grep "^$user-qr:" /etc/passwd >/dev/null; then
            useradd -m $user -s /bin/bash -p $(openssl passwd "$user") -U -d /home/$user
            useradd $user-qr -s /bin/bash -p $(openssl passwd "$user") -d /home/$user
            mkdir -p /home/$user
            chown $user -R /home/$user
            chmod 755 /home/$user
            uida=$(grep "^$user:" /etc/passwd | cut -f 3 -d ":")
            uidb=$(grep "^$user-qr:" /etc/passwd | cut -f 3 -d ":")
            sed -i "s/:$uidb:/:$uida:/g" /etc/passwd
            for g in ogretmen floppy audio video plugdev netdev lpadmin scanner $user
            do
                usermod -aG $g $user-qr || true
                usermod -aG $g $user || true
            done
        fi
        usermod $user-qr -p $(openssl passwd "$pass")
   """.format(username,password))

def module_init():
    loginwindow.qr.write = qr_json_action