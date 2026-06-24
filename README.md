# LoneStarOracle MCP Server

38 AI data tools for Claude and any MCP-compatible agent — crypto, DeFi, equities, commodities, energy, real estate, government intelligence, security audits, and more.

**Published on the official MCP registry:** `xyz.lonestaroracle/mcp-server`

[![Glama](https://glama.ai/mcp/servers/Homie4570/lso-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Homie4570/lso-mcp)

## Tools (38)

### Crypto & Blockchain
| Tool | Description |
|------|-------------|
| `token_due_diligence` | ERC-20 risk score, honeypot check, liquidity, holder concentration |
| `wallet_risk` | Wallet risk scoring — transaction patterns, exposure, risk flags |
| `contract_check` | Smart contract verification and security analysis |
| `chainscout_intelligence` | Whale transfers ($5M+), trending tokens, DeFi TVL movements |
| `whale_alert` | Real-time whale wallet tracking above a USD threshold |
| `token_launches` | Newly launched token scanner — risk score, liquidity, deployer history |
| `defi_risk` | DeFi protocol risk — TVL, audit status, exploit history |
| `cascade_watch` | DeFi liquidation cascade risk — systemic risk chain detection |
| `stablecoin_pulse` | Stablecoin health — peg deviation, collateral ratio, depeg risk |

### Equities & Markets
| Tool | Description |
|------|-------------|
| `equity_analysis` | Stock fundamentals, price, analyst ratings |
| `options_flow` | Unusual options activity and flow data |
| `insider_trading` | SEC Form 4 insider trade filings |
| `portfolio_risk` | Multi-asset portfolio risk scoring |
| `macro_indicators` | GDP, CPI, Fed rates, yield curve signals |
| `earnings_calendar` | Upcoming earnings dates and estimates |
| `tech_analysis` | Technical indicators — RSI, MACD, Bollinger Bands |
| `multi_timeframe_scan` | Multi-timeframe technical scan across assets |

### Commodities & Energy
| Tool | Description |
|------|-------------|
| `energy_markets` | Oil, gas, refined products prices and signals |
| `agricultural_commodities` | Corn, wheat, soy, cotton spot and futures |
| `industrial_metals` | Copper, aluminum, steel market data |
| `supply_chain_intelligence` | Supply chain stress signals and disruption alerts |
| `gpu_compute_prices` | GPU compute pricing across cloud providers |
| `grid_intelligence` | US electricity grid demand, generation mix, stress signals |

### Real Estate & Infrastructure
| Tool | Description |
|------|-------------|
| `real_estate_pulse` | Mortgage rates, housing inventory, market indicators |
| `lease_edge` | Commercial lease market intelligence |
| `geo_pulse` | Geopolitical risk scoring by region |
| `gov_edge` | Government procurement and contract intelligence |
| `latam_pulse` | Latin America economic and political risk signals |

### Data & Utilities
| Tool | Description |
|------|-------------|
| `news_sentiment` | News sentiment analysis across topics and tickers |
| `weather_forecast` | Hyperlocal weather forecasts for any location |
| `content_forge` | Repurpose URLs into LinkedIn posts, tweets, newsletters |
| `smart_contract_audit` | EVM smart contract security audit (Solidity) |
| `rust_contract_audit` | Rust/Solana smart contract security audit |
| `move_contract_audit` | Move/Aptos smart contract security audit |
| `staking_yields` | Staking yield rates across protocols and assets |
| `aerocheck_pool` | Aerodrome liquidity pool analysis on Base |
| `pdf_to_markdown` | Convert PDF documents to clean Markdown |
| `hire_floyd` | Hire Floyd AI agent for autonomous research and coding tasks |

## Usage

### With Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "lonestaroracle": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.lonestaroracle.xyz/mcp"]
    }
  }
}
```

### With any MCP client

Streamable HTTP endpoint: `https://mcp.lonestaroracle.xyz/mcp`

### Self-hosted (Docker)

```bash
docker build -t lso-mcp .
docker run -e LSO_BASE=https://lonestaroracle.xyz -p 8018:8018 lso-mcp
```

## Links

- **Live endpoint:** https://mcp.lonestaroracle.xyz
- **Full API catalog:** https://lonestaroracle.xyz
- **MCP Registry:** xyz.lonestaroracle/mcp-server
