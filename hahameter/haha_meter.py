from typing import Optional

from hahameter import metrics
from .config import Factors as fc


class HahaMeter():
    def __init__(
            self,
            ln: Optional[int] = fc.LENGTH,
            cp: Optional[int] = fc.CAPS,
            en: Optional[int] = fc.ENG,
            ks: Optional[int] = fc.SLAM,
            p: Optional[int] = fc.PSTART,
            seq: Optional[int] = fc.SEQUENTIAL
    ) -> None:
        self.METRICS = [
            (metrics.length, ln),
            (metrics.caps, cp),
            (metrics.eng, en),
            (metrics.keyboard_slam, ks),
            (metrics.p_start, p),
            (metrics.sequential, seq),
        ]

    def __call__(self, haha: str) -> float:
        if not haha:
            raise ValueError('Тебе в ответ на шутку отправили пустую строку? Ну, соболезную...')

        score = 0
        total_ratios = sum([r[1] for r in self.METRICS])

        for metric in self.METRICS:
            score += metric[0](haha) * metric[1]
        return round(score / total_ratios, 2)


default_meter = HahaMeter()


def get_score(haha: str) -> float:
    return default_meter(haha)
