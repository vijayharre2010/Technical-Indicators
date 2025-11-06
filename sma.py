def sma(data, period):
    if len(data) < period:
        return None
    return sum(data[-period:]) / period