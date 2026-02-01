import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc

#Variables
T = 252 #Trading days
n_steps = 1/ T 
r = 0.05 #risk free rate as effective rate
r_c = np.log(1+r) #risk free rate as a compounded rate
sigma = 0.2 #Standard deviation must be annual
stock_0 = 100 #Initial price of the stock
strike_p = 100 #The option is at the money
n_paths = 3000 #Number of paths we are going to simulate

#Functions

def simulate_stock_price (r_c, sigma, S0, n_steps, T): 
    Z = np.random.normal(0, 1, size=T)
    stock_price = np.empty(T+1)
    stock_price[0] = S0
    drift = (r_c - (0.5 * (sigma**2))) * n_steps
    diffusion = sigma * np.sqrt(n_steps)
    for i in range (1,T+1):
        stock_price[i] = stock_price[i-1] * np.exp(drift + (diffusion * Z[i-1]) )
    return stock_price

def Monte_Carlo(n_paths, r_c, sigma, S0, T, n_steps):
    paths = np.empty((n_paths, T+1))
    for j in range (0,n_paths):
        paths[j,:] = simulate_stock_price(r_c, sigma, S0,  n_steps,T)
    return paths

def Pricing (s_price, strike, r_c, T,n_steps):
    ST = s_price[:, -1]
    payoff = np.maximum(ST- strike, 0.0)
    disc = np.exp(-r_c * T*n_steps)
    call_price = disc * payoff.mean()
    return call_price

def Black_Scholes(s_price_0, strike, r_c,sigma, T, n_steps,):
    d1 = ( np.log((s_price_0)/(strike)) + ((r_c + ((sigma**2)/2)) *(T*n_steps))) / (sigma* ((T*n_steps)**0.5))
    d2 = d1 - (sigma * ((T*n_steps)**0.5))
    call = (s_price_0 * sc.norm.cdf(d1)) - (strike * np.exp(-r_c*(T*n_steps)) * sc.norm.cdf(d2))
    return call


#Code
MCS = Monte_Carlo(n_paths, r_c, sigma, stock_0, T, n_steps)
call = Pricing(MCS,strike_p,r_c,T,n_steps)
call_BS = Black_Scholes(stock_0,strike_p,r_c,sigma,T,n_steps)
dif = call -call_BS

print(f"The call using MCS is {call} and the call using BS is {call_BS} and the difference is {dif}")