import yfinance as yf
from plotly import graph_objs as go

crypto_data = yf.download('BTC-USD', start='2024-01-01', end='2024-06-01')

fig = go.Figure(data=[go.Candlestick(
    x=crypto_data.index,
    open=crypto_data['Open'],
    high=crypto_data['High'],
    low=crypto_data['Low'],
    close=crypto_data['Close'],
)])

fig.update_layout(
    title='Bitcoin Candlestick chart',
    yaxis_title='Price (USD)',
    xaxis_rangeslider_visible=False,
    xaxis=dict(
        rangeslider=dict(
            visible=False
        )
    ),
    plot_bgcolor = 'rgb(29, 37, 51)',
    font=dict(
        family='Courier New, monospace',
        size=15,
        color='black'
    )
)

fig.show()
