import unittest
from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import assertHTTPCode


class TestloginHTTP(unittest.TestCase):
    LoginURL = Config().get('LoginURL')

    def setUp(self):
        self.client = HTTPClient(url=self.LoginURL, method='GET')

    def test_login_http(self):
        res = self.client.send()
        logger.debug(res.text)
        assertHTTPCode(res, [400])
        self.assertIn('嗯哼嗯哼蹦擦擦', res.text)


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='接口html报告')
        runner.run(TestloginHTTP('test_login_http'))
