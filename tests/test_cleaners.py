import pytest
from nexus_pipeline.cleaners import clean_currency

def test_clean_currency():
    assert clean_currency('$1,250.50') == 1250.50
    assert clean_currency('0') == 0.0
