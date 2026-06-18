"""
LoneStarOracle MCP Server
Exposes 37 LSO data services as Claude tools via Model Context Protocol.
Free access through MCP — full paid API at lonestaroracle.xyz
"""

import os
import httpx
from fastmcp import FastMCP

mcp = FastMCP(
    name="LoneStarOracle",
    instructions=(
        "LoneStarOracle provides 37 AI data tools — crypto, DeFi risk, equities, commodities, energy, "
        "real estate, government intelligence, security audits, stablecoins, whale tracking, and autonomous coding. "
        "Use these tools to get crypto due diligence, DeFi liquidation risk, equity data, energy prices, "
        "real estate rates, agricultural commodities, news sentiment, and more. "
        "All data is live and refreshed continuously."
    )
)

BASE = os.getenv("LSO_BASE", "http://localhost")
TIMEOUT = 15

def _get(url: str, params: dict = None) -> dict:
    try:
        r = httpx.get(url, params=params, timeout=TIMEOUT)
        return r.json()
    except Exception as e:
        return {"error": "Service temporarily unavailable"}


# ── Crypto & Blockchain ───────────────────────────────────────────────────────

@mcp.tool()
def token_due_diligence(contract_address: str, chain: str = "eth") -> dict:
    """Full ERC-20 token due diligence: risk score, honeypot check, liquidity,
    holder concentration, ownership status. Chain: eth, base, bsc, arb, poly."""
    return _get(f"{BASE}:8000/report", {"address": contract_address, "chain": chain})


@mcp.tool()
def wallet_risk(address: str, chain: str = "eth") -> dict:
    """Wallet risk scoring — transaction patterns, exposure, risk flags."""
    return _get(f"{BASE}:8002/score", {"address": address, "chain": chain})


@mcp.tool()
def contract_check(address: str, chain: str = "eth") -> dict:
    """Smart contract verification and security analysis."""
    return _get(f"{BASE}:8003/verify", {"address": address, "chain": chain})


@mcp.tool()
def chainscout_intelligence() -> dict:
    """On-chain intelligence: whale transfers ($5M+), trending tokens by volume,
    DeFi TVL movements on Base and Ethereum. Refreshed every 15 minutes."""
    return _get(f"{BASE}:8012/report")


@mcp.tool()
def whale_alert(min_usd: float = 1000000) -> dict:
    """Real-time whale wallet tracking — large on-chain transfers above threshold.
    Pass min_usd to filter by minimum transfer size (default $1M)."""
    return _get(f"{BASE}:8039/whales", {"min_usd": min_usd})


@mcp.tool()
def token_launches() -> dict:
    """Scan newly launched tokens — filters for legitimate new launches vs. honeypots.
    Returns risk score, liquidity, deployer history, and launch metadata."""
    return _get(f"{BASE}:8037/scan")


@mcp.tool()
def defi_risk(protocol: str = "") -> dict:
    """DeFi protocol risk assessment — TVL, audit status, exploit history, smart contract risk.
    Pass protocol name or leave empty for top protocols overview."""
    params = {"protocol": protocol} if protocol else {}
    return _get(f"{BASE}:8038/risk", params)


@mcp.tool()
def cascade_watch() -> dict:
    """DeFi liquidation cascade risk monitor — tracks collateral-at-risk curves across
    Morpho Blue markets. Returns risk score 1-10, USD exposure at 5/10/20% price drops,
    and AI risk narrative. Critical for assessing systemic DeFi risk."""
    return _get(f"{BASE}:8041/risk")


@mcp.tool()
def stablecoin_pulse(symbol: str = "") -> dict:
    """Stablecoin stability monitoring — peg deviation, backing ratio, mint/burn activity,
    depeg risk score. Pass symbol (USDC/USDT/DAI/FRAX) or leave empty for full report."""
    params = {"symbol": symbol.upper()} if symbol else {}
    return _get(f"{BASE}:8036/pulse", params)


# ── Financial Markets ─────────────────────────────────────────────────────────

