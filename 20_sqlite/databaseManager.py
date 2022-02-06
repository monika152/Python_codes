import sqlite3


class DatabaseManager:
    def __init__(self,db_path) -> None:
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()


    def __insert_data(self,sql,data):
        self.cursor.execute(sql,data)
        self.conn.commit()

    print("Successfully !!")     


    def __select_data(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        return result

    def add_food(self,data):
        sql_insert = """INSERT INTO FOOD(Title,Price) VALUES(?,?)"""
        self.__insert_data(sql_insert,data)

    def get_list_foods(self):
        sql_select = """SELECT * FROM Food;"""
        return self.__select_data(sql_select)