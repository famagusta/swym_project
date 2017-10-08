'''
Simple script to crawl all pages with apple mobile phones on 
flipkart
'''
import os
import json
from flipkartCrawler import fetch_product_review


if __name__=="__main__":  
    flipkart_mobile_id_file = os.getcwd() + "/flipkart_apple_data/mobile_ids.txt"
    product_info = None
    with open(flipkart_mobile_id_file) as f:
        product_info = f.readlines()
            
    for product in product_info:
        mobile_id, url = product.split(',')
        try:
            reviews = fetch_product_review(mobile_id)            
            file_path = os.getcwd() + "/flipkart_apple_data/" + mobile_id + "/reviews_json.txt"
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
                 
            print("Writing Flipkart Reviews for " + mobile_id + " to file")
            with open(file_path, 'w') as fp:
                json.dump(reviews, fp)

        except Exception as exception:
            print("Exception Encountered in fetching Flipkart reviews for product with id " + mobile_id)
            print("\t" + str(exception))
