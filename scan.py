import urllib.request
import requests
import re
import urllib.parse # etait nommee urlparse
class Scanner:
    def __init__(self,url):
        self.session=requests.Session()
        self.target_url=url
        self.target_links=set()

    def extract_links_from(self,url):
        response=self.session.get(url)
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

    def login_script(self,url=None):

        data_dict = {"usename": "admin",
                     "password": "blabla"}
        response = requests.post(url, data=data_dict)
        #response2 = requests.get()
        print(response.content)
        target_url=""
        data_dict={"usename":"admin",
           "password":"blabla"}
        response= requests.post(target_url,data=data_dict)
        response2=requests.get()
        print(response.content)

    def google_search(self, url):
        #url = 'https://google.com/search?q=python'
        # Perform the request
        request = urllib.request.Request(url)
        # Set a normal User Agent header, otherwise Google will block the request.
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
        raw_response = urllib.request.urlopen(request).read()

        # Read the repsonse as a utf-8 string
        html = raw_response.decode("utf-8")
        A = re.findall('(?:href=")(.*?)"', str(html))
        for t in A:
            if "https" in t:
                print(t)



if __name__=="__main__":
    url='https://google.com'
    scan=Scanner(url)
    scan.crawl(url)

    url_test='''http://www.google.com/search?
      start=0
      &num=10
      &q=aknanai
      &cr=countryCA
      &lr=lang_fr
      &client=google-csbe
      &output=xml_no_dtd
      &cx=00255077836266642015:u-scht7a-8i'''
    url_test2='''http://www.google.com/search?
      start=0
      &num=5
      &q=aknanai
      &client=google-csbe
      &output=xml_no_dtd
      &cx=00255077836266642015:u-scht7a-8i'''

    r=requests.get(url_test2)
    A=re.findall('(?:href=")(.*?)"', str(r.content))
    for t in A:
        if "https" in t:
            print(t)





