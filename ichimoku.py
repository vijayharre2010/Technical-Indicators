def ichimoku(highs, lows, closes):
    tenkan_period = 9
    kijun_period = 26
    senkou_period = 52
    if len(highs) < senkou_period:
        return None
    tenkan_high = max(highs[-tenkan_period:])
    tenkan_low = min(lows[-tenkan_period:])
    tenkan = (tenkan_high + tenkan_low) / 2
    kijun_high = max(highs[-kijun_period:])
    kijun_low = min(lows[-kijun_period:])
    kijun = (kijun_high + kijun_low) / 2
    senkou_a = (tenkan + kijun) / 2
    senkou_b_high = max(highs[-senkou_period:])
    senkou_b_low = min(lows[-senkou_period:])
    senkou_b = (senkou_b_high + senkou_b_low) / 2
    chikou = closes[-kijun_period]
    return tenkan, kijun, senkou_a, senkou_b, chikou