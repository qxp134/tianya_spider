'''
Created on 

@author: QXP
'''


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self,word):
        fout = open('output%s.html'%word.decode('utf-8'), 'w')
        fout.write('<meta http-equiv="Content-Type"content="text/html;charset=utf-8"/>')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border = '1' table-layout:fixed;>")
        for data in self.datas:
            fout.write('<tr align = "center"  width = "1200" valign = "middle">')
            fout.write("<td><div style='width:1200px;word-wrap:break-word;'>%s</td>" % data['url'])
            fout.write("</tr>")
            fout.write('<tr align = "center"  width = "1200" valign = "middle">')
            fout.write("<td><div style='width:1200px;word-wrap:break-word;'>%s</td>" % data['title'].encode('utf-8'))
            fout.write("</tr>")
            fout.write('<tr align = "center"  width = "1200" valign = "middle">')
            fout.write("<td><div style='width:1200px;word-wrap:break-word;'>%s</td>" % data['time'])
            fout.write("</tr>")
            fout.write('<tr align = "center"  width = "1200" valign = "middle">')
            fout.write("<td><div style='width:1200px;word-wrap:break-word;'>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
        self.datas = []