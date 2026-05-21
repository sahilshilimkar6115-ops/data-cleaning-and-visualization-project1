import pandas as pd

data = {
    "Team": ["CSK", "MI", "RCB", "KKR", "SRH", "CSK"],
    "Runs": [180, 200, 190, 170, None, 180],
    "Wickets": [5, 4, 6, 7, 5, 5]
}

df = pd.DataFrame(data)


print("IPL Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())


df["Runs"] = df["Runs"].fillna(df["Runs"].mean())


df = df.drop_duplicates()


print("\nCleaned Dataset:")
print(df)


print("\nHighest Runs:")
print(df["Runs"].max())


print("\nAverage Runs:")
print(df["Runs"].mean())