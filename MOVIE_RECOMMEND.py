import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]


##################################################
print("PREFERRED SEARCH : ")
print("ACTION")
print("1.BATMAN VS SUPERMAN :DAWN OF JUSTICE  2.THE AMAZIMG SPIDER MAN 3.THE WOLVERINE  4.THE HUNTSMAN:WINTER'S WAR")
print("ADVERNTURE")
print("1.LIFE OF PI  2.TOMORROW NEVEER DIES  3.INSURGENT  4.CASINO ROYALE")
print("DRAMA")
print("1.KINGDOM OF HEAVEN  2.THE PATRIOT  3.THE CHRONILES OF NARINA:PRINCE CASPIAN   4.THE WOLF OF WALL STREET")
print("ANIMATION")
print("1.EPIC  2.DINOSAUR  3.TANGLED  4.CARS2")
print("SCIENCE FICTION")
print("1.INTERSTELLAR  3.THE MARTIAN  3.PACIFIC RIM  4.OBLIVION")


movie_user_likes = input("\n\nSEARCH A MOVIE : ")
movie_user_likes = movie_user_likes.title()

df = pd.read_csv("G:\software\movie recommend\movie_dataset.csv")

features = ['keywords' ,'cast', 'genres','director']

for feature in features:
    df[feature] = df[feature].fillna(' ')
def combine_features(row):
    try:
        return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']
    except:
        print("error:",row)
df["combined_features"] = df.apply(combine_features,axis=1)
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)
print("\nSIMILAR TO YOUR SEARCHED MOVIE : ")
movie_index = get_index_from_title(movie_user_likes)
movie_index = get_index_from_title('Epic')
print(movie_index)
similar_movies = list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movies,key = lambda x:x[1],reverse = True)
i=0
for movie in sorted_similar_movies:
    if i>0:
        print(get_title_from_index(movie[0]))
        i = i + 1
        if i > 50:
            break
    else:
        i=i+1
