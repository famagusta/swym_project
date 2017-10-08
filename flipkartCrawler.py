'''
Simple script to crawl all pages with apple mobile phones on 
flipkart
'''
import requests
import re
import json
from bs4 import BeautifulSoup
    
def crawl_flipkart_mobiles(current_url, visited_urls, child_urls, mobile_ids):
    '''
    Crawl Flipkarts Mobile Category for All Apple Products
    This is essentially a bread first search of html pages 
    '''
    flipkart_prefix = "http://www.flipkart.com"
    page = requests.get(url = flipkart_prefix + current_url).text
    pageText = BeautifulSoup(page, 'html.parser')
    
    title_tag = pageText.find_all("a", href=True)
    
    # add pages with starting tags /mobiles/apple~brand/ to list of pages to crawl
    # add pages which end with .SEARCH to list of phone ids
    visited_urls[current_url] = True
    for tag in title_tag:
        if tag['href'] is None or tag['href'] == current_url:
            continue
        if re.search("/mobiles/apple~brand/*", tag['href']) is not None:
            if tag['href'] not in visited_urls:
                child_urls.append(tag['href'])
        url_tokens = tag['href'].split('.')
        if url_tokens[-1] =='SEARCH':
            mobile_ids[url_tokens[-2]] = tag['href']
            
    print(str(len(child_urls)) + " New nodes added to list")
    print("Visited " + str(len(visited_urls)) + " nodes")
    print("Current Number of mobile ids " + str(len(mobile_ids)))
    
    if not child_urls:
        # no more relationships to crawl - return the result
        return visited_urls, mobile_ids
    else:
        # recursively crawl the child_url list which contains neighbours of 
        # visited nodes so far 
        current_url = child_urls.pop(0)
        crawl_flipkart_mobiles(current_url, visited_urls, child_urls, mobile_ids)
        
def fetch_product_review(phone_id):
    product_review_url = "http://www.flipkart.com/api/3/page/dynamic/product-reviews"
    
    # Fetch total number of reviews from first page of reviews - helps prevent making multiple calls
    payload = '{ "requestContext": {"productId":"MOBEN2YYKU9386TQ"}}'
    
    additional_headers = {
                             "Content-Type" : "application/json",
                            "X-user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 FKUA/website/41/website/Desktop"
                        }
    page = requests.post(url = product_review_url, data = payload, 
                         headers=additional_headers).text
    review_data = BeautifulSoup(page, 'html.parser')
    
    review_data_json = json.loads(str(review_data))
    no_of_reviews = review_data_json['RESPONSE']['data']['product_review_page_default_1']['params']['totalCount']
    
    # fetch all data for review
    payload = '{ "requestContext": {"productId":"' + phone_id + '", "start":"1", "count":' + str(no_of_reviews) + '}}'

    page = requests.post(url = product_review_url, data = payload, 
                         headers=additional_headers).text
    review_data = BeautifulSoup(page, 'html.parser')
    
    review_data_json = json.loads(str(review_data))
    reviews = review_data_json['RESPONSE']['data']['product_review_page_default_1']['data']
    output = []
    for review in reviews:
        simple_review = {}
        simple_review['author'] = review['value']['author']
        simple_review['text'] = review['value']['text']
        simple_review['url'] = "http://www.flipkart.com" + review['value']['url']
        output.append(simple_review)
        
    return output