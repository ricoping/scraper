# scraper
You can easily get HTML source. You can get the HTML source of static web page or dynamic web page by just selecting mode.

## How to use
~~~
import scraper
url = "https://www.google.com/search"
s = scraper.Scraper(url)

source = s.dynamicUrlParser() # Getting the HTML source of static web page
source = s.staticUrlParser() # Getting the HTML source of dynamic web page
source = s.dynamicUrlParserByTarget("app") 
# Getting the HTML source of dynamic web page after DOM you want is on.
~~~
