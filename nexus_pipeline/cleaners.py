# Currency normalizer
def clean_currency(val: str) -> float:
    clean = str(val).replace('$', '').replace(',', '').strip()
    return float(clean) if clean else 0.0
