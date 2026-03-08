import pandas as pd
import matplotlib.pyplot as plt

# load dataset
data = pd.read_csv("compact.csv")

# remove global aggregates
exclude = ["World","Asia","Europe","Africa","North America","South America","Oceania"]
data = data[~data["country"].isin(exclude)]

# convert date column
data["date"] = pd.to_datetime(data["date"])

# select one country (example: India)
india = data[data["country"] == "India"]

# plot trend
plt.figure(figsize=(10,5))
plt.plot(india["date"], india["total_cases"]/1000000)

plt.title("COVID Cases Over Time in India")
plt.xlabel("Date")
plt.ylabel("Total Cases(Millions)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Top 10 countries by vaccinations

filtered = data[~data["country"].str.contains("World|Asia|Europe|income|Union", na=False)]

vaccinations = filtered.groupby("country")["people_fully_vaccinated"].max().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
(vaccinations/1000000).plot(kind="bar", color="green")

plt.title("Top 10 Countries by COVID Vaccinations")
plt.xlabel("Country")
plt.ylabel("People Fully Vaccinated(Millions)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()