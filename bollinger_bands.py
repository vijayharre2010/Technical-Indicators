import math

def bollinger_bands(closes, period=20, std_dev=2):
    if len(closes) < period:
        return None, None, None
    sma_val = sum(closes[-period:]) / period
    variance = sum((x - sma_val)**2 for x in closes[-period:]) / period
    std = math.sqrt(variance)
    upper = sma_val + std_dev * std
    lower = sma_val - std_dev * std
    return upper, sma_val, lower