import scrapy

class MyprojectSpider(scrapy.Spider):
   name = "project"
   allowed_domains = ["theguardian/au"]
   
   start_urls = [
      "https:theguardian.com/au"
   ]
   def parse(self, response):
      for sel in response.xpath('//ul/li'):
         title = sel.xpath('a/text()').extract()
         link = sel.xpath('a/@href').extract()
         desc = sel.xpath('text()').extract()
         print (title, link, desc)