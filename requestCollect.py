import requests
import urllib.request
import threading
import os


def download(data, number, fileName):
    print(f"Downloading image number: {number}")
    r = requests.get(data['webformatURL'])
    with open(f'imageSets/{fileName}/{number}.jpeg', 'wb') as f:
        f.write(r.content)



fileNames = ['human', 'dog', 'cat', 'chicken', 'baby', 'child']


for fileName in fileNames:
    counter = 1
    os.makedirs(f'imageSets/{fileName}')
    print(f"Using {fileName}")


    terms = [f"realistic+{fileName}", f"realistic+looking+{fileName}"]
    for term in terms:
        print(f"Searching for: {term}\n\n")
        for i in range(1, 6):
            payload = {
                'key': 'API_KEY',
                'q': term,
                'image_type': 'photo',
                'colors': 'rgb',
                'per_page': 200,
                'page': i

            }
            try:
                r = requests.get('https://pixabay.com/api/', params=payload)
                b = r.json()
            except Exception as e:
                break
            for image in r.json()['hits']:
                threading.Thread(target=download, args=(image, counter,fileName)).start()
                counter += 1
