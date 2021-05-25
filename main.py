import json

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"
}

product_list = []
product_page_url = []

try:
    response = requests.get('https://tiki.vn/api/v2/products?category=8095&urlKey=laptop', headers=headers)
    response.raise_for_status()
    # access JSOn content
    json_response = json.loads(response.text)
    pages = json_response["paging"]["last_page"]
    # Get a list url
    i = 1
    while i <= pages:
        product_page_url.append('https://tiki.vn/api/v2/products?category=8095&urlKey=laptop&page=' + str(i))
        i+=1

    # Get a product id
    for page_url in product_page_url:
        response_page = requests.get(page_url, headers=headers)
        json_response_page = json.loads(response_page.text)
        listing_id = json_response_page["data"]
        for product in listing_id:
            product_list.append(product["id"])

    print(product_list)
    print(len(product_list))


except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')