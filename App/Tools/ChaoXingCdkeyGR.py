import random
import sqlite3
import config
def ChaoXingCdkeyGenerate():
    key ='123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    tmp = []
    for i in range(32):
        tmp.append(random.choice(key))
    cdkey = ''.join(tmp)
    return cdkey


if __name__ =='__main__':
    conn = sqlite3.connect(config.databasePath)
    c = conn.cursor()
    for i in range(32):
        c.execute('insert into cdkeys (cdkey) values (?)', [ChaoXingCdkeyGenerate()])
        conn.commit()
