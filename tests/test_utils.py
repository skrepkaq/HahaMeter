from hahameter.utils import is_haha, rusificate_haha, is_eng


def test_rus():
    assert rusificate_haha('хаха') == 'хаха'
    assert rusificate_haha('[f[f') == 'хаха'
    assert rusificate_haha('{F[f') == 'ХАха'
    assert rusificate_haha('[F{f') == 'хАХа'


def test_eng():
    assert is_eng('хаха') is False
    assert is_eng('[f[f') is True
    assert is_eng('{F{F') is True
    assert is_eng('{F[f') is True
    assert is_eng('{f[F') is True


def test_is_haha():
    assert is_haha('') is False
    assert is_haha('хАХа') is True
    assert is_haha('[f{А') is True
    assert is_haha('gптн') is False
    assert is_haha('хаха' + 'п' * 6) is False
    assert is_haha('хахаха' + 'н' * 5) is True
    assert is_haha('х' * 20 + 'а' * 20 + 'x' * 60) is False
    assert is_haha('х' * 21 + 'а' * 21 + 'о' * 58) is True
