# HahaMeter
Мой друг совершенно не умеет смеяться в переписке и отвечает на любую шутку:
> хаха

Возможно конечно что все мои штуки настолько не смешные (я оговорился, не возможно конечно (надеюсь)), но скорее всего он просто не знает как выразить своё восхищение моим утончённым юмором, и поэтому я решил ему помочь, написав алгоритм для вычисления на сколько собеднику сшешно судя по его смеху в переписке и теперь теперь благодаря этому алгоритму он легко сможет проверить что его «хаха» - это всего лишь:
```python
>>> get_score('хаха')
0.01
```
**0.01** по шкале от **0 до 1**
Но например:
```python
>>> get_score('Ахахахахаха')
0.18
>>> get_score('хахахахаххахахам')
0.35
>>> get_score('ХАХЗАВЖХАХЖАХЖХЖав')
0.58
```
### Установка
```
pip install git+https://github.com/skrepkaq/HahaMeter.git
```
  ### Использование
  Стандартные метрики
```python
from hahameter import get_score

get_score('АХВХАЖХВАЖХВДАЮВДЗА')
# 0.61
```
Кастомные метрики
```python
from hahameter import HahaMeter

# длина важнее всего, а капс вообще не важен
my_meter = HahaMeter(
    ln=50,  # длина
    cp=0    # капс
)

my_meter('АХВХАЖХВАЖХВДАЮВДЗА')
# 0.85
```
### Метрики оценивания
Запатентованы и засекречены.
Я запрещаю вам смотреть их в ```hahameter/metrics.py```
