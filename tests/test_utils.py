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
    assert is_haha('[f{A') is True
    assert is_haha('gптн') is False
    assert is_haha('хаха' + 'п' * 6) is False
    assert is_haha('хахах' + 'н' * 5) is True
    assert is_haha('ха' * 4 + 'x' * 99) is False
    assert is_haha('ха' * 5 + 'g' * 99) is True
