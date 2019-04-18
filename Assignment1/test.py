import os
import time
FolderPath = './'
filelists = []
whitelist = ['py']


def getFile(basedir):
    global filelists
    for parent, dirnames, filenames in os.walk(basedir):
        for filename in filenames:
            ext = filename.split('.')[-1]
            if ext in whitelist:
                filelists.append(os.path.join(parent, filename))


def countLine(fname):
    count = 0
    inOuter = False
    for file_line in open(fname).readlines():
        if('\'\'\'' in file_line):
            inOuter = not inOuter
        if file_line.strip() != '' and not ('#' in file_line) and not inOuter:
            count += 1
    print(fname + '----', count)
    return count


if __name__ == '__main__':
    startTime = time.clock()
    getFile(FolderPath)
    totalline = 0
    for filelist in filelists:
        totalline = totalline + countLine(filelist)
    print('total lines:', totalline)
    print('Done! Cost Time: %0.2f second' % (time.clock() - startTime))
