import pandas as pd
import matplotlib.pyplot as plt

print("Loading data...")

# Load datasets
trades = pd.read_csv("data/historical_data.csv")
sentiment = pd.read_csv("data/fear_greed_index.csv")

# Convert dates
trades['time'] = pd.to_datetime(trades['time'])
sentiment['Date'] = pd.to_datetime(sentiment['Date'])

# Create common date
trades['date'] = trades['time'].dt.date
sentiment['date'] = sentiment['Date'].dt.date

# Merge datasets
data = pd.merge(trades, sentiment, on='date', how='left')

# Clean data
data = data.dropna(subset=['Classification'])
data['closedPnL'] = pd.to_numeric(data['closedPnL'], errors='coerce')

# Create profit column
data['profit'] = data['closedPnL'] > 0

print("\n--- Results ---\n")

# Analysis
print("Average Profit:")
print(data.groupby('Classification')['closedPnL'].mean())

print("\nWin Rate:")
print(data.groupby('Classification')['profit'].mean())

print("\nAverage Leverage:")
print(data.groupby('Classification')['leverage'].mean())

# Simple visualization
data.boxplot(column='closedPnL', by='Classification')
plt.title("Profit by Market Sentiment")
plt.suptitle("")
plt.show()

print("\nDone.")