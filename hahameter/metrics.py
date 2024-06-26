import math

from . import utils


def length(haha: str) -> float:
    """Длиннее - смешнее"""
    length = len(haha)
    if length < 4:
        return 0
    elif length < 8:
        return 0.0875 * (length - 4) + 0.05
    elif length <= 20:
        return 0.6 * math.log(0.75 * (length - 8) + 1, 10) + 0.4
    return 1


def caps(haha: str) -> float:
    """Чем больше капса - тем смешнее, но если всё сообщение капс, то не так смешно"""
    haha = utils.rusificate_haha(haha)
    caps_count = len([c for c in haha if c.isupper()])
    caps_ratio = caps_count / len(haha)
    if caps_ratio < 0.2 or caps_count < 2:
        return 0
    elif caps_ratio < 0.6:
        return caps_ratio
    elif caps_ratio > 0.95:
        return 0.9
    return 1


def keyboard_slam(haha: str) -> float:
    """Чем дальше от 'х' и 'а' были промахи по клавишам - тем смешнее"""
    chars = [
        'ха',
        'зжэпмсp;\'gvc:"',
        'ъ=-вке]=-drt}+_',
        '0щдю.\\уычирн654ol./esxbhy)|^%$>?'
    ]
    total_slam = 0
    for c in utils.rusificate_haha(haha).casefold():
        for points, charset in enumerate(chars):
            if c in charset:
                total_slam += points
                break
        else:
            total_slam += 4
    slam_coef = total_slam / len(haha)
    if slam_coef == 0:
        return 0
    elif slam_coef > 2:
        return 1
    return slam_coef * 0.32 + 0.2


def eng(haha: str) -> float:
    """Забыл переключить раскладку - смешнее"""
    return float(utils.is_eng(haha))


def p_start(haha: str) -> float:
    """Написал ПХАХАХАХАХ - смешнее"""
    if haha.casefold()[0] == 'п':
        return 1
    return 0


def sequential(haha: str) -> float:
    """Не писал идеально хахаха, а например хахххахахаах - смешнее"""
    mismatch_count = 0
    haha = utils.rusificate_haha(haha).casefold()
    for i in range(len(haha) - 1):
        if haha[i] in ('х', 'а') and haha[i] == haha[i+1]:
            mismatch_count += 1
    if mismatch_count > 2:
        return 1
    return mismatch_count / 2
