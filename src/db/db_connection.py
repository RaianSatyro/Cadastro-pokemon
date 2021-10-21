import json
import os

class DataBase():
    def init(self):
        self.cwd = os.getcwd()

    def open_in_read_mode(self):
        arquivo = open(f'{self.cwd}\src\db\db.json', 'r')
        db_json = json.loads(arquivo.read())
        arquivo.close()
        return db_json
#
    def insert_in_BD(self, objeto):
        try:
            db_json_list = self.open_in_read_mode()
            db_json_list.append(objeto)
            print(db_json_list)
            arquivo = open(f'{self.cwd}\src\db\db.json', 'w')
            arquivo.write(json.dumps(db_json_list))
            arquivo.close()
            return True
        except:
            return False

db = DataBase()