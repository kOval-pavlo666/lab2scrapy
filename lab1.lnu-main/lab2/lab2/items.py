# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class FacultyItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    

class DepartmentItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    faculty = scrapy.Field()

class StaffItem(scrapy.Item):
    name = scrapy.Field()
    department = scrapy.Field()

class Lab2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
