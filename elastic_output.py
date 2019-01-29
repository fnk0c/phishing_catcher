#!/usr/bin/python
#coding: utf-8

from elasticsearch import Elasticsearch
from datetime import datetime

def auth():
    HOST = "192.168.0.24"
    PORT = 9200
    USER = "elastic"
    PASS = "changeme"

    return(Elasticsearch(HOST, port=PORT, http_auth=(USER, PASS)))

def write(date, domain, keywords):#, blacklist):
    
    data = {"domain": domain,
            "date": date,
            "@timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "keyword": keywords
#            "blacklisted": blacklist
            }

    es = auth()
    es.index(index="phishing_catcher", doc_type="string", id=date, body=data)
