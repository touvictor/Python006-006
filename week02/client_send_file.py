#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: send.py
socket client
"""

import socket
import os
import sys
import struct


def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 6666))
    except socket.error as msg:
        print msg
        sys.exit(1)

    print s.recv(1024)

    while 1:
        filepath = raw_input('please input file path: ')
        if os.path.isfile(filepath):
            # 定義定義檔案資訊。128s表示檔名為128bytes長，l表示一個int或log檔案型別，在此為檔案大小
            fileinfo_size = struct.calcsize('128sl')
            # 定義檔案頭資訊，包含檔名和檔案大小
            fhead = struct.pack('128sl', os.path.basename(filepath),
                                os.stat(filepath).st_size)
            s.send(fhead)
            print 'client filepath: {0}'.format(filepath)

            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print '{0} file send over...'.format(filepath)
                    break
                s.send(data)
        s.close()
        break


if __name__ == '__main__':
    socket_client()
	