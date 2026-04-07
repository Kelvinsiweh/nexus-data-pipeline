import json
import csv
from pathlib import Path
from typing import Iterator, Dict, Any, List
from .models import DataRecord

class BaseExtractor:
    def extract(self) -> Iterator[Dict[str, Any]]:
        raise NotImplementedError

class CsvExtractor(BaseExtractor):
    def __init__(self, filepath: str | Path):
        self.filepath = Path(filepath)

    def extract(self) -> Iterator[Dict[str, Any]]:
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {self.filepath}")
        with open(self.filepath, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield {
                    "record_id": row.get("record_id"),
                    "customer_id": row.get("customer_id"),
                    "category": row.get("category"),
                    "amount": float(row.get("amount", 0.0)),
                    "region": row.get("region", "Global"),
                    "status": row.get("status", "completed"),
                    "tags": [t.strip() for t in row.get("tags", "").split(",") if t.strip()]
                }

class SyntheticExtractor(BaseExtractor):
    """Generates realistic sample enterprise data for benchmarking."""
    def __init__(self, count: int = 50):
        self.count = count

    def extract(self) -> Iterator[Dict[str, Any]]:
        import random
        categories = ["Cloud Services", "Hardware", "Consulting", "Licensing", "Support"]
        regions = ["North America", "Europe", "Asia Pacific", "Latin America"]
        for i in range(1, self.count + 1):
            yield {
                "record_id": f"REC-{1000 + i}",
                "customer_id": f"CUST-{random.randint(100, 999)}",
                "category": random.choice(categories),
                "amount": round(random.uniform(25.0, 4800.0), 2),
                "region": random.choice(regions),
                "status": random.choice(["completed", "completed", "completed", "flagged"]),
                "tags": ["enterprise", "q3"]
            }
# Optimized streaming buffer
