def E(x, y, lag=0): # given two series x, y, calculate E[XY] (reflective of Pearson's coefficient since E[X], E[Y], sigma_X, sigma_Y assumed to be fixed
    assert len(x) == len(y)
    xlag, ylag = None, None
    if lag >= 0:
        xlag = x[lag:]
        ylag = y[:len(y) - lag]
    else:
        ylag = y[-lag:]
        xlag = x[:len(x) + lag]
    assert len(xlag) == len(ylag)
    assert len(xlag) > 10 # ensure you have enough data to get an accurate coefficient in the first place
    return np.dot(xlag, ylag)/len(xlag)