import sqlite3

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
        c.execute(sql_create_bugs_table)
        c.execute(sql_create_exchanges_table)


    def insert( model ):
        sql_insert_element = "INSERT INTO " + model.table() + " VALUES  (NULL"
        for i in range(1, len(model.toMap())):
            print (model.toMap())
            sql_insert_element = sql_insert_element + ",\"" + model.toMap()[i]+ "\""
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

    def delete( model):
        conn = sqlite3.connect("analysis-tool.db")
        db = conn.cursor()
        sql_delete_row = "DELETE FROM "+ model.table() + " WHERE id = " + str(model.getID())
        print(sql_delete_row)
        db.execute(sql_delete_row )
        conn.commit()
        db.close()
        conn.close()
    def getAll(  model=Exchange() ):
        conn = sqlite3.connect("analysis-tool.db")
        db = conn.cursor()
        sql_get_all_rows ="SELECT * FROM " +model.table()
        print(sql_get_all_rows)
        db.execute(sql_get_all_rows )
        rows = db.fetchall()
        db.close()
        conn.close()

        return rows


