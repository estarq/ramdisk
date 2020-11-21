# RAMDisk

![ramdisk](https://github.com/estarq/ramdisk/blob/main/ramdisk.png)

With RAMDisk you can use your RAM as a folder, maximizing speed and disk longevity.<br>
Ramdisks are shared with all users and use a minimal amount of RAM needed to store your files.<br>
In rare cases, when RAM is scarce, RAMDisk will utilize the swap partition to store new files.<br>
All files disappear at shutdown!<br>

# How to install

To install run

```
git clone https://github.com/estarq/ramdisk
cd ramdisk
sudo python3 install.py
```

Tested on:<br>
antiX, ArcoLinux, Elementary, EndeavourOS, Gecko, Kali, KDE neon, Kubuntu, Linuxfx, Lite, Lubuntu, LXLE, Mageia, Manjaro, Mint, MX Linux, OpenMandriva, openSUSE, Parrot, Peppermint, Pop!_OS, Q4OS, Solus, SparkyLinux, Tails, Trisquel, Ubuntu, Ubuntu Budgie, Ubuntu Kylin, Ubuntu MATE, Ubuntu Studio, Xubuntu, Zorin<br>

antiX - use terminal to run RAMDisk<br><br>
Doesn't work on:<br>
Debian, Devuan, Fedora, KaOS, PCLinuxOS, PureOS

# How to remove

To remove run
```
sudo python3 remove.py
```

# Details

Privileges required: yes (Polkit/PolicyKit + pkexec)<br>
Ramdisk's path: /mnt/name<br>
Ramdisk's access rights: rwxrwxrwx (777)<br>
Ramdisk's filesystem: tmpfs<br>
Automount: yes (/etc/fstab)<br>

Ramdisk's `size` limits it's total (RAM + swap) capacity. 

# Dependencies

python3, python3-gi, python3-gi-cairo, gir1.2-gtk-3.0, adwaita-icon-theme

(no need for manual installation)
