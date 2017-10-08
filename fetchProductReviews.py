'''
Main Script that executes review search of products based on input url
I have assumed here that we are using apple iphone series of products for 
searching reviews
For eg.
    http://www.apple.com/shop/buy-iphone/iphone-se
    http://www.apple.com/shop/buy-iphone/iphone6s
    https://www.apple.com/shop/buy-iphone/iphone-7
'''

import sys
import os
import requests
from bs4 import BeautifulSoup
from extractMetaTags import extract_meta_tags
import json
import pprint


def isTitleInMetaTagFile(meta_tag_file, title):
    '''
    Simplest possible matching function between a search query
    and tag files
    '''
    with open(meta_tag_file) as f:
        product_tags = f.readlines()[0]
        if title in product_tags:
            return True
        return False

def getAllReviews(product_id):
    '''
    Given a product id ~ retrieve all reviews for it from flipkart files
    '''
    file_path = os.getcwd() + "/flipkart_apple_data/" + product_id + "/reviews_json.txt"
    try:
        with open(file_path) as fd:
            json_data = json.load(fd)
        return json_data
    except Exception as exception:
        print(str(exception))

        
if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Invalid CLI input : kindly provide a url to query")
        
    url_input = sys.argv[1]
    
    page = requests.get(url = url_input).text
    pageText = BeautifulSoup(page, 'html.parser')
    product_meta_tags = extract_meta_tags(pageText)
    title = str(product_meta_tags._title)

    matching_ids = []
     
    rootDir = os.getcwd() + '/flipkart_apple_data/'
    for subdir, dirs, files in os.walk(rootDir):
        if isTitleInMetaTagFile(subdir + '/' + files[0], title):
            matching_ids.append(subdir.split('/')[-1])
    print(matching_ids)

    relevant_reviews = []
    for matching_id in matching_ids:
        matching_reviews = getAllReviews(matching_id)
        if matching_reviews is None:
            continue
        for matching_review in matching_reviews:
            relevant_reviews.append(matching_review)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(relevant_reviews)