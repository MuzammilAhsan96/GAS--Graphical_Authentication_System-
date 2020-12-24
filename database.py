import mysql.connector
#import emp_master_GUI


class database:
    con = None

    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="imanpass12",
                                               database="gas_database")
        except Exception as ex:
            print(ex)

    def universal_Transact(self, query, val):
        is_success = 0
        try:
            curr = self.con.cursor()
            curr.execute(query, val)
            if curr.rowcount > 0:
                is_success = 1
        except Exception as ex:
            print(ex)
        finally:
            self.con.commit()
            self.con.close()
        return is_success

    def universal_getdata(self, query):
        datalist = None
        try:
            curr = self.con.cursor()
            curr.execute(query)
            datalist = curr.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            self.con.commit()
            self.con.close()
        return datalist
