#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socketserver
import os
import json
import struct
import sys

dict_file_path = ""

def sendRealFile(conn, srcfile):
    '''发送真是文件'''
    with open(srcfile, 'rb')as f:
        conn.sendall(f.read())

def sendEndFlag(conn):
    conn.sendall(struct.pack('i', 0) )
    print('>>All File Send Out')

def operafile(srcfile):
    '''对报头进行打包'''
    filename = os.path.basename(srcfile)
    filesize_bytes = os.path.getsize(  srcfile )
    head_dir = {
        'filename': filename,
        'filesize_bytes': filesize_bytes,
    }
    head_info = json.dumps(head_dir)
    head_info_len = struct.pack('i', len(head_info))
    return head_info_len, head_info

class MyServer(socketserver.BaseRequestHandler):
    buffsize = 1024
    '''
    def handle(self):
        # ready file real name
        print('>>Socket Connection' , self.request , self.client_address)

        file_path = os.path.join( os.getcwd() ,UPADATE_FILE_DIR_NAME)
        for dir_path, dir_name, file_names in os.walk(file_path):
            for file_name in file_names:
                srcfile = os.path.join(file_path, file_name)
                print('>>[', file_name, '] send start')

                head_info_len, head_info = operafile( srcfile)
                self.request.send(head_info_len)  # 这里是4个字节
                self.request.send(head_info.encode('utf-8'))  # 发送报头的内容
                sendRealFile(self.request, srcfile)
        else:
            sendEndFlag(self.request)
    '''

    def handle(self):
        # ready file real name
        print('>>Socket Connection' , self.request , self.client_address)
        global dict_file_path
        load_dict = []
        with open(dict_file_path, "r", encoding='utf-8') as load_f:
            load_str = load_f.read()
            load_dict = json.loads(load_str)

        for file_src in load_dict:
            print('>>[', file_src, '] Operater ')

            head_info_len, head_info = operafile( file_src)
            self.request.send(head_info_len)  # 这里是4个字节
            self.request.send(head_info.encode('utf-8'))  # 发送报头的内容
            sendRealFile(self.request, file_src)
        else:
            sendEndFlag(self.request)


class ServerImpl:

    @staticmethod
    def serve_forever( _dict_file_path ):
        print('>>Server Start')

        global dict_file_path
        dict_file_path = _dict_file_path

        s = socketserver.ThreadingTCPServer(("127.0.0.1", 9000), MyServer)  # 多线程
        #   服务器一直开着
        s.serve_forever()
