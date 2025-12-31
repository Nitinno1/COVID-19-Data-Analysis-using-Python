import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Covid_data.csv")

df.columns = df.columns.str.strip()

df['State_UT'] = df['State_UT'].astype(str).str.strip().str.title()

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

df['Confirmed'] = df['Confirmed'].fillna(0)
df['Recovered'] = df['Recovered'].fillna(0)
df['Deaths'] = df['Deaths'].fillna(0)
df['Phase'] = df['Phase'].fillna('Not Specified')

df = df.drop_duplicates(subset=['State_UT', 'Date'])

df['Active'] = df['Confirmed'] - df['Recovered'] - df['Deaths']

num_cols = ['Confirmed', 'Recovered', 'Deaths', 'Active']
df[num_cols] = df[num_cols].clip(lower=0).round().astype(int)

df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

df['Recovery_Rate'] = np.where(
    df['Confirmed'] > 0,
    (df['Recovered'] / df['Confirmed']) * 100,
    0
)

top_states = (
    df.groupby('State_UT')['Confirmed']
    .max()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 5))
top_states.plot(kind='bar')
plt.title("Top 10 States by Confirmed COVID Cases")
plt.xlabel("State")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

state = input("Enter State Name: ").strip().title()

if state not in df['State_UT'].unique():
    print("❌ State not found!")
    print("\nAvailable States:")
    print(sorted(df['State_UT'].unique()))
else:
    state_df = df[df['State_UT'] == state].sort_values('Date')

    plt.figure(figsize=(10, 5))
    plt.plot(state_df['Date'], state_df['Confirmed'], label='Confirmed')
    plt.plot(state_df['Date'], state_df['Recovered'], label='Recovered')
    plt.plot(state_df['Date'], state_df['Deaths'], label='Deaths')
    plt.legend()
    plt.title(f"COVID-19 Trend in {state}")
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.tight_layout()
    plt.show()

phase_avg = df.groupby('Phase')['Active'].mean()

plt.figure(figsize=(8, 5))
phase_avg.plot(kind='bar')
plt.title("Average Active Cases by Lockdown Phase")
plt.xlabel("Phase")
plt.ylabel("Active Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

pivot = df.pivot_table(
    values='Active',
    index='State_UT',
    columns='Phase',
    aggfunc='mean'
).fillna(0)

plt.figure(figsize=(14, 8))
sns.heatmap(pivot, cmap='coolwarm', linewidths=0.5)
plt.title("Active COVID Cases Heatmap (State vs Phase)")
plt.xlabel("Phase")
plt.ylabel("State")
plt.tight_layout()
plt.show()
