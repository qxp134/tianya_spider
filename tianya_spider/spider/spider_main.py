# -*- coding: utf-8 -*-
'''
Created on 

@author: QXP
'''
from spider import url_manager, html_downloader, html_parser, html_outputer,connect_mysql
import os,time
from multiprocessing import Pool

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.connect = connect_mysql.Conenct()



    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try :
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont,count)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 11:
                    break
                count = count + 1
            except:
                print 'craw failed'


        
if __name__ == "__main__":
    obj_spider = SpiderMain()
    keywords = obj_spider.connect.keywords_list()
    p = Pool()
    for keyword in keywords:
        word = keyword[0].encode('utf-8')
        for page in range(1,70):
            root_url = "http://search.tianya.cn/bbs?q=%s&pn=%d"%(word,page)   
            p.apply_async(obj_spider.craw(root_url))
        p.close()
        p.join()
        obj_spider.outputer.output_html(word)
        obj_spider.urls.old_urls = set()
