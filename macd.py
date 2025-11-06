def ema(data, period):
    if len(data) < period:
        return None
    alpha = 2 / (period + 1)
    ema_val = sum(data[:period]) / period
    for price in data[period:]:
        ema_val = alpha * price + (1 - alpha) * ema_val
    return ema_val

def macd(closes, fast_period=12, slow_period=26, signal_period=9):
    if len(closes) < slow_period:
        return None, None
    fast_emas = []
    slow_emas = []
    for i in range(fast_period - 1, len(closes)):
        fast_emas.append(ema(closes[:i+1], fast_period))
    for i in range(slow_period - 1, len(closes)):
        slow_emas.append(ema(closes[:i+1], slow_period))
    min_len = min(len(fast_emas), len(slow_emas))
    macd_lines = [fast_emas[i] - slow_emas[i] for i in range(min_len)]
    signal_line = ema(macd_lines, signal_period)
    return macd_lines[-1] if macd_lines else None, signal_line