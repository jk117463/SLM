import bz2
import os
import pandas
from urllib.request import urlopen
import matplotlib.pyplot as plt
import statistics as stat
from statsmodels.nonparametric.smoothers_lowess import lowess as lowess


#Loading Data
url = "https://database.lichess.org/lichess_db_puzzle.csv.bz2"
bz2_filename = "puzzles.csv.bz2"
header = ["PuzzleId", "FEN", "Moves",
          "Rating", "RatingDeviation",
          "Popularity", "NbPlays",
          "Themes", "GameUrl"]

final_filename = "puzzles.csv"
if os.path.isfile(bz2_filename):
    print("File {} was already downloaded. Proceeding with decompress...".format(bz2_filename))

else:
    print("Downloading the file {}  from url {}".format(bz2_filename, url))

    with urlopen(url) as data, open(bz2_filename, "wb") as file:
        file.write(data.read())
    print("{} Download complete! Proceeding with decompress...".format(bz2_filename))

if os.path.isfile(final_filename):
    print("File was already decompressed into {}".format(final_filename))

else:
    with bz2.open(bz2_filename, "rt") as filefrom, open(final_filename, "w") as fileto:
        fileto.write(filefrom.read())
    print("{} successfully decompressed into {}!".format(bz2_filename, final_filename))
puzzles = pandas.read_csv(final_filename, names = header)


#Defining Limits
plays_median = stat.median(puzzles.NbPlays)
rating_low_cutoff = 1500
rating_high_cutoff = stat.quantiles(data=puzzles.Rating, n=100)[98]

#Filtered Dataset
puzzles_transformed = puzzles[(puzzles.Rating > rating_low_cutoff) & (puzzles.Rating < rating_high_cutoff) & (puzzles.NbPlays > plays_median)]
final = puzzles_transformed[["Rating", "Popularity"]]

ratings_dict = {}


for (i, rating) in enumerate(final.Rating):
    if rating in ratings_dict.keys():
        ratings_dict[rating].append(i)
    else:
        ratings_dict[rating] = [i]

ratings = final.Rating.unique()

#Creating mean popularities
mean_popularities = []

for rating in ratings:
    indices = ratings_dict[rating]
    popularities = final.iloc[indices, final.columns.get_loc("Popularity")]
    mean_popularities.append(stat.mean(popularities))

#Lowess
l_y, l_x = lowess(ratings, mean_popularities, frac=1/4).T

#plots
plt.scatter(x = ratings, y = mean_popularities, color= "black")
plt.plot(l_x, l_y, color="blue")
plt.xlabel('Ratings')
plt.ylabel('Mean Popularity')
plt.show()