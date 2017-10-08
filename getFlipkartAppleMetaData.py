'''
Simple script to crawl all pages with apple mobile phones on 
flipkart
'''
import requests
import os
from bs4 import BeautifulSoup
from extractMetaTags import extract_meta_tags


if __name__=="__main__":  
    flipkart_mobile_id_file = os.getcwd() + "/flipkart_apple_data/mobile_ids.txt"
    product_info = None
    with open(flipkart_mobile_id_file) as f:
        product_info = f.readlines()
            
    for product in product_info:
        mobile_id, mobile_url = product.split(',')
        page = requests.get(url = mobile_url).text
        pageText = BeautifulSoup(page, 'html.parser')
        try:
            meta_data = extract_meta_tags(pageText)
            file_path = os.getcwd() + "/flipkart_apple_data/" + mobile_id + "/meta_tags.txt"
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
                 
            print("Writing Flipkart Reviews for " + mobile_id + " to file")
            with open(file_path, 'w') as outfile:
                outfile.write(str(meta_data))
        except Exception as exception:
            print("Exception Encountered in fetching Flipkart reviews for product with id " + mobile_id)
            print("\t" + str(exception))
