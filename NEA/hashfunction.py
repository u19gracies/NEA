import hashlib

hash = hashlib.sha256(b'test')

new = hash.hexdigest()