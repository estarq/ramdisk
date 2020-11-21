import os

if os.popen('command -v apt').read():
    os.system('apt update')
    os.system('apt install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0 adwaita-icon-theme')
elif os.popen('command -v pacman').read():
    os.system('pacman -Sy')
    os.system('pacman -S --noconfirm python3-gi python3-gi-cairo gir1.2-gtk-3.0 adwaita-icon-theme')
elif os.popen('command -v eopkg').read():
    os.system('eopkg update-repo')
    os.system('eopkg install -y python3-gi')
    os.system('eopkg install -y python3-gi-cairo')
    os.system('eopkg install -y gir1.2-gtk-3.0')
    os.system('eopkg install -y adwaita-icon-theme')
elif os.popen('command -v zypper').read():
    os.system('zypper refresh')
    os.system('zypper install -n python3-gi python3-gi-cairo gir1.2-gtk-3.0 adwaita-icon-theme')

os.system('mv data/ramdisk /usr/bin/ramdisk')
os.system('chown root:root /usr/bin/ramdisk')
os.system('chmod 755 /usr/bin/ramdisk')

os.system('mv data/ramdisk.desktop /usr/share/applications/ramdisk.desktop')

os.system('mv data/ramdisk.png /usr/share/pixmaps/ramdisk.png')

os.system('mv data/ramdisk.policy /usr/share/polkit-1/actions/ramdisk.policy')

os.system('mkdir /usr/share/ramdisk/')
os.system('mv data/data.json /usr/share/ramdisk/data.json')

os.system('rm -rf data')
