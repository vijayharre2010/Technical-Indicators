def adx(highs, lows, closes, period=14):
    if len(highs) < period + 1:
        return None
    dm_plus = []
    dm_minus = []
    tr_values = []
    for i in range(1, len(highs)):
        move_up = highs[i] - highs[i-1]
        move_down = lows[i-1] - lows[i]
        dm_p = move_up if move_up > move_down and move_up > 0 else 0
        dm_m = move_down if move_down > move_up and move_down > 0 else 0
        dm_plus.append(dm_p)
        dm_minus.append(dm_m)
        tr = max(highs[i] - lows[i], abs(highs[i] - closes[i-1]), abs(lows[i] - closes[i-1]))
        tr_values.append(tr)
    avg_dm_plus = sum(dm_plus[:period]) / period
    avg_dm_minus = sum(dm_minus[:period]) / period
    avg_tr = sum(tr_values[:period]) / period
    for i in range(period, len(dm_plus)):
        avg_dm_plus = (avg_dm_plus * (period - 1) + dm_plus[i]) / period
        avg_dm_minus = (avg_dm_minus * (period - 1) + dm_minus[i]) / period
        avg_tr = (avg_tr * (period - 1) + tr_values[i]) / period
    di_plus = 100 * avg_dm_plus / avg_tr if avg_tr != 0 else 0
    di_minus = 100 * avg_dm_minus / avg_tr if avg_tr != 0 else 0
    dx = 100 * abs(di_plus - di_minus) / (di_plus + di_minus) if di_plus + di_minus != 0 else 0
    return dx