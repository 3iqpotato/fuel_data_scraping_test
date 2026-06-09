import asyncio

import httpx
from bs4 import BeautifulSoup

async def scrape_fuel(url: str) -> list[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    html_response = BeautifulSoup(response.text, 'html.parser')
    data_list = html_response.find_all("a", class_="graph_outside_link")

    graphic = html_response.find('div', id="graphic")
    prices = graphic.find_all('div')[4::]
    prices = [prices[i] for i in range(len(prices)) if i % 2 == 0]
    res = []
    for i in range(len(data_list)):
        res.append({data_list[i].text.strip().replace("*", ""): prices[i].text})

    return res
    # httpx.get → BeautifulSoup → връща list от {country, price_usd}



