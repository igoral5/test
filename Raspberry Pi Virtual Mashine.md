## Установка Raspbian “wheezy” в виртуальную машину QEMU

### Дано:

Host машина Gentoo x86_64

### Необходимо: 

Установить Raspbian “wheezy” в виртуальную машину QEMU c доступом к сети в режиме моста. 

### Подготовка Host машины

1. Необходимо, что бы ядро Host машины поддерживало bridging и Ethernet tap сетевые адаптеры. Проверить можно
следующими командами:

<pre>alimovl ~ # modprobe bridge
alimovl ~ # modprobe tun</pre>

если модули загружаются без ошибок - поддержка в ядре реализована. В противном случае, конфигурим и собираем новое ядро.

`alimovl ~ #  genkernel --menuconfig all`

Networking support->Networking options-> <M> 802.1d Ethernet Bridging<br>
Device Drivers->Network device support->Network core driver support-><M> Universal TUN/TAP device driver support<br>

2. Установим утилиты для управления мостом:

`alimovl ~ # emerge -av net-misc/bridge-utils`

3. Настройка конфигурации моста, файл /etc/conf.d/net:

<pre>dns_domain_lo="ваш домен" # замените своим именем домена
config_eth0="null"
bridge_br0="eth0"
config_br0="dhcp"</pre>

Если вы используете статический IP - адрес, настройте br0 соотвествующим образом.

<pre>alimovl ~ # cd /etc/init.d/
alimovl init.d # ln -s net.lo net.br0
alimovl init.d # rc-update add net.br0 default</pre>

После применения изменений (перегрузки) должны получить следующую картину:

