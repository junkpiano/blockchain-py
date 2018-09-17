#!/usr/bin/env python

import hashlib, json, sys

def hashMe(msg = ""):
    if type(msg) != str:
        msg = json.dump(msg, sort_keys=True)

    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(msg).hexdigest(), 'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()

class Block:
    def __init__(self, index, previousHash, timestamp, data, hash):
        self.index = Index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
