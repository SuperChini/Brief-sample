import pandas as pdimportar quandl as q
Import numpy packageimportar numpy as np
import matplotlib.pyplot as plt

# set the API key
q.ApiConfig.api_key = "<API key>”
msft_data = q.get("EOD/MSFT", start_date="2010-01-01", end_date="2022-01-01")
msft_data.describe
assign `Adj Close` to `daily_close`
daily_close = msft_data[['Adj_Close']]
returns as fractional changedaily_return = daily_close.pct_change
replacing NA values with 0
daily_return.fillna(0, inplace=True)
print(daily_return)
mdata = msft_data.resample('M').apply(lambda x: x[-1])monthly_return = mdata.pct_change
assigning adjusted closing prices to adj_pricesadj_price = msft_data['Adj_Close']
calculate the moving averagemav = adj_price.rolling(window=50).mean
print the resultprint(mav[-10:])
adj_price.plot
signal_df = pd.DataFrame(index=msft_data.index)signal_df['signal'] = 0.0
signal_df['short_mav'] = msft_data['Adj_Close'].rolling(window=short_lb, min_periods=1, center=False).mean
signal_df['long_mav'] = msft_data['Adj_Close'].rolling(window=long_lb, min_periods=1, center=False).mean
signal_df['signal'][short_lb:] = np.where(signal_df['short_mav'][short_lb:] > signal_df['long_mav'][short_lb:], 1.0, 0.0)
signal_df['positions'] = signal_df['signal'].diffsignal_df[signal_df['positions'] == -1.0]

