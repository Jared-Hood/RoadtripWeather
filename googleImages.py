from google_images_download import google_images_download   #importing the library

def getPics(keyword):
    response = google_images_download.googleimagesdownload()  # class instantiation

    arguments = {"keywords": keyword, "limit": 1, "print_urls": True}  # creating list of arguments
    paths = response.download(arguments)  # passing the arguments to the function