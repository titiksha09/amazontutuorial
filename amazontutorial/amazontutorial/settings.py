BOT_NAME = 'amazontutorial'
SPIDER_MODULES = ['amazontutorial.spiders']
NEWSPIDER_MODULE = 'amazontutorial.spiders'
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}
