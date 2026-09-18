
plot_histograms <- function(df) {
  par(mfrow = c(2, 2))
  hist(df$Sepal.Length, main = "Sepal Length", col = "lightblue")
  hist(df$Sepal.Width, main = "Sepal Width", col = "lightgreen")
  hist(df$Petal.Length, main = "Petal Length", col = "lightpink")
  hist(df$Petal.Width, main = "Petal Width", col = "lightyellow")
}

plot_boxplots <- function(df) {
  boxplot(Sepal.Length ~ Species, data = df, main = "Sepal Length por especie")
}

plot_scatter <- function(df) {
  plot(df$Petal.Length, df$Petal.Width,
       col = df$Species, pch = 19,
       main = "Petal Length vs Petal Width",
       xlab = "Petal Length", ylab = "Petal Width")
  legend("topleft", legend = levels(df$Species), col = 1:3, pch = 19)
}

data(iris)
plot_histograms(iris)
plot_boxplots(iris)
plot_scatter(iris)