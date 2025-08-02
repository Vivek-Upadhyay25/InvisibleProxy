# InvisibleProxy
Where code learns to think and bots act like humans — a next-gen automation hub.


# Proxy-Controlled Manual Chrome Browser with Playwright

This Python script launches a real (non-headless can be use as headless just need change " browser = await p.chromium.launch(headless=False)" as True) Chromium browser using Playwright, and routes all web traffic through an authenticated proxy server (supporting hostname-based proxies ).

🚀 Features

- ✅ Opens a visible browser window (not headless)
- 🌍 Routes all traffic through authenticated proxies
- 🔐 Proxy credentials are stored **only** in `config.json` (not in the code)
- 🧪 Lets you manually browse any website (good for geo-testing, anti-bot bypassing)
- 📦 Easy to run, GitHub-safe project


 🛠️ Requirements

- Python 3.7 or higher
- Pip
- Playwright

Install everything:

```bash
pip install playwright
playwright install


That's done - Run and Explore.


