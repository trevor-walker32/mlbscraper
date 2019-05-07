import requests
from selenium import webdriver
from bs4 import BeautifulSoup

#TODO inspect web elements to find tabular data 

options = []
choices = []
cart = []
newCart = []

data = requests.get('https://shop.travisscott.com')

soup = BeautifulSoup(data.text, 'html.parser')

listOfProducts = soup.find('div', {'class': 'shopify-section ProductGrid__outer'})

products = listOfProducts.find('div', {'class': 'ProductGrid ProductGrid__home js-product-grid'})

for product in products.find_all('a'):
    options.append(product.find_all('span')[1].text.strip())

for choice in choices:
    for option in options:
        if set(choice).intersection(set(option.lower())):
            if option not in cart:
                cart.append(option)

for option in options:
    output = option.lower().replace(' ','-')
    newCart.append(output)

# driver = webdriver.Safari()


for option in newCart:
    url = "https://shop.travisscott.com/products/{}".format(option)
    print(url)
    # driver.get(url)
    newData = requests.get(url)
    moreSoup = BeautifulSoup(data.text, 'html.parser')
    product2 = moreSoup.find('main', {'class':'B__container'})
    product3 = product2.find('div',{'class':'B__content'})
    product4 = product3.find_all('div')[1]
    product5 = product4.find_all('span')[1]
    print(product5.text.strip())
    
    # print(product5)
    # product6 = product5.find_all('div')
    # print(product6)

# addToCart = driver.find_element_by_id('')
# addToCart.click()