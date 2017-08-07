# Keeps track of user defined R functions
# Loads them for use in the local directory at startup
# Version 07/16/2017
# Author Gloire Rubambiza

# Plots the available bandwith for a given day
plottb <- function(x, y){
  
  data <- read.csv(x)
  linear_model <- lm(data$High.ABW~data$Time)
  plot(data$Time, data$High.ABW, pch = 20, main = y,  
       xlab = "Time of day", ylab = "Megabits/second", col.main = "blue", 
       col = "orange", cex.axis = 1.1, cex.lab = 1.2)
  abline(a=coef(linear_model), b=1, col="blue", lwd = 2)
}

# Plots the bandwidth for LANS presentation
plottbp <- function(x, y){
  
  data <- read.csv(x)
  linear_model <- lm(data$High.ABW~data$Time)
  plot(data$Time, data$High.ABW, pch = 20, main = y,  
       xlab = "Time of day", ylab = "Mbps", col.main = "blue", 
       col = "orange", cex.axis = 1.6, cex.lab = 2.0, cex.main = 3.0)
  abline(a=coef(linear_model), b=1, col="blue", lwd = 2)
}


# Plots the available bandwidth for Google cloud experiments
plottbc <- function(x, y){
  data <- read.csv(x)
  linear_model <- lm(data$High.ABW~data$Time)
  plot(data$Time, data$High.ABW, pch = 20, main = y, 
  xlab = "Time of day", ylab = "Megabits/second", col.main = "blue", 
        col = "orange", cex.axis = 1.2, cex.lab = 1.2)
  abline(a=coef(linear_model), b=1, col="orange", lwd = 2)
}

plotIPD <- function(x, y){
  
  data <- read.csv(x)
  plot(data$Hop.IP, data$Duration, pch = 20, xlab = "Hop IP", ylab = "Latency (milliseconds)",
  col.main = "blue", col = "darkorange", main = y, cex.axis = 1.1, cex.lab = 1.2 )
}

# Plots latency for LANS presentation
plotIPDP <- function(x, y){
  
  data <- read.csv(x)
  plot(data$Hop.IP, data$Duration, pch = 20, xlab = "Intermediate Host",
  ylab = "Latency (ms)", col.main = "blue", col = "black", main = y,
  cex.axis = 1.6, cex.lab = 2.0, cex.main = 3.0 )
}

histDuration <- function(x, y){
  data <- read.csv(x)
  hist(data$Duration, xlab = "Latency (milliseconds(Singapore)",
  col = "darkorange", main = y, breaks = 15, col.main = "blue", cex.axis = 1.1,
  cex.lab = 1.2, xlim=c(0,1000))

}

# Plots traceroute histogram for LANS presentation
histDurationP <- function(x, y){
  data <- read.csv(x)
  hist(data$Duration, xlab = "Latency (ms)", col = "darkorange",
  main = y,breaks = 15, col.main = "blue", cex.axis = 1.6, cex.lab = 2.0,
  cex.main = 3.0, xlim=c(0,1000))

}

# Plots available bandwidth histograms for different experiments
histBWJ <- function(x, y){
  data <- read.csv(x)
  hist(data$High.ABW, xlab = "Bandwidth Estimate(Mbps)", col = "darkorange", main = y,
       breaks = 10, col.main = "blue", xlim=c(600,2000), cex.axis = 1.2,
       cex.lab = 1.2)

}

histBWS <- function(x, y){
  data <- read.csv(x)
  hist(data$High.ABW, xlab = "Bandwidth Estimate(Mbps)", col = "darkorange", main = y,
       breaks = 10, col.main = "blue", xlim=c(180,280), cex.axis = 1.2, 
        cex.lab = 1.2)

}

histBWL <- function(x, y){
  data <- read.csv(x)
  hist(data$High.ABW, xlab = "Bandwidth Estimate(Mbps)", col = "darkorange", main = y,
       breaks = 10, col.main = "blue", xlim=c(400,1000), cex.axis = 1.2, 
       cex.lab = 1.2)

}

# Distribution for presentations
histBWJP <- function(x, y){
  data <- read.csv(x)
  hist(data$High.ABW, xlab = "Bandwidth Estimate(Mbps)", col = "darkorange", main = y,
       breaks = 10, col.main = "blue", xlim=c(600,2000), cex.axis = 1.6,
       cex.lab = 2.0, cex.main = 3.0)

}

histBWLP <- function(x, y){
  data <- read.csv(x)
  hist(data$High.ABW, xlab = "Bandwidth Estimate(Mbps)", col = "darkorange", main = y,
       breaks = 10, col.main = "blue", xlim=c(400,1000), cex.axis = 1.6, 
       cex.lab = 2.0, cex.main = 3.0)

}

# Produces a confidence interval for each server's bandwidth for the entire data collection
# Code help obtained from http://www.cyclismo.org/tutorial/R/confidence.html
bwac <- function(x,y){
  data <- read.csv(x)
  b_mean <- mean(data$High.ABW)
  n_sample <- length(data$High.ABW)
  s_dev <- sd(data$High.ABW)
  error <- qt(0.975 , df = n_sample-1) * s_dev / sqrt(n_sample)
  lower_bound <- b_mean - error
  upper_bound <- b_mean + error
  limits <- c(lower_bound, upper_bound)
  limits
}

# Produces a confidence interval for each server's traceroute for the entire data collection
# Code help obtained from http://www.cyclismo.org/tutorial/R/confidence.html
lac <- function(x){
  data <- read.csv(x)
  b_mean <- mean(data$Duration)
  n_sample <- length(data$Duration)
  s_dev <- sd(data$Duration)
  error <- qt(0.975 , df = n_sample-1) * s_dev / sqrt(n_sample)
  lower_bound <- b_mean - error
  upper_bound <- b_mean + error
  limits <- c(lower_bound, upper_bound)
  limits
}
