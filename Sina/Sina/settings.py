# encoding=utf-8
BOT_NAME = 'Sina'

SPIDER_MODULES = ['Sina.spiders']
NEWSPIDER_MODULE = 'Sina.spiders'

DOWNLOADER_MIDDLEWARES = {
    "Sina.middleware.UserAgentMiddleware": 401,
    "Sina.middleware.CookiesMiddleware": 402,
}

ITEM_PIPELINES = {
    'Sina.spiders.mypipelines.WeiboPipeline': 1,
}
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 2  # 间隔时间
MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '1111'
MYSQL_PORT = '3306'
MYSQL_DB = 'weibo'

