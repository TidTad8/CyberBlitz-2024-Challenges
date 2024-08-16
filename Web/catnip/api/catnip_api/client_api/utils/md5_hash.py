import hashlib

def md5_hash(input_string):
    input_bytes = input_string.encode('utf-8')
    hash_object = hashlib.md5()
    hash_object.update(input_bytes)
    
    hashed_string = hash_object.hexdigest()
    return hashed_string