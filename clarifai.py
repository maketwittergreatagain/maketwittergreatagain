from clarifai.client import ClarifaiApi

clarifai_api = ClarifaiApi()  # assumes environment variables are set.
result = clarifai_api.tag_image_urls('http://www.clarifai.com/img/metro-north.jpg')
