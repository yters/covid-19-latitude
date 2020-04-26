c2c <- read.table('coronavirus_coordinates.txt')
png('coronavirus_hemisphere.png')
sig <- c2c[,3]>500
x<-c2c[sig,2]
y<-c2c[sig,4]/c2c[sig,3]
plot(x,y,xlab="Latitude (cases > 500)",ylab="Death Rate (deaths/cases)")
fit <- lm(y ~ x + I(x^2))
lines(sort(x), fitted(fit)[order(x)], col='red', pch=20)
title("Hemisphere Effect on Coronavirus Death Rate")
tmp <- dev.off()
