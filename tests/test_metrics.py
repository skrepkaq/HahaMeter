from hahameter.metrics import length, caps, keyboard_slam, eng, p_start, sequential


def test_length():
    assert length('ха') == 0
    assert length('хаха') == 0.05
    assert round(length('х' * 7), 4) == 0.3125
    assert round(length('х' * 8), 4) == 0.4
    assert round(length('х' * 15), 4) == 0.8775
    assert round(length('х' * 19), 4) == 0.9797
    assert length('а' * 20) == 1


def test_caps():
    assert caps('а' * 10) == 0
    assert caps('Х' + 'а' * 9) == 0
    assert caps('Х' * 2 + 'а' * 8) == 0.2
    assert caps('Х' * 5 + 'а' * 5) == 0.5
    assert caps('Х' * 8 + 'а' * 2) == 1
    assert caps('Х' * 10) == 0.9

    assert caps('FFХХХаааff') == 0.5
    assert caps('ХАХАХ{F{{F') == 0.9


def test_slam():
    assert keyboard_slam('хаха') == 0
    assert keyboard_slam('[f{F') == 0
    assert keyboard_slam('а' * 8 + 'зм') == 0.264
    assert keyboard_slam('f' * 8 + 'pv') == 0.264
    assert keyboard_slam('а' * 9 + 'в') == 0.264
    assert keyboard_slam('f' * 9 + 'd') == 0.264
    assert keyboard_slam('а' * 7 + 'дщт') == 0.52
    assert keyboard_slam('а' * 7 + 'l.n') == 0.52
    assert keyboard_slam('хавьдлкрепиощзшхъдап') == 1
    assert keyboard_slam('[fdmlkrhtgbjopi[]lfg') == 1


def test_eng():
    assert eng('хаха') == 0
    assert eng('[f[f') == 1
    assert eng('{F{F') == 1
    assert eng('{F[f') == 1
    assert eng('{f[F') == 1


def test_p_start():
    assert p_start('хаха') == 0
    assert p_start('пхаха') == 1
    assert p_start('Пхаха') == 1


def test_sequential():
    assert sequential('хахахаха') == 0
    assert sequential('ххахахах') == 0.5
    assert sequential('хххахаха') == 1
    assert sequential('[f;хlf[[') == 0.5
    assert sequential('ьлдеиоткьхатрха') == 0
