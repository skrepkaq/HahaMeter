import random
import string

from hahameter import HahaMeter, metrics
from hahameter.config import Factors as fc
from hahameter.haha_meter import get_score

import pytest
from unittest.mock import patch


def mock_length(_):
    return 0.1


def mock_caps(_):
    return 0.15


def mock_eng(_):
    return 0.23


def mock_keyboard_slam(_):
    return 0.59


def mock_p_start(_):
    return 0.61


def mock_sequential(_):
    return 0.98


@pytest.fixture(autouse=True)
def mock_metrics():
    with patch.object(metrics, 'length', mock_length), \
         patch.object(metrics, 'caps', mock_caps), \
         patch.object(metrics, 'eng', mock_eng), \
         patch.object(metrics, 'keyboard_slam', mock_keyboard_slam), \
         patch.object(metrics, 'p_start', mock_p_start), \
         patch.object(metrics, 'sequential', mock_sequential):
        yield


def test_hahameter():
    haha_meter = HahaMeter()
    haha = "хаха"
    score = haha_meter(haha)
    expected_score = (
        mock_length(haha) * fc.LENGTH +
        mock_caps(haha) * fc.CAPS +
        mock_eng(haha) * fc.ENG +
        mock_keyboard_slam(haha) * fc.SLAM +
        mock_p_start(haha) * fc.PSTART +
        mock_sequential(haha) * fc.SEQUENTIAL
    ) / (fc.LENGTH + fc.CAPS + fc.ENG + fc.SLAM + fc.PSTART + fc.SEQUENTIAL)
    assert score == round(expected_score, 2)


def test_hahameter_custom_factors():
    custom_factors = {
        'ln': random.randint(1, 10),
        'cp': random.randint(1, 10),
        'en': random.randint(1, 10),
        'ks': random.randint(1, 10),
        'p': random.randint(1, 10),
        'seq': random.randint(1, 10)
    }
    haha_meter = HahaMeter(**custom_factors)
    haha = "хаха"
    score = haha_meter(haha)
    expected_score = (
        mock_length(haha) * custom_factors['ln'] +
        mock_caps(haha) * custom_factors['cp'] +
        mock_eng(haha) * custom_factors['en'] +
        mock_keyboard_slam(haha) * custom_factors['ks'] +
        mock_p_start(haha) * custom_factors['p'] +
        mock_sequential(haha) * custom_factors['seq']
    ) / sum(custom_factors.values())
    assert score == round(expected_score, 2)


def test_empty_haha():
    haha_meter = HahaMeter()
    haha = ""
    with pytest.raises(ValueError):
        haha_meter(haha)


def test_random_str():
    rus = [chr(_) for _ in range(ord("а"), ord("а") + 32)]
    rus += [chr(_) for _ in range(ord("А"), ord("А") + 32)]
    rus += 'ёЁ'
    rus = ''.join(rus)

    for _ in range(1000):
        haha = ''.join(random.choices(string.printable + rus, k=random.randint(1, 100)))
        score = get_score(haha)
        print(f'[{score}] {haha}')
        assert 0 <= score <= 1
