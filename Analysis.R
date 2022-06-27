### Purpose is to learn about what influences 'wins' via data exploration
#Reading in data
install.packages("readxl")
library("readxl")
data <- read_excel("C:\\Users\\airin\\Desktop\\football\\python-data-soccer\\finalDataFrame.xlsx")

#Basic Summary Stats
summary(data)
names(data)
head(data)
dim(data)

#Specific Variable Insights
summary(data$wins)
hist(data$wins, main = "Histogram of Wins", xlab = "Wins")

summary(data$goals)
hist(data$goals, main = "Histogram of Goals", xlab = "Goals")

summary(data$passes_completed_short)
hist(data$passes_completed_short, main = "Histogram of Short Passes", xlab="Short Passes")

plot(x = data$goals, y = data$wins, xlab = "Goals", ylab="Wins", main = "Goals x Wins")
plot(x = data$passes_completed, y = data$wins, xlab = "Passes Completed", ylab="Wins", main = "Passes Completed x Wins")
plot(x = data$shots_total_per90, y = data$wins, xlab = "ShotsPer90", ylab="Wins", main = "ShotsPer90 x Wins")
plot(x = data$average_shot_distance, y = data$wins, xlab = "AvgShotDistance", ylab="Wins", main = "AvgShotDistance x Wins")
plot(x = data$average_shot_distance, y = data$goals, xlab = "AvgShotDistance", ylab="Goals", main = "AvgShotDistance x Goals")
