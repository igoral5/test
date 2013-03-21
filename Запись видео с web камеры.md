## Захват видео 

### Запись видео с web камеры без звука

mencoder tv:// -fps 30 -tv driver=v4l2:width=640:height=480:device=/dev/video0 -ovc lavc -lavcopts vcodec=mjpeg -nosound -o test.avi

| Параметр                                           | Описание                                                                      |
|:---------------------------------------------------|:------------------------------------------------------------------------------|
|tv://                                               | Указывает на необходимость захвата видео                                      |
|-fps 30                                             | Частота кадров 30 кадров в секунду                                            |
|-tv&nbsp;driver=v4l2:width=640:height=480:device=/dev/video0| Субопции уточняющие режим захвата видео                                    |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;driver=v4l2     | Драйвер видео захвата Video for Linux v.2                                     |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;width=640       | Ширина видео 640                                                              |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;height=480      | Высота видео 480                                                              |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;device=/dev/video0| Устройство видео захвата /dev/video0                                        |
|-ovc lavc                                           | Кодировать libavcodec кодеком                                                 |
|-lavcopts vcodec=mjpeg                              | Субопции libavcodec кодека                                                    |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vcodec=mjpeg    | Кодировать выходной файл алгоритмом Motion JPEG                               |
|-nosound                                            | Без звука                                                                     |
|-o test.avi                                         | Выходной файл test.avi                                                        |

### Запись видео с web камеры со звуком

mencoder tv:// -fps 30 -tv driver=v4l2:width=640:height=480:device=/dev/video0:alsa:forceaudio:amode=0:adevice=hw.1,0 -ovc lavc -lavcopts vcodec=mpeg4 -oac mp3lame -lameopts vbr=3:br=32:mode=3 -af volnorm -o test.avi

| Параметр                                           | Описание                                                                      |
|:---------------------------------------------------|:------------------------------------------------------------------------------|
|tv://                                               | Указывает на необходимость захвата видео                                      |
|-fps 30                                             | Частота кадров 30 кадров в секунду                                            |
|-tv&nbsp;driver=v4l2:width=640:height=480:<br>device=/dev/video0:alsa:forceaudio:amode=0:adevice=hw.1,0| Субопции уточняющие режим захвата видео |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;driver=v4l2     | Драйвер видео захвата Video for Linux v.2                                     |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;width=640       | Ширина видео 640                                                              |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;height=480      | Высота видео 480                                                              |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;device=/dev/video0| Устройство видео захвата /dev/video0                                        |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alsa            | Захват звука через ALSA                                                       |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forceaudio      | Указывает захватывать звук даже если v4l сообщает, что нет источников звука   |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;amode=0         | Аудио режим: моно<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0: моно<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1: стерео<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2: язык 1<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3: язык 2 |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;adevice=hw.1,0  | Устанавливает аудио устройство. \<значение\> должно быть /dev/xxx для OSS и аппаратный ID для ALSA. Вы должны заменить любые ':' на '.' в ID для ALSA. |
|-ovc lavc                                           | Кодировать видео libavcodec кодеком                                           |
|-lavcopts vcodec=mpeg4                              | Субопции libavcodec кодека                                                    |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vcodec=mpeg4    | Кодировать выходной файл алгоритмом MPEG-4 (DivX 4/5)                         |
|-oac mp3lame                                        | Кодироват звук mp3lame cbr/abr/vbr MP3 using libmp3lame                       |
|-lameopts vbr=3:br=32:mode=3                        | Субопции mp3lame кодека                                                       |  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vbr=3           | Метод переменного битпотока abr<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0: cbr<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1: mt<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2: rh (по умолчанию)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3: abr<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4: mtrh |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;br=32           | Битпоток звука 32 кбит/с                                                      |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode=3          | Режим звука моно<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0: стерео<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1: joint-стерео<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2: двухканальный<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3: моно |
|-af volnorm                                         | Выполнить нормализацию уровня звука                                           |
|-o test.avi                                         | Выходной файл test.avi                                                        |
  
### Вывести видео с web камеры на экран без звука

mplayer tv:// -tv driver=v4l2:width=640:height=480:device=/dev/video0 -nosound

| Параметр                                           | Описание                                                                      |
|:---------------------------------------------------|:------------------------------------------------------------------------------|
|tv://                                               | Указывает на необходимость захвата видео                                      |
|-tv driver=v4l2:width=640:height=480:device=/dev/video0| Субопции уточняющие режим захвата видео                                    |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;driver=v4l2     | Драйвер видео захвата Video for Linux v.2                                     |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;width=640       | Ширина видео 640                                                              |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;height=480      | Высота видео 480                                                              |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;device=/dev/video0| Устройство видео захвата /dev/video0                                        |
|-nosound                                            | Без звука                                                                     |
