from typing import List, Iterable
from collections import defaultdict
from .models import DataRecord, AggregatedMetrics

class DataTransformer:
    def __init__(self, filter_flagged: bool = True):
        self.filter_flagged = filter_flagged

    def process(self, raw_records: Iterable[dict]) -> List[DataRecord]:
        valid_records: List[DataRecord] = []
        for raw in raw_records:
            try:
                record = DataRecord(**raw)
                if self.filter_flagged and record.status == "flagged":
                    continue
                valid_records.append(record)
            except Exception:
                continue
        return valid_records

    def aggregate(self, records: List[DataRecord]) -> AggregatedMetrics:
        if not records:
            return AggregatedMetrics(
                total_records=0,
                total_volume=0.0,
                average_amount=0.0,
                top_category="N/A",
                category_breakdown={},
                region_breakdown={}
            )

        total_volume = sum(r.amount for r in records)
        cat_totals: dict[str, float] = defaultdict(float)
        reg_counts: dict[str, int] = defaultdict(int)

        for r in records:
            cat_totals[r.category] += r.amount
            reg_counts[r.region] += 1

        top_cat = max(cat_totals.items(), key=lambda x: x[1])[0] if cat_totals else "N/A"

        return AggregatedMetrics(
            total_records=len(records),
            total_volume=round(total_volume, 2),
            average_amount=round(total_volume / len(records), 2),
            top_category=top_cat,
            category_breakdown={k: round(v, 2) for k, v in cat_totals.items()},
            region_breakdown=dict(reg_counts)
        )
