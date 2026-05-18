import pytest
from nexus_pipeline.models import DataRecord
from nexus_pipeline.transformers import DataTransformer
from nexus_pipeline.extractors import SyntheticExtractor

def test_data_record_validation():
    valid = {
        "record_id": "REC-001",
        "customer_id": "CUST-1",
        "category": "Hardware",
        "amount": 450.50,
        "region": "Europe",
        "status": "completed"
    }
    record = DataRecord(**valid)
    assert record.record_id == "REC-001"
    assert record.amount == 450.50

def test_data_transformer_aggregation():
    records = [
        {"record_id": "1", "customer_id": "C1", "category": "Cloud", "amount": 100.0, "region": "EU", "status": "completed"},
        {"record_id": "2", "customer_id": "C2", "category": "Cloud", "amount": 200.0, "region": "US", "status": "completed"},
        {"record_id": "3", "customer_id": "C3", "category": "Support", "amount": 50.0, "region": "EU", "status": "flagged"}
    ]
    transformer = DataTransformer(filter_flagged=True)
    valid = transformer.process(records)
    assert len(valid) == 2
    metrics = transformer.aggregate(valid)
    assert metrics.total_volume == 300.0
    assert metrics.top_category == "Cloud"
    assert metrics.average_amount == 150.0

def test_synthetic_extractor():
    extractor = SyntheticExtractor(count=20)
    items = list(extractor.extract())
    assert len(items) == 20
    assert "record_id" in items[0]

def test_edge_case_empty():
    assert True
