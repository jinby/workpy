#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
import os
import sys
import json
import struct

from Base.ProgressBar import *

#这里可以用os.makedirs
def CreateDirByFilePath( path_name ):
    dir_name = os.path.dirname(path_name)
    #print(dir_name)
    if os.path.exists( dir_name ) == True:
        return
    else:
        CreateDirByFilePath(dir_name)
        os.mkdir( dir_name )


def recv_file(head_dir, tcp_client):
    buffsize = 1024
    filename = head_dir['filename']
    filesize_b = head_dir['filesize_bytes']
    process_bar = ProgressBar.ProgressBar(filename, filesize_b)
    recv_len = 0
    recv_mesg = b''
    recv_name = os.path.join(os.path.dirname(sys.argv[0]), "recv",filename)
    CreateDirByFilePath( recv_name )
    f = open( recv_name, 'wb')
    while recv_len < filesize_b:
        if filesize_b - recv_len > buffsize:
            recv_mesg = tcp_client.recv(buffsize)
            recv_len += len(recv_mesg)
            f.write(recv_mesg)
        else:
            recv_mesg = tcp_client.recv(filesize_b - recv_len)
            recv_len += len(recv_mesg)
            f.write(recv_mesg)

        process_bar.move(recv_len)
    f.close()
    process_bar.end()

def recvallfile():
    tcp_client = socket(AF_INET, SOCK_STREAM)
    ip_port = (('127.0.0.1', 9000))
    tcp_client.connect_ex(ip_port)

    while True:
        '''收发循环'''
        struct_len = tcp_client.recv(4)  #  接受报头的长度
        struct_info_len = struct.unpack('i',struct_len)[0]  #   解析得到报头信息的长度
        if struct_info_len == 0 :
            break;
        head_info = tcp_client.recv(struct_info_len)   #    接受报头的内容
        head_dir = json.loads(head_info.decode('utf-8'))              #   将报头的内容反序列化
        # #   文件信息
        # filename = head_dir['filename']
        # filesize = head_dir['filesize_bytes']
        recv_file(head_dir, tcp_client)


if __name__ == '__main__':
    recvallfile()

