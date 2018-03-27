class Outputer(object):
    def __init__(self):  # 需要一个列表来放数据，所以这里初始化
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)#列表append

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')#不用在fout下encode了
        fout.write('<html>')
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")#神来之笔
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')