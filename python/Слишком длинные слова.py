
Не могу понять как решить Эту задачу !?

Слишком длинные слова
Иногда некоторые слова вроде «localization» или «internationalization» настолько длинны, что их весьма утомительно писать много раз в каком либо тексте.

Будем считать слово слишком длинным, если его длина строго больше 10 символов. Все слишком длинные слова можно заменить специальной аббревиатурой.

Эта аббревиатура строится следующим образом: записывается первая и последняя буква слова, а между ними — количество букв между первой и последней буквой (в десятичной системе счисления и без ведущих нулей).

Таком образом, «localization» запишется как «l10n», а «internationalization» как «i18n».

Вам предлагается автоматизировать процесс замены слов на аббревиатуры. При этом все слишком длинные слова должны быть заменены аббревиатурой, а слова, не являющиеся слишком длинными, должны остаться без изменений.

Входные данные
В первой строке содержится целое число n (1 ≤ n ≤ 100). В каждой из последующих n строк содержится по одному слову. Все слова состоят из малых латинских букв и имеют длину от 1 до 100 символов.

Выходные данные
Выведите n строк. В i строке должен находиться результат замены i-го слова из входных данных.
















n = int(input())

w = 'word'
l = 'localization'
i = 'internationalization'
p = 'pneumonoultramicroscopicsilicovolcanoconiosis'

if n % 2==0 and len(w)<10:
    print('word')
if n % 2==0 and len(l)>10:
    l = 'l10n'
    print(l)
if n % 2 ==0 and len(i)>10:
    i = 'i18n'
    print(i)
if n % 2 == len(p)>10:
    i = 'p43s'
    print(i)