@mcp.tool()
def equity_analysis(ticker: str) -> dict:
    """Equity intelligence: buy/hold/sell signal, upside % to analyst target, P/E, EPS, health flags, AI analysis. US stocks and ETFs. Cached 30 min."""
    return _get(f"{BASE}:8005/equity", {"ticker": ticker})


@mcp.tool()
def options_flow(ticker: str) -> dict:
    """Options flow for stocks AND crypto (BTC/ETH/SOL/AVAX via Deribit). Returns signal (bullish/bearish/neutral), conviction trade with USD premium, put/call ratio, unusual activity. Crypto under 1s, stocks cached 5 min."""
    return _get(f"{BASE}:8006/flow", {"ticker": ticker})


@mcp.tool()
def insider_trading(ticker: str) -> dict:
    """SEC Form 4 insider trading data — executive buy/sell transactions."""
    return _get(f"{BASE}:8010/trades", {"ticker": ticker})


@mcp.tool()
def portfolio_risk(tickers: str) -> dict:
    """Portfolio risk analysis — concentration, volatility, correlation.
    Pass tickers as comma-separated string: 'AAPL,MSFT,GOOGL'"""
    return _get(f"{BASE}:8007/analyze", {"tickers": tickers})


@mcp.tool()
def macro_indicators() -> dict:
    """Macro indicators — Fed funds rate, GDP, inflation, yield curve, DXY."""
    return _get(f"{BASE}:8008/macro")


@mcp.tool()
def earnings_calendar(tickers: str = "", days_soon: int = 7) -> dict:
    """Earnings dates, estimates, and beat/miss history. Last 4 quarters: EPS actual/estimate, surprise %, day-after price reaction, consecutive beats. Pass tickers as comma-separated string. days_soon: near-term window in days (default 7, max 90)."""
    params = {"days_soon": days_soon}
    if tickers:
        params["tickers"] = tickers
    return _get(f"{BASE}:8009/calendar", params)


@mcp.tool()
def tech_analysis(symbol: str, timeframe: str = "1d") -> dict:
    """18 technical indicators + AI signal for any ticker. Timeframes: 15m, 1h, 4h, 1d. Cached 5 min."""
    return _get(f"{BASE}:8024/aw/analyze", {"symbol": symbol, "timeframe": timeframe})


@mcp.tool()
def multi_timeframe_scan(symbol: str) -> dict:
    """Multi-timeframe TA confluence across 15m/1h/4h/1d: overall_signal (strong_buy/buy/neutral/sell/strong_sell), confluence_score, bull/bear breakdown, AI narrative. Cached 5 min."""
    return _get(f"{BASE}:8024/aw/scan", {"symbol": symbol})


# ── Energy & Commodities ──────────────────────────────────────────────────────

@mcp.tool()
def energy_markets() -> dict:
    """US energy market intelligence: WTI, Brent, Henry Hub, gasoline, heating oil,
    jet fuel, diesel, propane prices + crude inventory + rig count + basin production."""
    return _get(f"{BASE}:8015/report")


@mcp.tool()
def agricultural_commodities() -> dict:
    """Global agricultural commodity prices: corn, wheat, soybeans, rice, cotton,
    coffee, cocoa, sugar, beef, pork with 6-month trend."""
    return _get(f"{BASE}:8017/report")


@mcp.tool()
def industrial_metals() -> dict:
    """Real-time industrial metals prices — copper, aluminum, steel, lithium, zinc + precious metals with AI narrative."""
    return _get(f"{BASE}:8026/report")


@mcp.tool()
def supply_chain_intelligence() -> dict:
    """Supply chain intelligence — shipping rates, PPI, truck tonnage, manufacturing orders. Stress score 0-10."""
    return _get(f"{BASE}:8027/report")


@mcp.tool()
def gpu_compute_prices() -> dict:
    """Real-time GPU compute spot prices — H100, A100, A10G from Vast.ai, AWS, Lambda Labs."""
    return _get(f"{BASE}:8025/report")


