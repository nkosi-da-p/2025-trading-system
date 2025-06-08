import pandas as pd

def detect_bias(df: pd.DataFrame, lookback=20) -> pd.Series:
    """
    Detects market bias using swing high/low structure logic.

    Parameters:
    df (pd.DataFrame): Must have ['high', 'low'] columns and datetime index.
    lookback (int): Number of candles to look back for swing structure.

    Returns:
    pd.Series: Bias label per candle ['bullish', 'bearish', 'neutral']
    """
    highs = df['high']
    lows = df['low']
    bias = []

    for i in range(len(df)):
        if i < lookback:
            bias.append('neutral')
            continue

        window_highs = highs[i - lookback:i]
        window_lows = lows[i - lookback:i]

        recent_high = highs[i]
        recent_low = lows[i]

        prior_swing_high = window_highs.max()
        prior_swing_low = window_lows.min()

        if recent_high > prior_swing_high:
            bias.append('bullish')
        elif recent_low < prior_swing_low:
            bias.append('bearish')
        else:
            bias.append('neutral')

    return pd.Series(bias, index=df.index, name='bias')
