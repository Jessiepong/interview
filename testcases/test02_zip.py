import unittest
import requests
import settings

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.url = "https://assessement.onrender.com/api/zip"
        self.zip_file_path = settings.zip_file_path

    def test_zip_upload(self):
        with open(self.zip_file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(self.url, files=files)

        try:
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            print("fault:%s, already handled" %e)
            raise e


        #the response is a JSON containing a list of image URLs
        data = response.json()
        # print(data,type(data))

        # Check if each URL is accessible
        for image_url in data.get('images'):
            image_response = requests.get(image_url)
            try:
                self.assertEqual(image_response.status_code, 200)
            except Exception as e:
                print("fault:%s, already handled" % e)
                raise e


