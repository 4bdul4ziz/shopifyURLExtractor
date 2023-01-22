from django.shortcuts import render
import re
from urllib.request import urlopen

def search_url(request):
    if request.method == 'POST':
        url = request.POST['url']
        html = urlopen(url).read().decode('utf-8')
        shopify_shop = re.search(r'Shopify.shop = "([^"]+)"', html, re.IGNORECASE)
        return render(request, 'search.html', {'shopify_shop': shopify_shop})
    return render(request, 'search.html')
