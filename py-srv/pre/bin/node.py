import logging
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient

from settings import configurations
from data import DOC, INDEX_NAME

logging.basicConfig(level=logging.INFO)

class Cluster():
    def __init__(self) -> None:
        self.hive = [
            Node("es1"),
            Node('es2'),
            Node('es3')
        ]
    
class Node():
    def __init__(self,server) -> None:
        self.server = server

        es = Elasticsearch(
            server + ":9200",
            http_auth=["elastic", "changeme"],
        )

        client = IndicesClient(es)

        try:
            client.create(index=INDEX_NAME, body=configurations)
        except:
            logging.warn(server + " already has index")
            pass

        self.print_index(es)

    def print_index(self, es:Elasticsearch):
        for record in DOC:
            resp=es.index(index=INDEX_NAME, id=record['id'], document=record)
            logging.info("{} print_index: {}".format(self.server, resp['result']))

