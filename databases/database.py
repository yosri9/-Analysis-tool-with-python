import sqlite3

from api import ApiUtilities
from databases.models import Exchange


class Database():
    def analysisToolDatabase():
        conn = sqlite3.connect("analysis-tool.db")
        c = conn.cursor()
        sql_create_exchanges_table = """CREATE TABLE IF NOT EXISTS exchanges (
                                                    id integer PRIMARY KEY AUTOINCREMENT,
                                                    name text NOT NULL,
                                                    ip_address text NOT NULL,
                                                    username text NOT NULL,
                                                    password text NOT NULL



                                                );"""
        sql_create_bugs_table = """CREATE TABLE IF NOT EXISTS bugs (
                                                            id integer PRIMARY KEY AUTOINCREMENT,
                                                            repetition text NOT NULL,
                                                            level text NOT NULL,
                                                            description text NOT NULL

                                                        );"""
        sql_create_bug_exchanges_table = """CREATE TABLE IF NOT EXISTS bug_exchanges (
                                                            bug_id integer NOT NULL,
                                                            exchange_id integer NOT NULL,
                                                            FOREIGN KEY (bug_id) REFERENCES  bugs(id), 
                                                            FOREIGN KEY (exchange_id) REFERENCES  exchanges(id),
                                                            UNIQUE (bug_id, exchange_id)

                                                        );"""

        c.execute(sql_create_bugs_table)
        c.execute(sql_create_exchanges_table)
        c.execute(sql_create_bug_exchanges_table)


    def insert( model ):
        print(model.toList())
        if model.table() != "bug_exchanges":
            sql_insert_element = "INSERT INTO " + model.table() + " VALUES  (NULL"
            for i in range(1, len(model.toList())):
                sql_insert_element = sql_insert_element + ",\"" + str(model.toList()[i]) + "\""
        else:
            sql_insert_element = "INSERT INTO " + model.table() + " VALUES  ("

            sql_insert_element = sql_insert_element +   str(model.toList()[0]) + " ," +str(model.toList()[1])
        sql_insert_element = sql_insert_element + ")"

        conn = sqlite3.connect("analysis-tool.db")
        db = conn.cursor()

        print(sql_insert_element)
        db.execute(sql_insert_element)
        conn.commit()

        db.close()
        conn.close()


    def update(self , model):
        conn = sqlite3.connect("analysis-tool.db")
        db = conn.cursor()
        # TODO: update 2 table
        sql_update_row = "UPDATE" + model.table()  +"SET+" + model.toMap().items + "WHERE id = " + model.getID
        db.execute( sql_update_row , model.toMap().items() )

    def bugExchangedelete( model):
        conn = sqlite3.connect("analysis-tool.db")
        db = conn.cursor()
        sql_delete_row = "DELETE FROM "+ model.table() + " WHERE( bug_id = " + str(model.getBugID()) + " and exchange_id = "+ str(model.getExchangeID()) +")"
        print(sql_delete_row)
        db.execute(sql_delete_row )
        conn.commit()
        db.close()
        conn.close()
    def delete(model):
        conn = sqlite3.connect("analysis-tool.db")
        db = conn.cursor()
        sql_delete_row = "DELETE FROM " + model.table() + " WHERE( id = " +str(model.getID()) +" )"
        print(sql_delete_row)
        db.execute(sql_delete_row)
        conn.commit()
        db.close()
        conn.close()
    def getByID(model , bugID):
        conn = sqlite3.connect("analysis-tool.db")
        db = conn.cursor()
        sql_get_row = "SELECT * FROM " + model.table() + " WHERE ID = "+str(bugID)
        print(sql_get_row)
        db.execute(sql_get_row)
        rows = db.fetchone()
        db.close()
        conn.close()

        return rows
    def getBug(model):
        conn = sqlite3.connect("analysis-tool.db")
        db = conn.cursor()
        sql_get_row = "SELECT * FROM " + model.table() + " WHERE ( level = \"" + model.getLevel() + "\" and description = \""+ model.getDescription() + "\")"
        print(sql_get_row)
        db.execute(sql_get_row)
        row = db.fetchone()
        db.close()
        conn.close()
        return row


    def getAll(  model ):
        conn = sqlite3.connect("analysis-tool.db")
        db = conn.cursor()
        sql_get_all_rows ="SELECT * FROM " +model.table()
        print(sql_get_all_rows)
        db.execute(sql_get_all_rows )
        rows = db.fetchall()
        db.close()
        conn.close()

        return rows
    def getBugExchangeIDByExchangeID(model , exchangeID):
        conn = sqlite3.connect("analysis-tool.db")
        db = conn.cursor()
        sql_get_rows = "SELECT * FROM " + model.table() + " WHERE exchange_id = "+str(exchangeID)
        print(sql_get_rows)
        db.execute(sql_get_rows)
        rows = db.fetchall()
        db.close()
        conn.close()

        return rows
    def exist(  model ):
        conn = sqlite3.connect("analysis-tool.db")
        db = conn.cursor()
        sql_bug_existance =" SELECT EXISTS(SELECT * from bug_exchanges WHERE bug_id= " + str(model.getID()) +"); "
        print(sql_bug_existance)
        db.execute(sql_bug_existance )
        exist = db.fetchone()
        db.close()
        conn.close()

        return exist




