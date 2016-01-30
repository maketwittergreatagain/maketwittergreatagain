# -*- coding: utf-8 -*-

BOT_NAME = 'scrashtest'

SPIDER_MODULES = ['maketwittergreatagain.spiders']
NEWSPIDER_MODULE = 'maketwittergreatagain.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapyjs.SplashMiddleware': 725,
}

DUPEFILTER_CLASS = 'scrapyjs.SplashAwareDupeFilter'
SPLASH_URL = 'http://192.168.59.103:8050/'
