import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("netflix_titles.csv")
df=df.dropna(subset=['type','release_year','rating','country','duration'])
type_count=df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_count.index,type_count.values,color=["orange","lightblue"])
plt.xlabel("types")
plt.ylabel("values")
plt.title("Number of movies vs tv show")
plt.tight_layout()
plt.savefig("compare_of_movies_and_tvshows.png")
plt.show()


rating_count=df['rating'].value_counts()
plt.figure(figsize=(10,6))
plt.pie(rating_count,labels=rating_count.index,autopct='%1.1f%%',startangle=90)
plt.title("Percentage of content rating ")
plt.tight_layout()
plt.savefig("content_rating.png")
plt.show()

movie = df[df["type"] == "Movie"].copy()

movie["duration_int"] = (
    movie["duration"]
    .str.replace(" min", "", regex=False)
    .astype(float)
)

plt.figure(figsize=(8, 4))
plt.hist(movie["duration_int"].dropna(), bins=30, color="skyblue", edgecolor="black")

plt.title("Duration of Movies")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")

plt.tight_layout()
plt.savefig("duration_view_histogram_chart.png")
plt.show()



release_count = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_count.index, release_count.values, color="red")

plt.title("Release Year and TV Shows")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")

plt.tight_layout()
plt.savefig("Releasing_year_and_tvshow.png")
plt.show()

country_count=df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index,country_count.values,color="teal")
plt.title("Top 10 country by the show")
plt.xlabel("Number of shows")
plt.ylabel("Country")

plt.tight_layout()
plt.savefig("Top_10_countries.png")
plt.show()

content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Movies
ax[0].plot(
    content_by_year.index,
    content_by_year['Movie'],
    color='red'
)
ax[0].set_title("Movies Released per Year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of Movies")

# TV Shows
ax[1].plot(
    content_by_year.index,
    content_by_year['TV Show'],
    color='orange'
)
ax[1].set_title("TV Shows Released per Year")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Number of TV Shows")

fig.suptitle("Comparison of Movies and TV Shows Released Over the Years")

plt.tight_layout()
plt.savefig("Comparing_the_tvshow_and_movies.png")
plt.show()