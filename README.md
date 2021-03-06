# Решатель квадратных уравнений

Скрипт для решения уравнений вида **ax² + bx + c = 0**, где a, b, c — некоторые числа (a ≠ 0), x — неизвестное).


### Как использовать

Скрипт принимает на вход коэффициенты  a, b, c и возращает корни уравнения.

### Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
$ python aleksandra.katonina$ python quadratic_equation.py -a 1 -b 2 -c -3
# может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
(-3.0, 1.0)
```

Запуск тестов:
```
python tests.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

Запуск на Windows происходит аналогично.


### Программное использование
```python
from quadratic_equation import get_roots
root1, root2 = get_roots(1, 2, 4)
```

### Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
