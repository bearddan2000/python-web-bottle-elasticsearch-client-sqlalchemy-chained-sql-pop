from bottle import run
from node import  Node

if __name__ == "__main__":
    Node('elasticsearch')    
    run(host ='0.0.0.0', port = 8000, debug = True)