# ── Real Estate ───────────────────────────────────────────────────────────────

@mcp.tool()
def real_estate_pulse() -> dict:
    """US real estate market: 30yr/15yr/ARM mortgage rates with trend, housing starts,
    months supply, Case-Shiller HPI, affordability index."""
    return _get(f"{BASE}:8016/report")


@mcp.tool()
def lease_edge(status: str = "active", area: str = None, limit: int = 20) -> dict:
    """Gulf of Mexico oil & gas lease intelligence from BOEM. 218k+ leases, block status, upcoming BBG2 auction."""
    params = {"status": status, "limit": limit}
    if area:
        params["area"] = area
    return _get(f"{BASE}:8032/report", params)


# ── Grid & Infrastructure ─────────────────────────────────────────────────────

@mcp.tool()
def grid_intelligence(region: str = "") -> dict:
    """US electricity grid intelligence — real-time demand, generation mix (% renewable/gas/nuclear),
    and grid stress signals. Use to optimize when to run industrial operations, charge EV fleets,
    or shift compute workloads to low-cost/clean energy periods.
    Region codes: CISO (California), ERCO (Texas), MISO (Midwest), PJM (Mid-Atlantic),
    NYIS (New York), ISNE (New England), SWPP (Southwest). Leave empty for all regions."""
    if region:
        return _get(f"{BASE}:8019/region/{region.upper()}")
    return _get(f"{BASE}:8019/report")


# ── Geopolitical & Government ─────────────────────────────────────────────────

@mcp.tool()
def geo_pulse(region: str = "") -> dict:
    """Geopolitical risk monitor — conflict zones, sanctions, political instability scores
    by region. Returns risk score 1-10, active hotspots, and commodity impact analysis."""
    params = {"region": region} if region else {}
    return _get(f"{BASE}:8040/risk", params)


@mcp.tool()
def gov_edge(min_amount: float = 10000000, days_back: int = 7, agency: str = None) -> dict:
    """Federal contract awards from USASpending.gov $10M+. Cross-references winning vendors with stock tickers to surface market movers. Returns agency breakdown, award amounts, and AI narrative."""
    params = {"min_amount": min_amount, "days_back": days_back}
    if agency:
        params["agency"] = agency
    return _get(f"{BASE}:8031/report", params)


@mcp.tool()
def gov_edge_opportunities(keyword: str = "", naics: str = "", set_aside: str = "", days_back: int = 7) -> dict:
    """Search active federal contract opportunities from SAM.gov. Returns solicitations with deadlines, urgency flags (<=14 days), agency, NAICS code, set-aside type, and AI BD briefing. Filters: keyword, naics, set_aside (SBA/8A/WOSB/HUBZone/VOSB/SDVOSB)."""
    params = {"days_back": days_back}
    if keyword:
        params["keyword"] = keyword
    if naics:
        params["naics"] = naics
    if set_aside:
        params["set_aside"] = set_aside
    return _get(f"{BASE}:8031/opportunities", params)


@mcp.tool()
def latam_pulse() -> dict:
    """Latin America economic intelligence — BRL, ARS, COP, MXN, CLP currencies, Argentina dolar blue spread."""
    return _get(f"{BASE}:8029/report")


# ── News, Weather & Content ───────────────────────────────────────────────────

@mcp.tool()
def news_sentiment(query: str) -> dict:
    """News sentiment for stocks and crypto. Crypto queries auto-route to native crypto sources; AI synthesizes and returns aggregate_score (-1.0 to +1.0) signal alongside bullish/bearish/neutral."""
    return _get(f"{BASE}:8004/news", {"query": query})


