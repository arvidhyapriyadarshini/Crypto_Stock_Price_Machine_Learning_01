
import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()

d01 = today.strftime("%Y-%m-%d")
end_date = d11
d02 = date.today() - timedelta(days=730)
d02 = d02.strftime("%Y-%m-%d")
start_date = d02

data01 = yf.download('BTC-USD',
                      start=start_date,
                      end=end_date,
                      progress=False)
data01["Date"] = data01.index
data = data01[["Date","Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
print(data01.head())

# Save data to CSV
data.to_csv('bitcoin_data.csv', index=False)

correlation = data.corr()
print(correlation["Close"].sort_values(ascending=False))

pip install AutoTS

from autots import AutoTS

# Create the AutoTS model
model = AutoTS(forecast_length=10, frequency='infer', ensemble='simple')

# Fit the model to the data
model = model.fit(data, date_col='Date', value_col='Close', id_col=None)

# Make predictions
prediction = model.predict()

# Get the forecasted values
forecast = prediction.forecast

# Print the forecast
print(forecast)

print(forecast)

