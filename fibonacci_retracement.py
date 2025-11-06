def fibonacci_retracement(high, low):
    diff = high - low
    levels = {
        0: low,
        0.236: low + 0.236 * diff,
        0.382: low + 0.382 * diff,
        0.5: low + 0.5 * diff,
        0.618: low + 0.618 * diff,
        1: high
    }
    return levels