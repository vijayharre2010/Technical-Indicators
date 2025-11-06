def sma(data, period):
    if len(data) < period:
        return None
    return sum(data[-period:]) / period

def stochastic(highs, lows, closes, k_period=14, d_period=3):
    if len(closes) < k_period:
        return None, None
    k_values = []
    for i in range(k_period - 1, len(closes)):
        high_max = max(highs[i - k_period + 1:i + 1])
        low_min = min(lows[i - k_period + 1:i + 1])
        k = 100 * (closes[i] - low_min) / (high_max - low_min) if high_max > low_min else 0
        k_values.append(k)
    d_value = sma(k_values, d_period)
    return k_values[-1] if k_values else None, d_value