from data_ingest.fetch_data import fetch_yahoo_ohlcv
from indicators.bias_detection import detect_bias

# Step 1: Get data
df = fetch_yahoo_ohlcv(symbol='EURUSD=X', interval='1h', period='7d')

# Step 2: Apply bias detection
df['bias'] = detect_bias(df, lookback=20)

# Step 3: Print last 10 rows
print(df[['close', 'bias']].tail(10))
git 