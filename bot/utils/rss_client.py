import feedparser 
import httpx 
from collections import deque
import asyncio 
from bs4 import BeautifulSoup
from bot.db.crud import count_sources, get_sources, add_news
from hashlib import md5

class RSSClient:
    def __init__(self):
        self.client = httpx.AsyncClient()
        self.posted_q = deque(maxlen=1000)
        self.link="https://dev.to/feed/tag/python"
        self.iss = True
    
    async def rss_parser(self):
        while self.iss == True:
            if await count_sources() > 1:
                await asyncio.sleep(600)
                continue
            
            try:
                response = await self.client.get(self.link)
            except:
                await asyncio.sleep(10)
                continue

            feed = feedparser.parse(response.text)
            for entry in feed.entries:
                title = entry['title']
                description = entry['description']
                link = entry['link']

                description = BeautifulSoup(description, 'html.parser').get_text().strip()
                # print(description)
                content_hash = md5(description.encode()).hexdigest()
                if content_hash in self.posted_q:
                    continue

                await add_news(title=title, description=description, link=link)
                self.posted_q.appendleft(content_hash)
            await asyncio.sleep(5)
