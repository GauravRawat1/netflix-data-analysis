import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#DataSet loading
dt = pd.read_csv("Data/netflix_titles.csv")

print("\t====== NETFIX DATA ANALYSIS ======\t")
#DataSet overview
print("\nDataSet Overview:\n", dt.head(7))
print("\nDataSet Shape:\n",dt.shape)
print("\nNumber of Columns Present:\n",dt.columns)
print("\nMissing Values in(Columns):\n",dt.info())

#Data Cleaning
print("\nCLEANING DATA....\n")
#Handling Missing values
print("\nMissing Values in:\n",dt.isnull().sum())
#Missing Values treatment for Director,Cast,Country,Date_Added,Rating
dt["director"] = dt["director"].fillna("Unknown")
dt["cast"] = dt["cast"].fillna("Unknown")
dt["country"] = dt["country"].fillna("Unknown")
dt["rating"] = dt["rating"].fillna("Not Rated")
dt.dropna(subset=["date_added"], inplace=True)
dt.dropna(subset=["duration"], inplace=True)
#Handling Duplicate Values
print("\nDuplicate Values:\n",dt.duplicated().sum())
if dt.duplicated().sum() > 0:
    print("Duplicate Rows Removed..\n",dt.drop_duplicates(inplace=True))
else:
    print("\nNo Duplicate Value Found.\n")

#Data Cleaning Summery
print("\nData Cleaned Sucessfully...\nFinal Shape:\n",dt.shape)
print("\nMissing Values After Cleaning:\n",dt.isnull().sum())

#Feature engineering
dt["date_added"] = (
    dt["date_added"]
    .astype(str)
    .str.strip()
)
dt["date_added"] = pd.to_datetime(dt["date_added"], errors="coerce")
dt["year_added"] = dt["date_added"].dt.year
dt["month_added"] = dt["date_added"].dt.month_name()
dt["day_added"] = dt["date_added"].dt.day_name()
#content age 
dt["content_age"] = 2025 - dt["release_year"]
#dacade
dt["decade"] = (dt["release_year"] // 10) * 10
#Duration category
movie = dt[dt["type"] == "Movie"].copy()
movie["duration_num"] = (movie["duration"].str.extract(r'(\d+)').astype(int))
#Movie Category
movie["durationCt"] = pd.cut(movie["duration_num"],bins=[0,60,120,180,1000],
                             labels=["Short","Medium","Long","Very long"])

#EDA
contentType = (dt["type"].value_counts())
topCountries = (dt["country"].value_counts().head(10))
ratings = (dt["rating"].value_counts())
yearlyGrowth = (dt["year_added"].value_counts().sort_index())
releaseDate = (dt["release_year"].value_counts().sort_index())
decades = (dt["decade"].value_counts().sort_index())
topDirector = (dt["director"].value_counts().head(10))
topGenres = (dt["listed_in"].value_counts().head(10))

#Visualization
#Movie VS tv shows
contentType.plot(kind="bar",color="skyblue", edgecolor="black")
plt.title("Movie VS TV Shows",fontweight="bold")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.show()

#Netfix Growth over years
yearlyGrowth.plot(kind="line",marker="o")
plt.title("Netflix Content Added Over Years", fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Titles Added")
plt.grid()
plt.show()

#Top Countries
topCountries.plot(kind="barh",color="pink",edgecolor="black")
plt.title("Top Countries Producing Netflix Content",fontweight="bold")
plt.xlabel("Number of Titles")
plt.show()

#Rating Distribution
ratings.plot(kind="bar",color ="yellow",edgecolor= "black")
plt.title("Netflix Content Ratings",fontweight="bold")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

#Top Genres
topGenres.plot(kind="bar",color="pink",edgecolor="black")
plt.title("Most Popular Netflix Genres",fontweight="bold")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.show()

#Release Year Distribution
plt.hist(dt["release_year"],bins=20)
plt.title("Release Year Distribution",fontweight="bold")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.show()

#Content Age Distribution
plt.hist(dt["content_age"],bins=20, color="skyblue")
plt.title("Content Age Distribution",fontweight="bold")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

#Decade Distribution
decades.plot(kind="bar",color="orange",edgecolor="black")
plt.title("Content by Decade",fontweight="bold")
plt.xlabel("Decade")
plt.ylabel("Number of Titles")
plt.show()

#Final Insights
print("="*60)
print("NETFLIX DATA ANALYSIS - KEY INSIGHTS")
print("="*60)

print(
    f"1. Netflix has more "
    f"{contentType.idxmax()} content."
)

print(
    f"2. The country producing the most content is "
    f"{topCountries.index[0]}."
)

print(
    f"3. The most common rating is "
    f"{ratings.idxmax()}."
)

print(
    f"4. Netflix added the most content in "
    f"{yearlyGrowth.idxmax()}."
)

print(
    f"5. The most active decade is "
    f"{decades.idxmax()}s."
)

print(
    f"6. Average content age is "
    f"{round(dt['content_age'].mean(),2)} years."
)

print(
    f"7. Most recent content release year is "
    f"{dt['release_year'].max()}."
)

print(
    f"8. Oldest content release year is "
    f"{dt['release_year'].min()}."
)