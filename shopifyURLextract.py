import re
from urllib.request import urlopen

def input_url():
    url = input("Enter the url: ")
    return url

def main():
    html = urlopen(input_url()).read().decode('utf-8')
    shopify_shop = re.search(r'Shopify.shop = "([^"]+)"', html, re.IGNORECASE)
    print(shopify_shop)

main()

