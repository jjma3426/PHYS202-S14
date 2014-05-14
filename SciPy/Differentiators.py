def fourPtCenteredDiff(x,y):
    """This algorithm uses a higher order differencing method to approximate the slope of the line. It finds the slope
    by checking the difference in dy versus dx from the center of the center of dx for 4 points of slices of the array."""
    dydx = np.zeros(y.shape,float) 
    dydx[2:-2] = (y[:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:])/(12*(x[2]-x[1]))
    dydx[1] = (y[2]-y[1])/(x[2]-x[1]) 
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) 
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) 
    dydx[-2] = (y[-2] - y[-3])/(x[-2] - x[-3]) 
    return dydx

def twoPtForwardDiff(x,y):
    """This approximation method the same lower order approximation as the Two Point Center Function but it find the difference
    of the y points,dy, from the right most point of dx rather than the center."""
    dydx = np.zeros(y.shape,float) 
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[1]-y[0])/(x[1]-x[0])
    return dydx

def twoPtCenteredDiff(x,y):
    """This algorithm is like the Four Point Centered Difference function but it only does that approximation for two points
    or two slices of the array based on a lower order approximation."""
    dydx = np.zeros(y.shape,float) 
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) 
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) 
    return dydx

x = np.arange(0.,10.0,0.02)
y = 8*x**4 + 3*x

dydx4 = fourPtCenteredDiff(x,y)
dydx2c = twoPtCenteredDiff(x,y)
dydx2f = twoPtForwardDiff(x,y)

plt.plot(x, dydx4, label='Four Point Approximation')
plt.plot(x, dydx2c, label='Two Point Approximation(Centered)')
plt.plot(x, dydx2f, label='Two Point Approximation (Forward)')
plt.plot(x, dydxE, label='Exact')
plt.legend(loc='upper left')
plt.show()