System Requirement
===================================================================================================
Any unix based environment with Python2.7 or higher (including Python3)
Python package manager pip
Python virtual environment wrappers virtualenv
A working internet connection.


Getting Started
===================================================================================================
1. Download and install virtualenv in your system.
2. Navigate to project folder and start the virtualenv by typing the following command
	$ virtualenv venv
	$ source ./venv/bin/activate
	$ pip install -r requirements.txt (for python2)
	$ pip2 install -r requirements.txt (for python3)
	
	
Crawling Flipkart
====================================================================================================
	$ sh fetchFlipkartReviews
	
The script takes a while to run. At the end of the scripts, you should see a folder
flipkart_apple_data populated with some files


Searching for Product Review
====================================================================================================
python fetchProductReview.py product_url

This system has been tested for products from apples iphone series
https://www.apple.com/shop/buy-iphone/iphone-8
https://www.apple.com/shop/buy-iphone/iphone-7
https://www.apple.com/shop/buy-iphone/iphone6s
https://www.apple.com/shop/buy-iphone/iphone-se

