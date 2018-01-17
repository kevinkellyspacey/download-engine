#!/usr/bin/env python3
import subprocess
import re
import time
def download_engine(url='',path=''):
    #axel CMD
    CMD = ['axel','-n','10','http://old-releases.ubuntu.com/releases/16.04.1/ubuntu-16.04-desktop-amd64.iso']
    with subprocess.Popen(CMD,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) as output:
        for line in output.stdout:
            if line.startswith('['):
                # print("Line:",line)
                pecent,speed = filter(line)
                if pecent and speed:
                    print("percent:",pecent,"\t","speed:",speed)
                # time.sleep(1)


def filter(line):
    '''[  5%]  .......... .......... .......... .......... ..........  [1841.3KB/s]
       [ 10%]  .......... .......... .......... .......... ..........  [3930.6KB/s]'''
    # print("Filter:",line)
    pattern = re.compile(r'^\[\s+(.*)\]\s+\.\W+\.\s+\[\s*(.*)]$')
    try:
        pecent = pattern.match(line).expand(r'\1')
        speed = pattern.match(line).expand(r'\2')
        return pecent,speed
    except:
        print(line)
        return None,None
    # finally:
    #     if pecent:
    #         return pecent,None
    # try:
    #     fragment = line.split()
    #     percent = fragment[1].split(']')[0]
    #     print(percent)
    #     speed = fragment[-1].split('[')[1].split(']')[0]
    #     print(speed)
    #     return percent,speed
    # except:
    #     # pass
    #     print(line)

if __name__ == '__main__':
    download_engine()
    # filter("[  5%]  .......... .......... .......... .......... ..........  [1841.3KB/s]")