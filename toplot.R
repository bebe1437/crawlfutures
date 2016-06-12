getwd()

#加權指數
taiex <- read.csv(file="taiex.csv",head=TRUE,sep=",")
names(taiex)
x<-c(1:nrow(taiex))
y<-taiex[, 'price']
plot(x, y, type="l", xaxt="n", xlab="time", ylab="price")
axis(1, at=x, labels=taiex[, 'date'])

#大台
futures_TX <- read.csv(file="futures_TX.csv",head=TRUE,sep=",")
names(futures_TX)
par(new=T)
y<-futures_TX[,'price']
plot(x, y, type="l", axes=F, ylab="", xlab="", col="green", lwd=1)
##成交量
par(new=T)
y<-futures_TX[,'amount']
plot(x, y, type="h", axes=F, ylab="", xlab="", col="dimgrey", lwd=1)

#小台
futures_MTX <- read.csv(file="futures_MTX.csv",head=TRUE,sep=",")
names(futures_MTX)
par(new=T)
y<-futures_MTX[,'price']
plot(x, y, type="l", axes=F, ylab="", xlab="", col="cornflowerblue", lwd=1, lty=2)
##成交量
par(new=T)
y<-futures_MTX[,'amount']
plot(x, y, type="h", axes=F, ylab="", xlab="", col="grey", lwd=2)

plot_unclosed<-function(name, dataframe, columns, colors){
  len<-length(columns)
  for(i in 1:len){
    print(columns[i])
    y<-dataframe[, columns[i]]
    par(new=T)
    plot(x, y, type="l", axes=F, ylab="", xlab="", col=colors[i], main=name)
    par(new=T)
    plot(x, y, type="h", axes=F, ylab="", xlab="", col=colors[i])
  }
  #description
  legend(x=1, y=max(y), bty="n"
         , legend=c('taiex','amount', columns)
         , col=c('black','grey', colors)
         , lwd=c(1,1,1,1,1))
}

bull <- c('dealer_bull','trust_bull','foreign_bull')
bear <- c('dealer_bear','trust_bear','foreign_bear')
cols <- c('blue','pink','darkseagreen')
#大台
unclosed_TXF <- read.csv(file="unclosed_TXF.csv",head=TRUE,sep=",")
#plot_unclosed("futures:TX", unclosed_TXF, bear, cols)
#小台
unclosed_MXF <- read.csv(file="unclosed_MXF.csv",head=TRUE,sep=",")
plot_unclosed("futures:MTX", unclosed_MXF, bear, cols)

