# crawlfutures
Crawl data of Taiwan futures

# Run

## 加權收盤價
  * python crawl_taiex.py [year] [begin_month] [end_month]
  * python crawl_taiex.py [year]/[month]/[day]
  
## 三大法人未平倉
  * python crawl_comp.py [TXF|MXF] [year] [begin_month] [end_month]
  * python crawl_comp.py [TXF|MXF] [year]/[month]/[day]

## 期貨收盤資訊
  * python crawl_futures.py [TX|MTX] [year] [begin_month] [end_month]
  * python crawl_futures.py [TX|MTX] [year]/[month]/[day]

# Todo Fix
python urllib2: connection reset by peer
