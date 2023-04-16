import logging, os
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.result import ChunkedIteratorResult

from model import DbModel

logging.basicConfig(level=logging.INFO)

INDEX_NAME = os.environ["INDEX_NAME"]

class Cluster():
    def __init__(self) -> None:
        self.hive = [
            Node("es1"),
            Node('es2'),
            Node('es3')
        ]

    def filter_query(self):
        for node in self.hive:
            node.filter_query()
    
    def get_all_query(self):
        for node in self.hive:
            node.get_all_query()
    
class Node():
    def __init__(self,server) -> None:
        self.server = server
        ELASTICSEARCH = {
            'engine': 'elasticsearch',
            'host': server,
            'port': 9200,
            'user': 'elastic',
            'password': 'changeme'
        }

        self.engine = create_engine("{engine}://{host}:{port}".format(**ELASTICSEARCH))
    
        self.session_local = sessionmaker(
            bind=self.engine
        )

    def get_db(self):
        db = self.session_local()
        try:
            yield db
        finally:
            db.close()

    def print_result(self, collection: ChunkedIteratorResult, func_name: str):
        for row in collection:
            for obj in row:
                logging.info("{} {}: {}".format(self.server,func_name, str(obj)))

    def filter_query(self):
        db = next(self.get_db())
        stm = select(DbModel).where(DbModel.id > 3)
        collection = db.execute(stm)
        self.print_result(collection, "filter_query")

    def get_all_query(self):
        db = next(self.get_db())
        stm = select(DbModel)
        collection = db.execute(stm)
        self.print_result(collection, "get_all_query")
