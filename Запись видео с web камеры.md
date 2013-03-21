## Запись видео с web камеры без звука

mencoder tv:// -fps 30 -tv driver=v4l2:width=640:height=480:device=/dev/video0 -ovc lavc -lavcopts vcodec=mjpeg -nosound -o test.avi

| Параметр                                           | Описание                                                                      |
|:---------------------------------------------------|:------------------------------------------------------------------------------|
|tv://                                             | Указывает на необходимость захвата видео                                      |
|-fps 30                                           | Частота кадров 30 кадров в секунду                                            |
|-tv driver=v4l2:width=640:height=480:device=/dev/video0| Субопции уточняющие режим захвата видео                                  |
|<pre>    driver=v4l2</pre>                                    | Драйвер видео захвата Video for Linux v.2                                     |
|<pre>    width=640</pre>                                      | Ширина видео 640                                                              |
|<pre>    height=480</pre>                                     | Высота видео 480                                                              |
|<pre>    device=/dev/video0</pre>                             | Устройство видео захвата /dev/video0                                          |
|-ovc lavc                                        | Кодировать libavcodec кодеком                                                 |
|-lavcopts vcodec=mjpeg                           | Субопции libavcodec кодека                                                    |
|<pre>    vcodec=mjpeg</pre>                                   | Кодировать выходной файл алгоритмом Motion JPEG                               |
|-nosound                                         | Без звука                                                                     |
|-o test.avi                                      | Выходной файл test.avi                                                        |

## Запись видео с web камеры со звуком

`mencoder tv:// -fps 30 -tv driver=v4l2:width=640:height=480:device=/dev/video0:alsa:forceaudio:amode=0:adevice=hw.1,0 -ovc lavc -lavcopts vcodec=mpeg4 -oac mp3lame -lameopts vbr=3:br=32:mode=3 -af volnorm -o test.avi`

  tv://													Указывает на необходимость захвата видео
  -fps 30												Частота кадров 30 кадров в секунду
  -tv driver=v4l2:width=640:height=480:device=/dev/video0:alsa:forceaudio:amode=0:adevice=hw.1,0	Субопции уточняющие режим захвата видео
	  driver=v4l2											Драйвер видео захвата Video for Linux v.2
	  width=640											Ширина видео 640
	  height=480											Высота видео 480
	  device=/dev/video0										Устройство видео захвата /dev/video0
	  alsa												Захват звука через ALSA
	  forceaudio											Указывает захватывать звук даже если v4l сообщает, что нет источников звука
	  amode=0											Аудио режим: моно
													    0: моно
													    1: стерео
													    2: язык 1
													    3: язык 2
	  adevice=hw.1,0										Устанавливает аудио устройство. <значение> должно быть /dev/xxx для OSS и аппаратный ID для ALSA. 
													Вы должны заменить любые ':' на '.' в ID для ALSA.
  -ovc lavc 												Кодировать видео libavcodec кодеком
  -lavcopts vcodec=mpeg4										Субопции libavcodec кодека
	  vcodec=mpeg4											Кодировать выходной файл алгоритмом MPEG-4 (DivX 4/5)
  -oac mp3lame												Кодироват звук mp3lame cbr/abr/vbr MP3 using libmp3lame
  -lameopts vbr=3:br=32:mode=3										Субопции mp3lame кодека
	  vbr=3												Метод переменного битпотока
													    0: cbr
													    1: mt
													    2: rh (по умолчанию)
													    3: abr
													    4: mtrh
	  br=32												Битпоток звука 32 кбит/с
	  mode=3											Режим звука
													    0: стерео
													    1: joint-стерео
													    2: двухканальный
													    3: моно
  -af volnorm												Выполнить нормализацию уровня звука
  -o test.avi												Выходной файл test.avi
  
## Вывести видео с web камеры на экран без звука

`mplayer tv:// -tv driver=v4l2:width=640:height=480:device=/dev/video0 -nosound`

  tv://													Указывает на необходимость захвата видео
  -tv driver=v4l2:width=640:height=480:device=/dev/video0						Субопции уточняющие режим захвата видео
	  driver=v4l2											Драйвер видео захвата Video for Linux v.2
	  width=640											Ширина видео 640
	  height=480											Высота видео 480
	  device=/dev/video0										Устройство видео захвата /dev/video0
  -nosound												Без звука



	  