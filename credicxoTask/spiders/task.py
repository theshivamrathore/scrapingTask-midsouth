import scrapy

###### to store the data into file use command
        ### - scrapy crawl task -o data.json
        ### Already i have stored data into data.json for your reference


class Task(scrapy.Spider):
    name = 'task'
    start_urls = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1']

    def parse(self, response):
        """This function will crawl the data from the given url in the start_urls list"""

        price = response.css('.price span::text').extract()
        title = response.css('.catalog-item-name::text').extract()
        stock = response.css('.status *::text').extract()
        manufacturer = response.css('.catalog-item-brand::text').extract()

        zip_data = zip(price,title,stock,manufacturer)

        for data in zip_data:
            crawl =  {
                'price':data[0],
                'title':data[1],
                'stock':'flase' if data[2] == 'Out of Stock' else 'true',
                'manufacturer':data[3]
            }

            yield crawl