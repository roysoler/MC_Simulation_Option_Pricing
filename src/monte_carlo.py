import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Variables
t = 252 #Trading days
dt = 1/ t 
r = 0.05 #risk free rate as effective rate
r_c = np.log(1+r) #risk free rate as a compounded rate
variance = 0.02 
stock_0 = 100 #Initial price of the stock
strike_p = 100 #The option is at the money
n_paths = 2000 #Number of paths we are going to simulate

#Functions

def simulate_stock_price (r, variance, S0, t, dt): 
    Z = np.random.normal(0, 1, size=t)
    stock_price = np.empty(t+1)
    stock_price[0] = S0
    drift = (r - (0.5 * variance)) * dt
    diffusion = np.sqrt(variance) * np.sqrt(dt)
    for i in range (1,t+1):
        stock_price[i] = stock_price[i-1] * np.exp(drift + (diffusion * Z[i-1]) )
    return stock_price

def Monte_Carlo(n_paths, r, variance, S0, t, dt):
    paths = np.empty((n_paths, t+1))
    for j in range (0,n_paths):
        paths[j,:] = simulate_stock_price(r, variance, S0, t, dt)
    return paths

def Pricing (s_price, strike, r, t,dt):
    ST = s_price[:, -1] 
    payoff = np.maximum(ST- strike, 0.0)
    call_price = np.exp(-r * t*dt) * np.mean(payoff)
    return call_price

#Code
MCS = Monte_Carlo(n_paths, r_c, variance, stock_0, t, dt)
call = Pricing(MCS,strike_p,r_c,t,dt)