## Краткая шпаргалка по командам git
### Начальная настройка git
| Комманда                                                    |  Описание                                                              |
|:------------------------------------------------------------|:-----------------------------------------------------------------------|
|`git config --global user.name "John Doe"`                   | Установить глобально (для всех проектов данного пользователя) его имя  |
|`git config --global user.email johndoe@example.com`         | Установить глобально электронный адрес                                 |
|`git config --global core.editor kwrite`                     | Установить глобально редактор текста                                   |
|`git config --global merge.tool meld`                        | Установить глобально программу для разрешения конфликтов               |
|`git config --global color.ui true`                          | Установить глобально цветной вывод на терминал                         |
|`git config --list`                                          | Посмотреть используемые настройки                                      |
|`git config user.name`                                       | Посмотреть значение настройки, в данном случае имени пользователя      |


Настройки храняться в /etc/gitconfig (системные настройки для всех пользователей данной машины, ключ --system ) ~/.gitconfig (глобальные настройки
данного пользователя, ключ --global) .git/config (локальные настройки для данного репозитария). Настройки действуют подобно файлам css в порядке:
системные, глобальные, локальные


### Общие команды git
| Комманда                                                    |  Описание                                                              |
|:------------------------------------------------------------|:-----------------------------------------------------------------------|
|`git init`                                                   | Создание в текущем каталоге репозитория git                            |
|`git clone git@github.com:username/reponame.git`             | Клонировать существующий репозитарий с доступом по ssh                 |
|`git clone https://username@github.com/username/reponame.git`| Клонировать существующий репозитарий с доступом https                  |
|`git clone /opt/git/project.git my_repo`                     | Клонировать существующий локальный репозиторий и поместить его в папку my_repo. Примечание: для того что бы отправлять в такой репозитарий свои изменения, он должен быть голым (bare)|
|`git add readme.txt`                                         | Добавить в индекс файл readme.txt                                      |
|`git add .`                                                  | Добавить в индекс все изменные файлы текущего и вложенных каталогов (кроме файлов указанных в .gitignore) |
|`git rm readme.txt`                                          | Удалить readme.txt из отслеживаемых файлов и из рабочего каталога      |
|`git rm -f readme.txt`                                       | Позваляет удалить измененый и проиндексированный файл readme.txt       |
|`git rm --cached readme.txt`                                 | Удалить файл readme.txt из индекса, но оставить его в рабочем каталоге |
|`git mv file_from file_to`                                   | Переместить или переименовать файл                                     |
|`git commit`                                                 | Зафиксировать индекс (для формирования комментария будет вызван редактор указанны в core.editor) |
|`git commit -a -m 'first commit'`                            | Зафиксировать все изменения (-a) с указанным комметарием (-m)          |
|`git status`                                                 | Показать текущий статус репозитария                                    |
|`git diff`                                                   | Показать разность между проиндексированными и измененными файлами      |
|`git diff --stage`                                           | Показать разность между последним коммитом и индексированными файлами  |
|`git log`                                                    | Просмотр истории коммитов                                              |
|`git log -p -2`                                              | Вывести информацию о двух последних коммитах (-2), вместо списка измененных файлов вывести разницу |
|`git log --status`                                           | Вывести историю коммитов и сведения о количестве вставок, удаления и замен |
|`git log --pretty=oneline`                                   | Вывести историю коммитов в особом формате, в данном случае в одну строку |
|`git log --graph`                                            | Вывести историю коммитов и графическое отображение дерева веток (ascii графика) |
|`git log --since=2.weeks`                                    |	Выводит историю коммитов, сделанных за последнии 2 недели              |


Кроме того существует gitk, который в графическом виде показывает историю коммитов


### Отмена изменений
| Комманда                                                    |  Описание                                                              |
|:------------------------------------------------------------|:-----------------------------------------------------------------------|
|`git commit --amend`                                         | Сделать новую фиксацию, которая заменит предыдущий коммит              |
|`git reset HEAD readme.txt`                                  | Отменить индексацию файла                                              |
|`git checkout -- readme.txt`                                 | Отменить изменение файла                                               |

