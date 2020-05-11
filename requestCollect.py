import requests
import urllib.request
import threading
import os


def download(data, number):
    print(f"Downloading image number: {number}")
    r = requests.get(data['webformatURL'])
    with open(f'imageSets/realistic/{number}.jpeg', 'wb') as f:
        f.write(r.content)


# make_image_classifier --image_dir imageSets --tfhub_module https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4 --image_size 224 --saved_model_dir new_model --labels_output_file class_labels.txt

fileNames = ['human', 'dog', 'cat', 'chicken', 'baby', 'child']
counter = 1
os.makedirs(f'imageSets/realistic')
for fileName in fileNames:
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
                threading.Thread(target=download, args=(image, counter,)).start()
                counter += 1
