file = open("poptrend.txt","w",)
#write poptrend data onto a textfile 
for line in open('felidae_file'):
    rec = line.strip()
    if rec.startswith('Pop'):
        file.write(line)

        file.close()
#get number of each trend
file = open(r"poptrend.txt", "r", encoding="utf-8-sig")
from collections import Counter

wordcount = Counter(file.read().split())

for item in wordcount.items(): print("{}\t{}".format(*item))

file.close()

#create bar graph in R
poptrend=c(2,5,30)
colors=c("blue", "green", "red")
barplot(poptrend, main="Population Trend of Felidae", 
        xlab="Population Trend", ylab="# Species",names.arg=c("Unknown","Stable","Decreasing"), col=colors)
