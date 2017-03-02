# -*- coding: utf-8 -*-
from sql import Sql

class WeiboPipeline(object):
    def process_item(self, item, spider):
        NickName = item['NickName']
        ret = Sql.select_name(NickName)
        if ret[0] == 1:
            print('已经存在了')
            pass
        else:
            NickName = item['NickName']
            Gender = item['Gender']
            City = item['City']
            Signature = item['Signature']
            Birthday = item['Birthday']
            Num_Tweets = item['Num_Tweets']
            Num_Follows = item['Num_Follows']
            Num_Fans = item['Num_Fans']
            Sex_Orientation = item['Sex_Orientation']
            Marriage = item['Marriage']
            URL = item['URL']
            Sql.insert_dd_name(NickName, Gender, City, Signature,Birthday,Num_Tweets,Num_Follows,Num_Fans,Sex_Orientation,Marriage,URL)
            print('开始存个人信息')



