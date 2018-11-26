# coding:utf-8
from Base.Socket_Server import ServerImpl
from CdgRegHelp import *
import os
import sys

if __name__ == '__main__':
    CdgRegHelp.WriteCdgKey()
    json_path = os.path.join(os.path.dirname(sys.argv[0]),"Base/record.json")
    ServerImpl.serve_forever(json_path)