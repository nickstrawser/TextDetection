## Text identification and file renaming using Google Vision API

### To use this app
1. Clone the repository
2. Install python3 and the google-cloud-vision module for python
3. Create a Google cloud account at https://cloud.google.com/storage, follow their instructions for creating a new project and creating the vision_key.json file (helpful link here: https://cloud.google.com/vision/docs/ocr)
4. add images you wish to process to a bucket in your google cloud storage account as well as to the images/todo folder in the local repository
5. update the path on line 26 of main.py to include your bucket name and replace YOUR_BUCKET_NAME_HERE
6. update the new_name variable on line 36 to your chosen filename
7. delete the DELETE_ME.txt file in both images/todo and images/complete
8. run main.py