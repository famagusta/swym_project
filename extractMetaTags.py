'''
Extract a products meta data as described by opengraph 
we shall assume that both product page and crawled pages
have opengraph meta tags. 
Note : Amazon is the largest ecommerce site in the world
       They however do not annotate their site with 
       opegraph tags. They have their own custom 
       tagging system
'''

import requests 
from bs4 import BeautifulSoup

class OpenGraphMetaData():
    __slots__ = ['_title', '_type', '_url', '_image', '_site_name']
    def __init__(self, title, prod_type, url, image, site_name):
        self._title = title
        self._type = prod_type
        self._url = url
        self._image = image
        self._site_name = site_name
    
    def __str__(self):
        return str(self._title) + '\n' + str(self._type) + '\n' \
            + str(self._url) + '\n' + str(self._image) + '\n' + str(self._site_name)   
             
    def is_valid(self):
        return self._title is not None or self._type is not None\
             or self._url is not None or self._image is not None
        
def extract_meta_tags(pageText):
    title_tag = pageText.find("meta", attrs={"property":"og:title"})
    title = None
    if title_tag:
        title = title_tag.attrs['content']
        
    url_tag = pageText.find("meta", attrs={"property":"og:url"})
    url = None
    if url_tag:
        url = url_tag.attrs['content']
        
    image_tag = pageText.find("meta", attrs={"property":"og:image"})
    image = None
    if image_tag:
        image = image_tag.attrs['content']
        
    type_tag = pageText.find("meta", attrs={"property":"og:type"})
    prod_type = None
    if type_tag:
        prod_type = type_tag.attrs['content']
        
    site_name_tag = pageText.find("meta", attrs={"property":"og:site_name"})
    site_name = None
    if site_name_tag:
        site_name = site_name_tag.attrs['content']
    
    basic_meta_data = OpenGraphMetaData(title, prod_type, url, image, site_name)
    
    return basic_meta_data
    
if __name__=="__main__":
    # Test code
    iphone_url = "https://www.apple.com/shop/buy-iphone/iphone-7"
    page = requests.get(url = iphone_url).text
    pageText = BeautifulSoup(page, 'html.parser')
    iphone_meta_tags = extract_meta_tags(pageText)
    print(iphone_meta_tags)
    
    flipkart_iphone_url = "https://www.flipkart.com/apple-iphone-7-black-32-gb/product-reviews/itmen6daftcqwzeg?pid=MOBEMK62PN2HU7EE"
    page = requests.get(url = flipkart_iphone_url).text
    pageText = BeautifulSoup(page, 'html.parser')
    flipkart_meta_tags = extract_meta_tags(pageText)
    print(flipkart_meta_tags)