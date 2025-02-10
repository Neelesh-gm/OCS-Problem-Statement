import hashlib
def hashof(s):
    return hashlib.md5(s.encode()).hexdigest()
