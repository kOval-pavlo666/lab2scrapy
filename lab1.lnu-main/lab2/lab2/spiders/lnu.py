import scrapy
from bs4 import BeautifulSoup
from lab2.items import FacultyItem, DepartmentItem, StaffItem


class LnuSpider(scrapy.Spider):
    name = "lnu"
    allowed_domains = ["lnu.edu.ua"]
    start_urls = ["https://lnu.edu.ua/about/faculties/"]


    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        # знаходимо список факультетів і для кожного факультету
        fac_list = soup.find(class_="page-content")
        for item in fac_list.find_all(class_="thumb"):
            a = item.find("a")
            # в <a> знаходимо тег <img> і отримуємо атрибут alt
            img_tag = a.find('img')
            if img_tag:
                fac_name = img_tag.get('alt')
                fac_url = a.get('href')
                print(f"Faculty Name: {fac_name}, URL: {fac_url}")
        
            yield FacultyItem(
                name=fac_name,
                url=fac_url
            )

            yield scrapy.Request(
                # адреса сторінки, яку необхідно парсити
                url=fac_url,
                # метод для обробки результатів завантаження
                callback=self.parse_faculty,
                # передаємо дані про факультет в функцію колбеку
                meta={
                    "faculty": fac_name
                }
            )
            
    def parse_faculty(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        dep_list = soup.find(class_="menu clearfix")
        # для кожної кафедри у списку

        for li in dep_list.find_all("li"):
                a = li.find("a")
                # знаходимо текст безпосередньо в контенті елементу  a
                dep_name = a.find(string=True, recursive=False)
                # URL кафедри
                dep_url = a.get('href')
                # повертаємо дані про кафедру

                yield DepartmentItem(
                    name=dep_name,
                    url=dep_url,
                    # факультет дізнаємось із метаданих, переданих при запиті
                    faculty=response.meta.get("faculty")
                )
            