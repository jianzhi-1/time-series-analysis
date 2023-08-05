x = np.random.normal(0, 1, 100)
sm.tsa.stattools.adfuller(x, maxlag=None, regression='c', autolag='AIC', store=False, regresults=False)
# https://www.statsmodels.org/dev/generated/statsmodels.tsa.stattools.adfuller.html
# the first number is the test statistic (more negative -> more likely time series is stationary)
# the second number is p value
