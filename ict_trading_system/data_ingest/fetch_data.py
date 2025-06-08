import yfinance as yf
import pandas as pd

def fetch_yahoo_ohlcv(symbol='EURUSD=X', interval='1h', period='7d') -> pd.DataFrame:
    """
    Fetches OHLCV data from Yahoo Finance.

    Parameters:
    - symbol (str): Ticker symbol (e.g., 'EURUSD=X', 'AAPL', 'BTC-USD')
    - interval (str): e.g., '1m', '5m', '15m', '1h', '1d'
    - period (str): e.g., '7d', '1mo', '6mo', '1y'

    Returns:
    - pd.DataFrame: Data with ['open', 'high', 'low', 'close', 'volume']
    """
    df = yf.download(tickers=symbol, interval=interval, period=period)
    if df.empty:
        raise ValueError(f"No data returned for symbol: {symbol}")

    df = df[['Open', 'High', 'Low', 'Close', 'Volume']].copy()
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df.index.name = 'timestamp'
    return df