@mcp.tool()
def weather_forecast(city: str, date: str = "", threshold: float = None, direction: str = "greater") -> dict:
    """7-model consensus + 80 ensemble members (GEFS 30 + ECMWF 50) for weather probability.
    When a threshold is given, returns both an empirical probability (direct member count) and
    a blended prob_exceeds (60% empirical / 40% Gumbel). Also returns method_divergence: if
    empirical and Gumbel disagree by >0.15, signal is forced to PASS regardless of spread.
    Also returns: signal (YES/NO/PASS), outlier (which model disagrees most with consensus).
    Coordinates aligned to NWS ASOS stations used by Kalshi/Polymarket for settlement.
    Cities: Chicago, New York, Miami, Houston, Phoenix, Seattle, Denver, Atlanta, Boston, LA.
    direction: 'greater' or 'less'. Cost: $0.02 via x402."""
    params = {"city": city}
    if date:
        params["date"] = date
    if threshold is not None:
        params["threshold"] = threshold
        params["direction"] = direction
    return _get(f"{BASE}:8001/forecast", params)


@mcp.tool()
def content_forge(url: str) -> dict:
    """Transform any URL into LinkedIn post, tweet thread, newsletter section, and SEO summary."""
    try:
        r = httpx.post(f"{BASE}:8013/repurpose", json={"url": url}, timeout=60)
        return r.json()
    except Exception as e:
        return {"error": "Service temporarily unavailable"}


# ── Security Audits ───────────────────────────────────────────────────────────

@mcp.tool()
def smart_contract_audit(source: str = "", github_url: str = "", contract_name: str = "Contract") -> dict:
    """Solidity smart contract security audit powered by RattlerAI (Claude Opus + Slither).
    Detects reentrancy, access control flaws, flash loan vulnerabilities, oracle manipulation,
    integer overflow, MEV exposure, proxy upgrade risks, signature replay, and 20+ other
    vulnerability classes. Slither cross-validates findings to filter false positives.
    Returns a Code4rena-style severity report (Critical/High/Medium/Low) with root cause
    analysis and fix recommendations. Ideal as a pre-deploy sanity check or audit triage.
    Provide Solidity source code or a GitHub URL to a .sol file. Cost: $2.00 via x402."""
    payload = {"contract_name": contract_name}
    if source:
        payload["source"] = source
    if github_url:
        payload["github_url"] = github_url
    try:
        r = httpx.post(f"{BASE}:8020/audit", json=payload, timeout=120)
        return r.json()
    except Exception as e:
        return {"error": "Service temporarily unavailable"}


@mcp.tool()
def rust_contract_audit(source: str = "", github_url: str = "", contract_name: str = "Contract") -> dict:
    """Rust smart contract security audit powered by CottonmouthAI (Claude Opus).
    Auto-detects the framework (CosmWasm, Anchor/Solana, Stellar/Soroban, NEAR) and applies
    targeted checks: unsafe arithmetic, missing account validation, signer privilege escalation,
    PDA seed collisions, CPI reentrancy, storage layout bugs, and integer truncation.
    Returns a severity-graded report (Critical/High/Medium/Low) with root cause analysis
    and recommended fixes. Provide raw Rust source code or a GitHub URL. Cost: $2.00 via x402."""
    payload = {"contract_name": contract_name}
    if source:
        payload["source"] = source
    if github_url:
        payload["github_url"] = github_url
    try:
        r = httpx.post(f"{BASE}:8021/audit", json=payload, timeout=120)
        return r.json()
    except Exception as e:
        return {"error": "Service temporarily unavailable"}


@mcp.tool()
def move_contract_audit(source: str = "", github_url: str = "", contract_name: str = "Contract") -> dict:
    """Move smart contract security audit powered by CopperheadAI (Claude Opus).
    Covers Aptos and Sui. Detects resource leaks, capability confusion, object ownership
    violations, signer abuse, type confusion, missing abort conditions, and privilege
    escalation patterns specific to the Move VM and object model.
    Returns a severity-graded report (Critical/High/Medium/Low) with root cause analysis
    and remediation guidance. Provide raw Move source code or a GitHub URL. Cost: $2.00 via x402."""
    payload = {"contract_name": contract_name}
    if source:
        payload["source"] = source
    if github_url:
        payload["github_url"] = github_url
    try:
        r = httpx.post(f"{BASE}:8022/audit", json=payload, timeout=120)
        return r.json()
    except Exception as e:
        return {"error": "Service temporarily unavailable"}


