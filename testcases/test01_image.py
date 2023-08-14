import unittest
import requests
from ddt import ddt, data, unpack

@ddt
class TestImageAPI(unittest.TestCase):
    @data(
        ('image/jpeg', './testdata/test01.jpg', 200),
        ('image/png', './testdata/test03.PNG', 200),
        ('application/pdf', './testdata/test02.txt', 500)
    )
    @unpack
    def test_image_upload(self, content_type, file_name, expected_status_code):
        url = 'https://assessement.onrender.com/api/image'
        with open(file_name, 'rb') as f:
            files = {'file': (file_name, f, content_type)}
            response = requests.post(url, files=files)
        try:
            self.assertEqual(response.status_code, expected_status_code)
        except Exception as e:
            print("fault:%s, already handled"%e)
            raise e


# C:\Users\jessi\Desktop\Interface Test\testcases\test01_image.py
# C:\Users\jessi\Desktop\Interface Test\testdata\test01.jpg