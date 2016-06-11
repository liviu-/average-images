import os
import urllib
import urllib.error
import requests


URL = "https://bingapis.azure-api.net/api/v5/images/search"
NUMBER_OF_IMAGES = 10
DIR = '/tmp/average_images'

def search_images(term, api_key):
    params = {"q": term, "count":NUMBER_OF_IMAGES}
    headers = {'ocp-apim-subscription-key': api_key}
    response = requests.request("GET", URL,
                                headers=headers,
                                params=params)

    return response.json()['value']

def download_image(url, filename):
    urllib.request.urlretrieve(url, filename)

def get_api_key():
    try:
        api_key_file = os.path.join(
            os.path.expanduser('~'), ".average_pixels_api")
        with open(api_key_file, 'r') as f:
            api_key = f.read().replace('\n','')
    except FileNotFoundError:
        api_key = input("Please insert your API key: ")

    return api_key


def save_images(term):
    api_key = get_api_key()
    images = search_images(term, api_key)
    filenames = []

    if not os.path.exists(DIR):
        os.makedirs(DIR)


    for i, img in enumerate(images):
        if img['encodingFormat'] == 'unknown':
            continue
        name = "{path}/{filename}.{ext}".format(
                path=DIR,
                filename="_".join(term.split()) + str(i),
                ext=img['encodingFormat'])
        try:
            download_image(img['contentUrl'], name)
            filenames.append(name)
        except urllib.error.HTTPError:
            pass

    return filenames
