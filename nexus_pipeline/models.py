from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, field_validator

class DataRecord(BaseModel):
    record_id: str = Field(..., description="Unique record identifier")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    customer_id: str
    category: str
    amount: float = Field(..., ge=0.0, description="Transaction amount in USD")
    region: str
    status: str = Field(default="completed")
    tags: List[str] = Field(default_factory=list)

    @field_validator("status")
    @classmethod
    def validate_status(cls, v: str) -> str:
        allowed = {"completed", "pending", "flagged", "cancelled"}
        if v.lower() not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return v.lower()

class AggregatedMetrics(BaseModel):
    total_records: int
    total_volume: float
    average_amount: float
    top_category: str
    category_breakdown: dict[str, float]
    region_breakdown: dict[str, int]
