from abc import ABC,abstractmethod
import dataObjects.dbConfig as cfg
import sqlite3

class saveable(ABC):


    def getCursor(self):
        return sqlite3.connect(cfg.conn['path']).cursor()

    def cleanup(self, cur):
        cur.connection.commit()
        cur.connection.close()

    @abstractmethod
    def save(self):
        pass

