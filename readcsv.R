
getwd()
futures <- read.csv(file="futures.csv",head=TRUE,sep=",")
names(futures)

date <- futures['date']
taiex <- futures['taiex']
price <- futures['price']


#漲跌幅
len <- nrow(price)
previous<-data.frame(c(NA, price[1:len-1,]))
diffp<-price - previous
ptag<-ifelse(diffp[,]>0, "漲", "跌")

#價差
difft <- price -taiex
ttag <- ifelse(difft[,] > 0, "正","逆")

#法人
comp <- (futures['CompBull'] - futures['CompBear']) / futures['CompBear']
#top5
top5 <- (futures['t5Bull'] - futures['t5Bear']) / futures['t5Bear']
top5
#top10
top10 <- (futures['t10Bull'] - futures['t10Bear']) / futures['t10Bear']
top10

#results
data <- futures['date']
data[,'contract'] <- futures['contract']
data[,'price'] <- futures['price']
data[,'ptag'] <- ptag
data[,'diffp'] <-diffp
data[,'ttag'] <- ttag
data[,'difft'] <- difft
data[,'comp'] <- comp
data[,'top5'] <- top5
data[,'top10'] <- top10

data

#plot: date/price
x<-c(1:nrow(futures))
y<-data[,'price']
plot(x, y,main="futures", type="l")
#plot: date/comp
y<-data[,'comp']
plot(x, y,main="Company", type="l")
#plot: date/top5
y<-data[,'top5']
plot(x, y,main="Top5", type="l")
#plot: date/top10
y<-data[,'top10']
plot(x, y,main="Top10", type="l")

