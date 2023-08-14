import unittest
from BeautifulReport import BeautifulReport

import settings

if __name__=='__main__':
    ts = unittest.TestLoader().discover(settings.test_case_dir)
    bs = BeautifulReport(ts)
    bs.report('report.html')