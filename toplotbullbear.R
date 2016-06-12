getwd()

#大台
unclosed_TXF <- read.csv(file="unclosed_TXF.csv",head=TRUE,sep=",")
#小台
unclosed_MXF <- read.csv(file="unclosed_MXF.csv",head=TRUE,sep=",")

foreign<-c('foreign_bear','foreign_bull')
dealer<-c('dealer_bear','dealer_bull')
trust<-c('trust_bear','trust_bull')
cols <- c('darkseagreen','pink')

columns<-foreign
dataframe<-unclosed_TXF
plotname<-'futures:TX'

#加權指數
taiex <- read.csv(file="taiex.csv",head=TRUE,sep=",")
names(taiex)
ylims<-c(min(taiex[,'price']), max(taiex[,'price']))
x<-c(1:nrow(taiex))
y<-taiex[, 'price']
plot(x, y, type="l", xaxt="n", xlab="time", ylab="price", ylim=ylims2)
axis(1, at=x, labels=taiex[, 'date'])

#description
legend(x=1, y=max(taiex[,'price']), bty="n"
       , legend=c('taiex','amount', columns)
       , col=c('black','grey', cols)
       , lwd=c(1,1,1,1,1))

#大台
futures_TX <- read.csv(file="futures_TX.csv",head=TRUE,sep=",")
names(futures_TX)
par(new=T)
y<-futures_TX[,'price']
plot(x, y, type="l", axes=F, ylab="", xlab="", col="green", lwd=1, ylim=ylims)
##成交量
par(new=T)
y<-futures_TX[,'amount']
plot(x, y, type="h", axes=F, ylab="", xlab="", col="dimgrey", lwd=1)

#小台
futures_MTX <- read.csv(file="futures_MTX.csv",head=TRUE,sep=",")
names(futures_MTX)
par(new=T)
y<-futures_MTX[,'price']
plot(x, y, type="l", axes=F, ylab="", xlab="", col="cornflowerblue", lwd=1, lty=2, ylim=ylims)
##成交量
par(new=T)
y<-futures_MTX[,'amount']
plot(x, y, type="h", axes=F, ylab="", xlab="", col="grey", lwd=2)



maxs<-c()
len<-length(columns)
for(i in 1:len){
  tmp <- max(dataframe[,columns[i]])
  maxs<-c(maxs, tmp)
}
ylims<-c(0,max(maxs))

plot_unclosed<-function(name, dataframe, columns, colors){
  for(i in 1:len){
    y<-dataframe[, columns[i]]
    par(new=T)
    plot(x, y, type="l", axes=F, ylab="", xlab="", col=colors[i], main=name, ylim=ylims)
    par(new=T)
    plot(x, y, type="h", axes=F, ylab="", xlab="", col=colors[i], ylim=ylims)
  }
}

plot_unclosed(plotname, dataframe, columns, cols)