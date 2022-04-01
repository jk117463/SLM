### cleaning
rm(list = ls())
library(R.utils)


# Download source files from URL into and create download sub-directory on 1st run only.
url <- "https://database.lichess.org/lichess_db_puzzle.csv.bz2"
destfile <- "./download/puzzles.csv.bz2"

if(!file.exists("./download/puzzles.csv.bz2")) {
  dir.create("./download")  
  download.file(url,destfile=destfile)
}

puzzles <- read.csv(bzfile(destfile))
head(puzzles)
