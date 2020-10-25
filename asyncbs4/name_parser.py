str = 'https://bilim-all.kz/esimder/all?sort=value&page={}&per-page=100'
import asyncio
import aiohttp
import lxml
from bs4 import BeautifulSoup
import time
import multiprocessing
import threading


async def get_content(session,url):
    async with session.get(url,timeout = 3) as responce:
            data = await responce.text(encoding='utf-8')
            print('url : {}'.format(url))
    return BeautifulSoup(data,'lxml')

async def parse(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_content(session,i)) for i in urls]
        soups = await asyncio.gather(*tasks,return_exceptions=True)
    return soups

def get_url_responce(url):
    urls = [url.format(i) for i in range(1,22)]
    loop = asyncio.get_event_loop()
    soups = loop.run_until_complete(parse(urls))
    loop.close()

    return soups

start = time.time()
soups = get_url_responce(str)
print(time.time() - start)


divs = []
for i in soups:
    divs.append(i.findAll("h2", {"class": "heading"}))

names = []
for i in divs:
    for j in i:
        names.append(j.text)
        