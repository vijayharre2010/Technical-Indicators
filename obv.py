def obv(closes, volumes):
    if len(closes) != len(volumes) or len(closes) < 2:
        return None
    obv_val = 0
    for i in range(1, len(closes)):
        if closes[i] > closes[i-1]:
            obv_val += volumes[i]
        elif closes[i] < closes[i-1]:
            obv_val -= volumes[i]
    return obv_val