# ── DeFi & Staking ────────────────────────────────────────────────────────────

@mcp.tool()
def staking_yields(symbol: str = "") -> dict:
    """Live staking yield comparison across 7 assets (ETH, SOL, ATOM, ADA, DOT, AVAX, MATIC).
    For each asset returns: protocol APY (live), exchange rates (Coinbase/Kraken/Binance — live),
    liquid staking options (Lido, Frax, Rocket Pool, Marinade, Jito — live from DeFiLlama),
    liquid restaking options for ETH (ether.fi, Renzo, Kelp, Puffer — live), and a
    best_strategy field naming the single highest-yield option with its risk level.
    Use when an agent needs to know where to stake an asset for maximum yield.
    Pass symbol (ETH/SOL/ATOM etc.) to filter, or leave blank for the full report. Cost: $0.05."""
    params = {}
    if symbol:
        params["symbol"] = symbol.upper()
    return _get(f"{BASE}:8033/report", params)


@mcp.tool()
def aerocheck_pool(pool_address: str) -> dict:
    """Aerodrome DEX pool risk assessment on Base. Checks both tokens in the pool for honeypots,
    rug pull vectors, hidden ownership, and tax manipulation. Returns per-token risk scores,
    flags, and an AI verdict: safe / caution / avoid. Use before providing liquidity."""
    return _get(f"{BASE}:8035/pool", {"address": pool_address})


# ── Documents & Utilities ─────────────────────────────────────────────────────

@mcp.tool()
def pdf_to_markdown(url: str, summarize: bool = True) -> dict:
    """Convert any PDF document (via URL) to clean Markdown. Returns full markdown text,
    page count, word count, table count, metadata, and an AI summary. Useful for
    extracting structured content from whitepapers, reports, contracts, or research papers."""
    return _get(f"{BASE}:8034/report", {"url": url, "summarize": str(summarize).lower()})



# ── Token Launch Intelligence ──────────────────────────────────────────────────

@mcp.tool()
def wealth_pulse(wallet: str = "", tickers: str = "", contracts: str = "") -> dict:
    """Cross-asset portfolio risk analyzer. Pass a wallet address — auto-fetches all Base on-chain holdings (ERC-20 + ETH), values each position, flags stablecoin % and top concentration. Also accepts stock tickers and token contracts. Returns unified risk score 1-10, AI narrative, and cross_asset_flags."""
    params = {}
    if wallet:
        params["wallet"] = wallet
    if tickers:
        params["tickers"] = tickers
    if contracts:
        params["contracts"] = contracts
    return _get(f"{BASE}:8042/analyze", params)


@mcp.tool()
def bundle_scope(address: str) -> dict:
    """Token launch bundle and sniper detection on Base. Scans first 3 blocks after launch
    for same-block coordinated buys. Returns risk score, bundle wallets, and dump status.
    Use before buying any new token to check if the launch was bundled."""
    return _get(f"{BASE}:8043/scan", {"address": address})

# ── Autonomous Agent ──────────────────────────────────────────────────────────

@mcp.tool()
def hire_floyd(task: str, repo: str = "", context: str = "") -> dict:
    """Hire Floyd autonomous coding agent. Writes code and opens pull requests on GitHub."""
    payload = {"task": task}
    if repo:
        payload["repo"] = repo
    if context:
        payload["context"] = context
    try:
        r = httpx.post(f"{BASE}:8011/hire", json=payload, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": "Service temporarily unavailable"}


if __name__ == "__main__":
    if os.getenv("SERVE_HTTP"):
        import uvicorn
        app = mcp.http_app(path="/mcp")
        uvicorn.run(app, host="0.0.0.0", port=8018, log_level="info")
    else:
        mcp.run()
