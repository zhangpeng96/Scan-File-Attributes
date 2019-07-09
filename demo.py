import os, shutil, hashlib
from sqlite import SQLite
from os import stat
from tprint import tprint
import datetime

def currentTs():
    ts_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    return ts_str    

def mts(ts):
    if isinstance(ts, str):
        ts = float(ts)
    ts_str = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S.%f')
    return ts_str

def get_md5(path):
    return hashlib.md5(open(path,'rb').read()).hexdigest()

def get_sha1(path):
    return hashlib.sha1(open(path,'rb').read()).hexdigest()


if __name__=='__main__':
    sqlite = SQLite('data.db')
    # sqlite.insert()
    while True:
        input_dir = input('Enter folder path: ')
        if isinstance(input_dir, str):
            work_dir = input_dir
            break
        else:
            pass
    # work_dir = 'D:\\共享区'
    for parent, dirnames, filenames in os.walk(work_dir,  followlinks=True):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            file_attr = stat(file_path)
            attr_list = [file_attr.st_mode, file_attr.st_uid, file_attr.st_gid, file_attr.st_size, file_attr.st_atime, file_attr.st_mtime, file_attr.st_ctime]
            name, ext = os.path.splitext(filename)

            sql = '''INSERT OR IGNORE INTO `files` (name, ext, filename, dirpath, filepath, md5, sha1, mode,
                     uid, gid, size, astime, mstime, cstime, uptime, atime, mtime,  ctime, remark) 
                     VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}',{7},{8},{9},{10},
                     '{11}','{12}','{13}','{14}',{15},{16},{17},'{18}')'''.format(
                        name, ext, filename, parent, file_path,
                        get_md5(file_path), get_sha1(file_path),
                        attr_list[0], attr_list[1], attr_list[2], attr_list[3],
                        mts(attr_list[4]), mts(attr_list[5]), mts(attr_list[6]), currentTs(),
                        attr_list[4], attr_list[5], attr_list[6], ''
                    )
            tprint('write_successfully', filename)
            sqlite.insert(sql)
            # print(attr_list)

