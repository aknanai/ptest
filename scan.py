import requests
import re
import urllib.parse # etait nommee urlparse
class Scanner:
    def __init__(self,url):
        self.target_url=url
        self.target_links=set()

    def extract_links_from(self,url):
        response=requests.get(url)
        return re.findall('(?:href=")(.*?)"',str(response.content))# str est une piece maitresse

    def crawl(self,url=None):
        href_links=self.extract_links_from(url)
        for link in href_links:
            link=urllib.parse.urljoin(url,link)

            if '#' in link:
                link=link.split("#")[0]

            '''if self.target_url in link and link not in self.target_links:
                self.target_links.add(link)
                print(link)
                self.crawl(link)'''
            if self.target_url in link and link not in self.target_links:
                print(link)
                self.target_links.add(link)
                self.crawl(link)

if __name__=="__main__":
    url='https://google.com'
    scan=Scanner(url)
    scan.crawl(url)