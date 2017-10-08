'''
Simple script to crawl all pages with apple mobile phones on 
flipkart
'''

import os
from flipkartCrawler import crawl_flipkart_mobiles


if __name__=="__main__":
    flipkart_apple_mobile_start_url = "/mobiles/apple~brand/pr?sid=tyy,4io"
    visited_urls = {}
    child_urls = []
    mobile_ids = {}
    crawl_flipkart_mobiles(flipkart_apple_mobile_start_url, visited_urls, child_urls, mobile_ids)
    
    file_path = os.getcwd() + "/flipkart_apple_data/" + "mobile_ids.txt"
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    print("Writing to file")
    with open(file_path, 'w') as outfile:
        for key, value in mobile_ids.iteritems():
            if key == " " or key == "" or key is None:
                continue
            outfile.write(key + ',' + "http://www.flipkart.com" + value + '\n')