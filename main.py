import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='vision_key.json'
from google.cloud import vision

def longestString(strings):
    max_len = -1
    res = ''
    for s in strings:
        if(len(s) > max_len):
            max_len = len(s)
            res = s
    return res

def main():

    files = os.listdir("images/todo")
    

    for i in files:
        print("\n")
        old_name = os.path.join("images/todo/", i)

        client = vision.ImageAnnotatorClient()

        image = vision.Image()
        image.source.image_uri = os.path.join('gs://YOUR_BUCKET_NAME_HERE/', i)
        response = client.document_text_detection(image=image)
        texts = response.text_annotations

        if(len(texts) > 0):
            code = texts[0].description
            code = code.replace(" ", "")
            code = code.split('\n')
            code = longestString(code)
            code = code.replace('/', '1')
            new_name = "images/complete/IMG_20230228_" + code + ".jpg"
            try:
                os.rename(old_name, new_name)
                print(old_name + "\t" + new_name)
            except:
                print("RENAME FAILED: \t" + old_name + "\t" + new_name + "\t" + code)
        else:
            print(i + "\t" + "FAILED")

if __name__ == '__main__':
    main()