import asyncio
import json
from playwright.async_api import async_playwright


def load_proxy():
    with open("config.json", "r") as f:
        cfg = json.load(f)["proxy"]
        return {
            "server": f"http://{cfg['host']}:{cfg['port']}",
            "username": cfg["username"],
            "password": cfg["password"]
        }

async def main():
    proxy = load_proxy()

  
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # for headlesss you can make it " True"
        context = await browser.new_context(proxy=proxy)

        page = await context.new_page()
        print("✅ Proxy browser opened.")
        print("🕹️ You can now manually browse. Try visiting https://whatismyipaddress.com")

        await page.wait_for_timeout(600000)  # Keep open for 10 minutes ( MS is used)
        await browser.close()
if __name__ == "__main__":
    asyncio.run(main())
