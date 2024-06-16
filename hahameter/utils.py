import re


def rusificate_haha(haha: str) -> str:
    """Переводит хаха с англ. раскладки сохраняя регистр"""

    haha = haha.replace('[', 'х').replace('{', 'Х')
    haha = haha.replace('f', 'а').replace('F', 'А')
    return haha


def is_eng(haha: str) -> bool:
    return bool(re.search(r'[\[\{][fF]', haha))


def is_haha(haha: str) -> bool:
    haha = rusificate_haha(haha).casefold()

    ha_count = len([c for c in haha if c in ('х', 'а')])
    ha_ratio = ha_count / len(haha)

    if ha_ratio >= 0.5 or ha_count >= 10:
        return True
    return False
