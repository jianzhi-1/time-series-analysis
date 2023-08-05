def E(x, y, lag=0, lim=10): # given two series x, y, calculate E[XY] (reflective of Pearson's coefficient since E[X], E[Y], sigma_X, sigma_Y assumed to be fixed
    assert len(x) == len(y)
    xlag, ylag = None, None
    if lag >= 0:
        xlag = x[lag:]
        ylag = y[:len(y) - lag]
    else:
        ylag = y[-lag:]
        xlag = x[:len(x) + lag]
    assert len(xlag) == len(ylag)
    assert len(xlag) > lim # ensure you have enough data to get an accurate coefficient in the first place
    return np.dot(xlag, ylag)/len(xlag)

def plotE(x, y, maxlag=40, lim=10):
    lag_arr = np.arange(-maxlag, maxlag, 1)
    res = [E(x, y, lag=lag, lim=10) for lag in lag_arr]
    plt.plot(lag_arr, res, label="E[XY]")
    plt.legend()
    plt.show()
