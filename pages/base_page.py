from urllib.parse import urlparse

class BasePage(object):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.driver.get('https://b2c.passport.rt.ru')
 

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path


class BaseOnlimePage(object):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.driver.get('https://my.rt.ru/')


    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path


class BaseStartPage(object):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.driver.get('https://start.rt.ru/')


    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path


class BaseSmarthomePage(object):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.driver.get('https://lk.smarthome.rt.ru/')


    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path


class BaseKeyPage(object):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.driver.get('https://key.rt.ru/')


    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path