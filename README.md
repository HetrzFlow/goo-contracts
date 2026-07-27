# Stock Token Arbitrage

[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Chains](https://img.shields.io/badge/Chains-RH%20%7C%20BSC%20%7C%20EVM-lightgrey)](configs/)

**One price, three chains, capture the drift**

Cross-chain arbitrage engine for stock tokens across Robinhood Chain, BSC and EVM: price discovery, spread detection, execution and risk limits.

## Quick start

```bash
git clone https://github.com/cervemone/stock-token-arbitrage.git
cd stock-token-arbitrage
pip install -r requirements.txt   # or: npm install
python -m src.main --help
```

## Layout

```
  engine/
  feeds/
  execution/
  risk/
  tests/
  docs/
  scripts/
  configs/
  examples/
  benchmarks/
  integrations/
  research/
```

## Related

- `stock-token-index` — the registry this repo builds on
- `stock-analyst-agent` — the agent that consumes this data
- `rh-stock-token-sdk` — SDK for Robinhood Chain stock tokens

## License

MIT
