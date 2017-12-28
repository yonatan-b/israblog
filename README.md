# israblog
command line:
-------------
.\israblog\israblog>scrapy crawl israblog_scrape -o israblog.jl

scraper statistics:
-------------------
2017-12-24 05:03:55 [scrapy.core.engine] INFO: Closing spider (finished)
2017-12-24 05:03:55 [scrapy.extensions.feedexport] INFO: Stored jl feed (739676 items) in: israblog.jl
2017-12-24 05:03:55 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/exception_count': 154,
 'downloader/exception_type_count/twisted.internet.error.DNSLookupError': 24,
 'downloader/exception_type_count/twisted.internet.error.TCPTimedOutError': 120,
 'downloader/exception_type_count/twisted.web._newclient.ResponseNeverReceived': 10,
 'downloader/request_bytes': 362314446,
 'downloader/request_count': 773028,
 'downloader/request_method_count/GET': 773028,
 'downloader/response_bytes': 33327050172,
 'downloader/response_count': 772874,
 'downloader/response_status_count/200': 771873,
 'downloader/response_status_count/302': 869,
 'downloader/response_status_count/400': 1,
 'downloader/response_status_count/404': 131,
 'dupefilter/filtered': 2287125,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2017, 12, 24, 3, 3, 55, 295822),
 'item_scraped_count': 739676,
 'log_count/DEBUG': 1512722,
 'log_count/ERROR': 1067,
 'log_count/INFO': 2571,
 'offsite/domains': 15,
 'offsite/filtered': 6633,
 'request_depth_max': 8249,
 'response_received_count': 772005,
 'scheduler/dequeued': 773024,
 'scheduler/dequeued/memory': 773024,
 'scheduler/enqueued': 773024,
 'scheduler/enqueued/memory': 773024,
 'spider_exceptions/IndexError': 13,
 'spider_exceptions/TypeError': 626,
 'spider_exceptions/ValueError': 417,
 'start_time': datetime.datetime(2017, 12, 22, 10, 32, 27, 45070)}
2017-12-24 05:03:55 [scrapy.core.engine] INFO: Spider closed (finished)
