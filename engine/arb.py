"""Core arbitrage detection."""
from dataclasses import dataclass

@dataclass
class Quote:
    chain: str
    price: float
    fee: float

def spread(a: Quote, b: Quote) -> float:
    return (a.price - b.price) / min(a.price, b.price) - (a.fee + b.fee)

def find_opportunity(quotes: list) -> list:
    out = []
    for i in range(len(quotes)):
        for j in range(i + 1, len(quotes)):
            s = spread(quotes[i], quotes[j])
            if abs(s) > 0.005:
                out.append({"between": (quotes[i].chain, quotes[j].chain), "spread": s})
    return out
