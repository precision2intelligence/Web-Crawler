from bs4 import BeautifulSoup
import urllib.parse
import re

class Parser(object):
    def _get_new_url(self, page_url, soup):  # 这里怎么又是soup？？page_url是补全代码用的
        new_urls = set()
        # /<a target="_blank" href="/item/C%2B%2B">C++</a>
        links = soup.find_all('a', href=re.compile(r"/item/.*"))#???r"/item/.*"或者r"/item/"

        for link in links:
            new_url = link['href']  # 不知道这句话是什么意思
            new_full_url = urllib.parse.urljoin(page_url, new_url)  # 这里还得导入
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data={}  # 定义字典

        # url
        res_data['url']=page_url

        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1><h2>（计算机程序设计语言）</h2>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary"><div class="para" label-module="para">Python<sup>[1]</sup><a class="sup-anchor" name="ref_[1]_21087">&nbsp;</a>
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self,page_url,html_cont):  # 先写的这里
        if page_url is None or html_cont is None:
            return  # 为什么不是return None？return是直接停吗

        soup=BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        # print(soup)
        new_urls = self._get_new_url(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data
