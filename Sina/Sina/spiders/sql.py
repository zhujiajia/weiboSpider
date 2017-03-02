import mysql.connector


MYSQL_HOSTS ='127.0.0.1'
MYSQL_USER ='root'
MYSQL_PASSWORD = '1111'
MYSQL_PORT ='3306'
MYSQL_DB = 'weibo'

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor(buffered=True)



class Sql:
    @classmethod
    def insert_dd_name(cls, NickName, Gender, City, Signature,Birthday,Num_Tweets,Num_Follows,Num_Fans,Sex_Orientation,Marriage,URL):
        sql = 'INSERT INTO InformationItem (`NickName`, `Gender`, `City`, `Signature`,`Birthday`, `Num_Tweets`, `Num_Follows`, `Num_Fans`,`Sex_Orientation`,`Marriage`, `URL`) VALUES ' \
'(%(NickName)s, %(Gender)s, %(City)s, %(Signature)s),(%(Birthday)s, %(Num_Tweets)s, %(Num_Follows)s, %(Num_Fans)s,(%(Sex_Orientation)s, %(Marriage)s, %(URL)s)'
        value = {
            'NickName': NickName,
            'Gender': Gender,
            'City': City,
            'Signature': Signature,
            'Birthday': Birthday,
            'Num_Tweets': Num_Tweets,
            'Num_Follows': Num_Follows,
            'Num_Fans': Num_Fans,
            'Sex_Orientation': Sex_Orientation,
            'Marriage': Marriage,
            'URL': URL
        }
        print NickName, Gender, City, Signature,Birthday,Num_Tweets,Num_Follows,Num_Fans,Sex_Orientation,Marriage,URL
        cur.execute(sql, value)
        cnx.commit()
        print 'success'



    @classmethod
    def id_name(cls, NickName):
        sql = 'SELECT id FROM InformationItem WHERE NickName=%(NickName)s'
        value = {
            'NickName': NickName
        }
        cur.execute(sql, value)
        for name_id in cur:
            return name_id[0]

    @classmethod
    def select_name(cls, NickName):
        sql = "SELECT EXISTS(SELECT 1 FROM InformationItem WHERE NickName=%(NickName)s)"
        value = {
            'NickName': NickName
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def sclect_chapter(cls, url):
        sql = "SELECT EXISTS(SELECT 1 FROM dd_chaptername WHERE url=%(url)s)"
        value = {
            'url': url
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]


