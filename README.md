# Monte Carlo Option Pricing

This project prices European call and put options
using Monte Carlo simulation under a Geometric Brownian Motion.

## Model
The stock price follows:
dS_t = r S_t dt + σ S_t dW_t

## Methodology
- Simulate price paths using GBM
- Compute option payoff at maturity
- Discount expected payoff at risk-free rate

## Technologies
- Python
- NumPy
- matplotlib

## How to run
pip install -r requirements.txt
python src/MonteCarloSimulation.ib
