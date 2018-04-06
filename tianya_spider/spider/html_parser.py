# -*- coding: utf-8 -*-
'''
Created on 

@author: QXP
'''
import urlparse
import time

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_cont,count):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        if count == 1:
            new_data = {}
            new_data['url'] = page_url
            new_data['title'] = ''
            new_data['summary'] = ''
            new_data['time'] = time.localtime()
        else:
            new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('h3')#.find('a')#, href=re.compile(r"/view/\d+\.shtml"))
        for link in links:
            new_url = link.find('a')['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url

        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('span', class_= "s_title").find("span")
        res_data['title'] = title_node
        print title_node.get_text()
        time = ''
        timenode = soup.find('div', class_="atl-info")
        times = timenode.find_all('span')
        for i in times:
            time = time + i.get_text().encode('utf-8')
        res_data['time'] = time
        data1 = ''
        summary_nodes = soup.find_all('div', class_="atl-item")
        i = 0
        j = 1
        for summary_node in summary_nodes:
            step1 = summary_node.find('div',class_="atl-content")
            step2 = step1.find('div',class_="bbs-content")
            data1 = data1 + 'comment %d'%i + '\r\n'+ step2.get_text()   
            step3 = step1.find_all('span',class_="ir-content")
            for step4 in step3:
                data1 = data1 + 'reply %d'%j + '\r\n'+ step4.get_text()   
                j = j + 1
            i = i + 1
        res_data['summary'] = data1
        return res_data



