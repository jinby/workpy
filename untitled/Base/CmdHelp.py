
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import shutil
import sys, getopt
import json
import os

if __name__ == '__main__':

    load_dict = []
    print(sys.argv)
    json_path = os.path.join(os.path.dirname(sys.argv[0]) , "record.json")
    print(json_path)

    if os.path.exists( json_path ):
        with open( json_path , "r" , encoding='utf8') as load_f:
            load_str = load_f.read()
            load_dict = json.loads( load_str )

    if len(sys.argv) > 1 :
        print(sys.argv)
        try:
            opts, args = getopt.getopt(sys.argv[1:],"f:ct:", ["file=", "clear","to="])
        except getopt.GetoptError:
            print('test.py -f <file> --file=<file> -c --clear -t --to=<dir>')
            sys.exit(2)

        print(opts)
        for o, a in opts:
            if o in ("-f", "--file"):
                realpath = str(a).replace("\\", "/")
                if  not realpath in load_dict:
                    load_dict.append(realpath)
                print(load_dict)

            if o in ("-c", "--clear"):
                load_dict.clear()

            if o in ("-t", "--to"):
                for path in load_dict:
                    #path = path.replace("\\", "/")
                    #a = str(a).replace("\\", "/")
                    if not os.path.isfile(path):
                        continue
                    name = os.path.basename(path)
                    path_to = os.path.join(a , name)

                    if (os.path.exists(path_to)):
                        for i in range(100):
                            bkfile = "bk_%d_%s" % (i, name)
                            if (not os.path.isfile( os.path.join(a, bkfile) ) ):
                                os.rename(path_to, os.path.join(a, bkfile))
                                break
                    print( path, path_to)
                    shutil.copy2(path, path_to)

        with open( json_path, "w",encoding='utf-8') as f:
            load_str = json.dumps(load_dict, ensure_ascii=False)
            f.write(load_str)






