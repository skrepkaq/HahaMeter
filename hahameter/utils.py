import re


def rusificate_haha(haha: str) -> str:
    """Переводит хаха с англ. раскладки сохраняя регистр"""

    haha = haha.replace('[', 'х').replace('{', 'Х')
    haha = haha.replace('f', 'а').replace('F', 'А')
    return haha


def is_eng(haha: str) -> bool:
    return bool(re.search(r'[\[\{][fF]', haha))


def is_haha(haha: str) -> bool:
    if not haha:
        return False

    haha = rusificate_haha(haha).casefold()

    h_count = len([c for c in haha if c == 'х'])
    h_ratio = h_count / len(haha)

    a_count = len([c for c in haha if c == 'а'])
    a_ratio = a_count / len(haha)

    if h_ratio > 0.2 and a_ratio > 0.2 and len(haha) > 3:
        return True
    return False
