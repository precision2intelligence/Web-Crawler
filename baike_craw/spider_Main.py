import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):  # object 和 self 是什么关系？
        self.urls = url_manager.Manager()  # 文件名（库名）.类？
        self.download = html_downloader.Downloader()
        self.parser = html_parser.Parser()
        self.output = html_outputer.Outputer()

    def craw(self, root_url):  # 传入参数
        self.urls.add_new_url(root_url)  # 对象.方法
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.download.download_url(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 前两步获得的参数
                self.urls.add_new_urls(new_urls)  #增加新解析出的页面链接
                self.output.collect_data(new_data) #列表化

                if count == 100:
                    break
                count = count + 1
            except:
                print('craw failed')
        self.output.output_html()  # 写出为html

if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)  # 对象+方法，曾经错过
