import hashlib

def get_md5(string: str) -> str:
    # 英文: Return MD5 hash of a given string
    # 中文: 返回给定字符串的 MD5 哈希值
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()
