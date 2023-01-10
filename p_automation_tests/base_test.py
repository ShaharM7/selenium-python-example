from containers import Container


class BaseTest(object):

    def setUp(self):
        container = Container()
        chrome_browser = container.chrome_browser

    def tearDown(self):
        pass


if __name__ == "__main__":
    pass
