import sqlite3
import os


class Tools():

    @staticmethod
    def createDb():

        # 如果路径下没有db文件，重新创建并插入示例数据
        if os.path.exists('mydata.db') == False:
            connect = sqlite3.connect('mydata.db')
            c = connect.cursor()
            c.execute('''create table mydata(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Website varchar(1000),
                username varchar(1000),
                passwd varchar(1000)
            );
            ''')
            connect.commit()
            c.execute("insert into mydata values(1,'qq','qq','test123')")
            connect.commit()
            connect.close()

    @staticmethod
    def getData():

        conn = sqlite3.connect('mydata.db')
        c = conn.cursor()
        cursor = c.execute('select * from mydata')

        data_list = []
        for row in cursor:
            temp_list = []
            temp_list.append(row[0])
            temp_list.append(row[1])
            temp_list.append(row[2])
            temp_list.append(row[3])
            data_list.append(temp_list)
        conn.close()
        return data_list

    @staticmethod
    def addData(website, username, passwd):

        connect = sqlite3.connect('mydata.db')
        c = connect.cursor()
        command = "insert into mydata values(null,'%s','%s','%s')" % (website, username, passwd)
        print(command)
        c.execute(command)
        connect.commit()
        connect.close()

    @staticmethod
    def editData(id, website, username, passwd):

        connect = sqlite3.connect('mydata.db')
        c = connect.cursor()
        print(1)
        command = "update mydata set website='%s',username='%s',passwd='%s' where id=%s" % (
        website, username, passwd, id)
        print(command)
        c.execute(command)
        connect.commit()
        connect.close()

    @staticmethod
    def delData(id):
        print(33333)
        connect = sqlite3.connect('mydata.db')
        c = connect.cursor()
        print(1)
        command = "delete from mydata where id = %s" % id
        print(command)
        c.execute(command)
        connect.commit()
        connect.close()