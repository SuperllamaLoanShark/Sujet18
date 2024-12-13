import numpy
import mp
import matplotlib
tau = 2
T = 20
N = 1000
y0 = 2
'''
def derive(y):
    return ((1372*(y**2))-(7889*(y**2))+(9219*y)-2610)
    if t<T/2:
        g = 10
    else:
        g=6
    return (g-y)/Tau

def euler(derive, y0, t):
    h = t[1]-t[0]
    N = len(t)
    y = numpy.zeros(N)
    y[0] = y0
    for n in range(0, N-1):
        y[n+1] = y[n] + h*derive(y[n], t[n])
    return y
'''
def y(y0, h, t_max):
    def derive(y):
        return ((1372*(y**2))-(7889*(y**2))+(9219*y)-2610)
    h = abs(t_max[1] - t_max[0])
    N = len(t_max)
    y_t = numpy.zeros(N)
    y_t[0] = y0
    for n in range(0, N-1):
        y_t[n+1] = y[n] + h*derive(y[n], t[n])
    mp.dps =6
    return mp(y_t)

t_max = numpy.linspace(0,T,N)
h = abs(t_max[1] - t_max[0])
#y = y(derive, y0, t)
y_t= y(y0, h, t_max)


def plot(h, y_tab):
    matplotlib.plot(t,y, ".", ms = 2, label='y(t) pour N={}', format(N))
    matplotlib.legend()
    matplotlib.xlabel('t')
    matplotlib.ylim(0, 12)
    matplotlib.grid()
    matplotlib.show()

def conv(h, k):
    temp = 10**(-k)
    N=1
    while abs(y(N) - h) >= temp:
        N += 1
    return N

def main():
    #mp.dps = 6
    plot()
    y()