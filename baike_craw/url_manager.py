class Manager(object):
    def __init__(self):  # 后面的似乎以下面的为实例化————分割——————初始化init后，后面的新函数也用self为实例对象
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            # 因为这个用的是add函数，
            # 而且判断既不在新也不在旧才添加

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
            # 这里用的是上面定义好的方法
            # 爬取一个网页后批量添加，但是需要保证是否不在已爬取中，所以是用自己的函数

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()  # 新的不用加对象
        self.old_urls.add(new_url)  # 已经定义的一定有对象self
        return new_url



