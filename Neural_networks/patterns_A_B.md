Рассмотрим следующие пэттерны $A$ и $B$ , нам требуется доказать, что перцептрон не может отличать эти два пэттерна, при условии одинакового количества активных элементов и возможности сдвига.

При идентицикации пэттерна $A$ перцептрон должен показывать 1, при пэттерне $B$ 0. И в том и другом классе возможны 6 сдвигов.

Рассмотрим все возможные виды примеры пэттернов $A$ и $B$

$a_1=[101110]$ , $a_2=[010111]$, $a_3=[101011]$, $a_4=[110101]$, $a_5=[111010]$,  $a_6=[011101]$

$b_1=[101101]$, $b_2=[110110]$$,   $ $b_3=[011011]$ ,  $b_4=[101101]$ ,   $ b_5=[110110]$,  $b_6=[011011]$

Распишем для всех этих паттернов условия для определения паттерна А или В:

$a_1 : w_1 + w_3 + w_4 + w_5 + b \geq 0$ ﻿

$a_2: w_2 + w_4 + w_5 + w_6 + b\geq 0 $

$a_3:  w_1 + w_3 + w_5 + w_6 + b \geq 0$ ﻿

$a_4 : w_1 + w_2 + w_4 + w_6 + b\geq 0 $

$a_5:  w_1 + w_2 + w_3 + w_5 + b \geq 0$ ﻿

$a_6:  w_2+ w_3 + w_4 + w_6 + b \geq 0$ ﻿



$b_1 : w_1 + w_3 + w_4 + w_6 + b < 0$ ﻿

$b_2: w_1 + w_2 + w_4 + w_5 + b< 0 $

$b_3:  w_2 + w_3 + w_5 + w_6 + b < 0$ ﻿

$b_4 : w_1 + w_3 + w_4 + w_6 + b< 0 $

$b_5:  w_1 + w_2 + w_4 + w_5 + b < 0$ ﻿

$b_6:  w_2+ w_3 + w_5 + w_6 + b < 0$ ﻿

Если просуммировать все эти условия, мы получим следующее для паттерна $A$:

$\sum_{i=1}^{6}4*w_i + 6*b \geq 0$

Аналогично для пэттерна $B$

$\sum_{i=1}^{6}4*w_i + 6*b < 0$



(Дополнительно мы можем записать это в еще более общем виде:

$\sum_{i=1}^{n}a*w_i + n*b \geq 0$ где $a$ - это количество активных элементов, а $n$ - количество всех возможных сдвигов

$\sum_{i=1}^{n}a*w_i + n*b < 0$ где $a$ - это количество активных элементов, а $n$ - количество всех возможных сдвигов)



Таким образом мы наблюдаем абсолютно идентичное поведение для обоих паттернов, каждый элемент активируется по 4 раза $A: \sum_{i=1}^{6}4*w_i + 6*b \geq 0$ ,     $B: \sum_{i=1}^{6}4*w_i + 6*b < 0$ , и не возможно подобрать веса $w_i$, которые могли бы позволить перцептрону различить между этими классами так как для обоих классов он получает абсолютно одинаковую входную информацию