<pre>alimovl ~ # ifconfig
br0: flags=4419<UP,BROADCAST,RUNNING,PROMISC,MULTICAST>  mtu 1500
        inet 192.168.181.113  netmask 255.255.255.0  broadcast 192.168.181.255
        inet6 fe80::3ed9:2bff:fe58:e439  prefixlen 64  scopeid 0x20<link>
        ether 3c:d9:2b:58:e4:39  txqueuelen 0  (Ethernet)
        RX packets 736440  bytes 1349247947 (1.2 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 299235  bytes 34894278 (33.2 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::3ed9:2bff:fe58:e439  prefixlen 64  scopeid 0x20<link>
        ether 3c:d9:2b:58:e4:39  txqueuelen 1000  (Ethernet)
        RX packets 1369006  bytes 1403154738 (1.3 GiB)
        RX errors 0  dropped 1323  overruns 0  frame 0
        TX packets 336248  bytes 38387346 (36.6 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 20  memory 0xfe400000-fe420000  

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 0  (Local Loopback)
        RX packets 92109  bytes 17156404 (16.3 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 92109  bytes 17156404 (16.3 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

alimovl ~ # brctl show
bridge name     bridge id               STP enabled     interfaces
br0             8000.3cd92b58e439       no              eth0</pre>

При этом связь Host машины с внешним миром и Internet должна нормально функционировать.

4. Установим kpartx:

`alimovl ~ # emerge -av sys-fs/multipath-tools`

### Установка QEMU

От QEMU нам потребуется поддержка ARM платформы, поэтому в файл /etc/portage/package.use добавим строку:

`app-emulation/qemu qemu_softmmu_targets_arm -qemu_softmmu_targets_x86_64`

опция qemu_softmmu_targets_arm добавляет поддержку ARM платформы, -qemu_softmmu_targets_x86_64 выключает эмуляцию 
платформы x86_64 (если она вам нужна, удалите ее)

Сборка и установка QEMU:

`alimovl ~ # emerge -av app-emulation/qemu`

В процессе запуска виртальной машины необходимы административные привилегии для создания сетевого интерфейса и включения его в мост.
Для того что бы иметь возможность запускать виртуальную машину из под обычного пользователя выполним:

`alimovl ~ # chmod u+s /usr/libexec/qemu-bridge-helper`

### Получение ядра

При запуске виртульной машины используется модифицированние ядро, берем его с http://xecdesign.com/downloads/linux-qemu/kernel-qemu

### Получение образа диска Raspbian “wheezy”

Берем файл 2013-02-09-wheezy-raspbian.zip с http://www.raspberrypi.org/downloads

### Подготовка образа диска

Пусть образ лежит в /home/igor/qemu/Raspberry, туда же положим ядро kernel-qemu.
Распакуем образ диска:

<pre>igor@alimovl ~/qemu/Raspberry $ unzip 2013-02-09-wheezy-raspbian.zip
Archive:  2013-02-09-wheezy-raspbian.zip
  inflating: 2013-02-09-wheezy-raspbian.img</pre>

Образ диска имеет два раздела и что бы смонтировать его предварительно сделаем маппинг:

<pre>igor@alimovl ~/qemu/Raspberry $ sudo kpartx -av 2013-02-09-wheezy-raspbian.img
add map loop0p1 (253:0): 0 114688 linear /dev/loop0 8192
add map loop0p2 (253:1): 0 3665920 linear /dev/loop0 122880</pre>

Создаем каталоги для монтирования:

<pre>igor@alimovl ~/qemu/Raspberry $ sudo mkdir /mnt/raspberry
igor@alimovl ~/qemu/Raspberry $ sudo mkdir /mnt/raspberry/disk1
igor@alimovl ~/qemu/Raspberry $ sudo mkdir /mnt/raspberry/disk2</pre>

Монтируем диски:

<pre>igor@alimovl ~/qemu/Raspberry $ sudo mount /dev/mapper/loop0p1 /mnt/raspberry/disk1
igor@alimovl ~/qemu/Raspberry $ sudo mount /dev/mapper/loop0p2 /mnt/raspberry/disk2</pre>

В Raspberry Pi качестве диска используется SD карточка, которая видна в системе /dev/mmcblk0 и /dev/mmcblk0p1, /dev/mmcblk0p2 ее разделы.
Некорые программы обращаются к этим устройствам, для того что бы не возникало ошибок создадим файл /mnt/raspberry/disk2/etc/udev/rules.d/90-qemu.rules
следующего содержания:

<pre>KERNEL=="sda", SYMLINK+="mmcblk0"
KERNEL=="sda?", SYMLINK+="mmcblk0p%n"</pre>

Это обеспечит автоматическое создание символьных ссылок на устройство /dev/sda и его разделы

Закомментируем содержимое файла /mnt/raspberry/disk2/etc/ld.so.preload:

\# /usr/lib/arm-linux-gnueabihf/libcofi_rpi.so

Для большего разрешения экрана при запуске X window создадим файл /mnt/raspberry/disk2/etc/X11/xorg.conf следующего содержания:

<pre>Section "Screen"
Identifier "Default Screen"
SubSection "Display"
Depth 16
Modes "800x600" "640x480"
EndSubSection
EndSection</pre>

Размонтируем диски и отменим мапирование диска:

<pre>igor@alimovl ~/qemu/Raspberry $ sudo umount /dev/mapper/loop0p1
igor@alimovl ~/qemu/Raspberry $ sudo umount /dev/mapper/loop0p2
igor@alimovl ~/qemu/Raspberry $ sudo kpartx -d 2013-02-09-wheezy-raspbian.img
loop deleted : /dev/loop0</pre>

На полученном образе диска мало свободного места и рекомендуется его расширить:

<pre>igor@alimovl ~/qemu/Raspberry $ qemu-img resize 2013-02-09-wheezy-raspbian.img +2G
Image resized.</pre>

Эта команда увеличивает размер образа диска на 2 Gb.

### Запуск виртуальной машины

Запуск осуществляется командой:

`qemu-system-arm -kernel kernel-qemu -cpu arm1176 -m 256 -M versatilepb -no-reboot -net nic -net bridge -serial stdio -append "root=/dev/sda2 panic=1" -hda 2013-02-09-wheezy-raspbian.img`

При первом запуске были проблемы с монтированим диска (его удалось смонтировать только в режиме read-only), если это так, выполним команду:

`fsck.ext4 /dev/sda2`

На вопросы <Fix что-то>? отвечать y. После завершения проверки нажать Ctrl-D.

В процессе загрузки неизбежно будут возникать ошибки (мы запускаем систему с не родным ядром), но к счатью не критические.

### Первоначальная настройка виртуальной машины

Если загрузка будет успешной, мы автоматически попадаем в программу первоначальной настройки raspi-config (затем ее можно будет вызвать командой sudo raspi-config).

1. Раширяем корневой раздел: 

`expand_rootfs      Expand root partition to fill SD card`

2. Устанавливаем локали:

`change_locale      Set locale`

Снимаем выделение с локали en_GB.UTF-8 UTF-8 и выделяем локали en_US.UTF-8 UTF-8 и ru_RU.UTF-8 UTF-8. Локалью по умолчанию назначаем ru_RU.UTF-8 UTF-8.

3. Устанавливаем часовой пояс:

`change_timezone    Set timezone`

Выбираем Europe Moscow (или необходимый вам часовой пояс)

4. Настраиваем ввод и вывод консоли:

`configure_keyboard Set keyboard layout`

<pre>Выбираем Generic 105-key (Intl) PC
Keyboard layout: Other
Country of origin for the keyboard: Russian
Keyboard layout: Russian
Method for toggling between national and Latin mode: Alt+Shift
Method for temporarily toggling between national and Latin input: No temporary switch
Key to function as AltGr: The default for the keyboard layout
Compose key: No compose key
Use Control+Alt+Backspace to terminate the X server? <Yes></pre>

5. Устанавливаем пароль пользователя pi:

`change_pass        Change password for 'pi' user`

Выходим из raspi-config с перезагрузкой

6. После перегрузки можно установить необходимые компоненты и выполнить обновление системы:

Если вы для доступа в Internet используете прокси сервер, создайте файл /etc/apt/apt.conf.d/90proxy:

`pi@raspberrypi ~ $ sudo nano /etc/apt/apt.conf.d/90proxy`

Следующего содержания:

`Acquire::http::Proxy "http://yourproxyaddress:proxyport";`

Выполняем команды:

<pre>sudo apt-get update
sudo apt-get install console-cyrillic mc gpm
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get autoremove
sudo apt-get clean</pre>

После выполения этих команд, мы установим кириллические консольные шрифты, Midnight Commander, мышь консольного режима и выполним обновление системы.

Теперь можно попробовать запустить Xwindow командой startx, кроме того можно подключится к нашей виртуальной машине по ssh.


Использованные материалы:

http://www.v13.gr/blog/?p=276<br>
http://xecdesign.com/qemu-emulating-raspberry-pi-the-easy-way/<br>
http://www.soslug.org/wiki/raspberry_pi_emulation<br>
https://help.ubuntu.com/community/AptGet/Howto<br>
http://ru.gentoo-wiki.com/wiki/%D0%9F%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_%D0%92%D0%9C_qemu_%D0%B2_%D0%BB%D0%BE%D0%BA%D0%B0%D0%BB%D1%8C%D0%BD%D1%83%D1%8E_%D1%81%D0%B5%D1%82%D1%8C<br>
http://en.gentoo-wiki.com/wiki/Bridging_Network_Interfaces<br>