### Команды работы с удаленными репозитариями
| Комманда                                                    |  Описание                                                              |
|:------------------------------------------------------------|:-----------------------------------------------------------------------|
|`git remote`                                                 | Показать список удаленных репозитариев                                 |
|`git remote -v`                                              | Показать список удаленных репозитариев и их url'ы                      |
|`git remote show origin`                                     | Показать дополнительную информацию о удаленном репозитарии: url, текущий HEAD, настройки для git pull и git push |
|`git remote add origin git@github.com:username/reponame.git` | Добавить удаленный репозитарий под именем origin                       |
|`git remote rename <old> <new>`                              | Сменить имя (алиас) удаленного репозитария                             |
|`git remote remove <name>`                                   | Удалить связь с удаленным репозитарием                                 |
|`git fetch origin`                                           | Получить все ветки из удаленного репозитария, но ничего не сливая      |
|`git branch --set-upstream-to=origin/master master`          | Настроить удаленный репозиторий и ветку из которой будут браться изменения (origin/master) и локальную ветку куда эти изменения будут вливаться (master) для git pull |
|`git pull`                                                   | Взять изменения из удаленного репозитария и влить себе                 |
|`git push`                                                   | Отправить свои изменения в удаленный репозитарий                       |
|`git push origin master`                                     | Отправить свои изменения из ветки master в удаленный репозитарий origin |

### Работа а метками
| Комманда                                                    |  Описание                                                              |
|:------------------------------------------------------------|:-----------------------------------------------------------------------|
|`git tag`                                                    | Показать список меток                                                  |
|`git tag -l 'v.1.*'`                                         | Показать список меток совпадающих с шаблоном                           |
|`git tag -a v.1.4 -m 'my version 1.4'`                       | Создать аннотированную метку с описанием                               |
|`git tag -s v1.5 -m 'my signed 1.5 tag'`                     | Создать подписанную ключем аннотированную метку с описанием            |
|`git tag -a v1.2 -m 'version 1.2' 9fceb02`                   | Поставить метку на определенный коммит                                 |
|`git tag v1.4-lw`                                            | Создать легковесную метку                                              |
|`git show v1.4`                                              | Посмотреть информацию о метке                                          |
|`git tag -v v1.4.2.1`                                        | Верификация метки                                                      |
|`git push origin v1.5`                                       | Отправить метку в удаленный репозитарий (по умолчанию метки не отправляются) |
|`git push origin --tags`                                     | Отправить все неотправленные метки в удаленный репозитарий             |

