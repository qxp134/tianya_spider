#coding=utf-8
'''
Created on 2016��11��10��

@author: Administrator
'''
import mysql.connector


class Conenct(object):
    def keywords_list(self):
        conn = mysql.connector.connect(user='root', password='qxp1993816', database='keywords', use_unicode=True)
        # ��������
        cursor = conn.cursor()
        cursor.execute('select keyword from traffic_police')
        values = cursor.fetchall()
        for v in values:
            print v[0].encode('utf-8')
        # �ǵù�����
        cursor.close()
        conn.close()
        return values