# Monte Carlo Option Pricing vs Black-Scholes Formula

This project prices European call and put options
using Monte Carlo simulation under a Geometric Brownian Motion.
Comparing the call price with the price given by the Black-Scholes Formula

## Model
The stock price follows:
dS_t = r S_t dt + σ S_t dW_t

## Methodology
- Simulate price paths using GBM
- Compute option payoff at maturity
- Discount expected payoff at risk-free rate
- Obtain the price of the call using MCS
- Obtain the price of the call using BS

## Technologies
- Python
- NumPy
- matplotlib

## How to run
pip install -r requirements.txt    
python src/monte_carlo.py