### Команды работы с ветками
<table>
<tr>
<th align="left">Комманда</th><th align="left">Описание</th>
</tr>
<tr>
<td align="left"><code>git branch</code></td><td align="left">Показать список веток</td>
</tr>
<tr>
<td align="left"><code>git branch -v</code></td><td align="left">Показать более подробный список веток</td>
</tr>
<tr>
<td align="left"><code>git branch -r</code></td><td align="left">Показать список веток полученных из удаленных репозитариев</td>
</tr>
<tr>
<td align="left"><code>git branch --merged</code></td><td align="left">Показать список слитых веток</td>
</tr>
<tr>
<td align="left"><code>git branch --no-merged</code></td><td align="left">Показать список веток, в которых есть неслитые коммиты</td>
</tr>
<tr>
<td align="left"><code>git branch ticket42</code></td><td align="left">Создать новую ветку ticket42</td>
</tr>
<tr>
<td align="left"><code>git checkout ticket42</code></td><td align="left">Переключится на ветку ticket42</td>
</tr>
<tr>
<td align="left"><code>git checkout -b ticket42</code></td><td align="left">Создать новую ticket42 и переключится на нее</td>
</tr>
<tr>
<td align="left"><code>git checkout -b serverfix origin/serverfix</code></td><td align="left">Создать локальную ветку serverfix, которая будет отслеживать состояние, удаленной ветки serverfix в репозитарии origin и переключится на нее. До этого удаленную ветку необходимо получить командой git fetch origin</td>
</tr>
<tr>
<td alig="left"><code>git checkout --track origin/serverfix</code></td><td align="left">Более короткая форма предыдущей команды. Будет создана локальная ветка serverfix, которая будет отслеживать состояние удаленной ветки origin/serverfix и переключится на нее</td>
</tr>
<tr>
<td align="left"><code>git merge ticket42</code></td><td align="left">Слить текущую ветку и ветку ticket42</td>
</tr>
<tr>
<td align="left"><code>git mergetool</code></td><td align="left">Запустить программу, указанную в merge.tool для разрешения конфликта</td>
</tr>
<tr>
<td align="left"><code>git branch -d ticket42</code></td><td alig="left">Удалить ветку ticket42, при этом все коммиты в этой ветке должны быть влиты</td>
</tr>
<tr>
<td align="left"><code>git branch -D ticket42</code></td><td align="left">Удалить ветку ticket42, в которой могут быть не влитые коммиты</td>
</tr>
<tr>
<td align="left"><code>git push origin :serverfix</code></td><td align="left">Удалить из удаленного репозитария ветку serverfix</td>
</tr>
<tr>
<td align="left"><code>git rebase master</code></td><td align="left">Перемещение текущей ветки на ветку master</td>
</tr>
<tr>
<td align="left"><code>git rebase --onto master server client</code></td><td align="left">Пусть имеем следующуй вид веток:<pre>
               master
                 |
С1&lt;-C2&lt;-С5&lt;-C6&lt;-C7
     \
      C3&lt;-C4&lt;-C10
       \       |
        \    server
         C8&lt;-C9
              |
            client
</pre>После выполнения этой команды будем иметь:<pre>
               master   client
                 |        |
С1&lt;-C2&lt;-С5&lt;-C6&lt;-C7&lt;-C8'&lt;-C9'
     \
      C3&lt;-C4&lt;-C10
               |
             server
</pre>То есть ветка client в свое время основанная на ветке server, перебазируется на ветку master, причем изменения сделанные на ветке server не попадают в ветку master, в том числе коммит C3. Если теперь переключится на ветку master:<br>
<code>git checkout master</code><br>
и сделать<br>
<code>git merge client</code><br>
получим следущую картину:<pre>
                        client
                          |
С1&lt;-C2&lt;-С5&lt;-C6&lt;-C7&lt;-C8'&lt;-C9'
     \                    |
      C3&lt;-C4&lt;-C10       master
               |
             server
</pre>Фактически все изменения сделанные на тематической ветке client, влиты в основную ветку master, а изменения сделанные на ветке server нет.</td>
</tr>
<tr>
<td align="left"><code>git rebase master server</code></td><td align="left">Продолжим работать с деревом веток из предыдущего пояснения, эта команда приведет с следующему виду:<pre>
                        client
                          |
С1&lt;-C2&lt;-С5&lt;-C6&lt;-C7&lt;-C8'&lt;-C9'&lt;-C3'&lt;-C4'&lt;-C10'
                          |              |
                        master         server
</pre>Теперь уже изменения сделанные на ветке server перебазированы на ветку master. Далее переключаемся на ветку master и делаем слияние с веткой server<br>
<code>git checkout master</code><br>
<code>git merge server<code><br>
Получаем следующее:<pre>
                        client         master
                          |              |
С1&lt;-C2&lt;-С5&lt;-C6&lt;-C7&lt;-C8'&lt;-C9'&lt;-C3'&lt;-C4'&lt;-C10'
                                         |
                                       server
</pre>В итоге все изменения сделанные на ветках client и server влиты в основную ветку master и их можно удалить:<br>
<code>git branch -d client</code><br>
<code>git branch -d server</code><br>
Кроме того получена линейная структура коммитов, которую будет понятнее смотреться в удаленном репозитарии</td>
</tr>
</table>

