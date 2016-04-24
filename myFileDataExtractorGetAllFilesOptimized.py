#!/usr/bin/python2.7

#trying to extract some data out of a snmp file.

#open the file

#print 'hello, world'
# Well, I guess I can still program in python. NOT!

import sqlite3
import sys
import os
import fnmatch
import glob
import formic
import zlib
import gzip




import errno

count = 0
countAllLines = 0
countC1 = 0
countC2 = 0
countF1 = 0

ifInUcastPktsTotal = 0
ifInErrorsTotal = 0
ifInDiscardsTotal = 0
ifOutUcastPktsTotal = 0
ifOutErrorsTotal = 0
ifOutDiscardsTotal = 0

conn = sqlite3.connect('contentSNMPmini.sqlite')
cur = conn.cursor()
conn.text_factory = str

# 9-ifInUcastPkts  , 10-ifInErrors  ,  11-ifInDiscards  ,  13-ifOutUcastPkts  ,  14-ifOutErrors  ,  15-ifOutDiscards
cur.execute('''DROP TABLE IF EXISTS WirelessFailure ''')
#cur.executescript('''DROP TABLE IF EXISTS WirelessFailure;''')
cur.execute('''CREATE TABLE IF NOT EXISTS WirelessFailure
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, ifInUcastPkts INTEGER, ifInErrors INTEGER, ifInDiscards INTEGER, ifOutUcastPkts INTEGER, ifOutErrors INTEGER, ifOutDiscards INTEGER)''')

while True:

    #path = '/Users/robinhood/aa-workspace-python/GMANE/fall03/031101/AcadBldg1AP1'
    #files = glob.glob(path)

    #walk the path through all the subdirectories
    fileset = formic.FileSet(include="**/*.gz", directory="/Users/robinhood/aa-workspace-python/GMANE/-CAPSTONE-SNMP/fall03/")
    for filename in fileset:
        count = count + 1
        print filename
        print count
        with gzip.open(filename, 'rb') as f:
            #file_content = f.read()
            for line in f:
            #print file_content
            #while True:
            #    for line in file_content:
                    #countAllLines = countAllLines + 1
                #print line
                '''
                if line.startswith("c1"):
                    countC1 = countC1 + 1
                    line = line.rstrip()
                    #print line

                    parts = line.split(',')
                    #print parts

                if line.startswith("c2"):
                    countC2 = countC2 + 1
                    line = line.rstrip()
                    #print line

                    parts = line.split(',')
                    #print parts
                '''

                if line.startswith("if"):
                    countF1 = countF1 + 1
                    line = line.rstrip()
                    # print line

                    parts = line.split(',')
                    #print parts
                    #print parts[8]
                    ifInUcastPkts = parts[8]
                    #print 'ifInUcastPkts: ', ifInUcastPkts
                    try:
                        ifInUcastPktsTotal = ifInUcastPktsTotal + int(ifInUcastPkts)
                    except ValueError:
                        pass
                    #print 'ifInUcastPktsTotal ',ifInUcastPktsTotal



                    ifInErrors = parts[9]
                    #print 'ifInErrors', ifInErrors
                    try:
                        ifInErrorsTotal = ifInErrorsTotal + int(ifInErrors)
                    except ValueError:
                        pass
                    #print 'ifInErrorsTotal ',ifInErrorsTotal



                    ifInDiscards = parts[10]
                    #print 'ifInDiscards', ifInDiscards
                    try:
                        ifInDiscardsTotal = ifInDiscardsTotal + int(ifInDiscards)
                    except ValueError:
                        pass
                    #print 'ifInDiscardsTotal ',ifInDiscardsTotal

                    ifOutUcastPkts = parts[12]
                    #print 'ifOutUcastPkts', ifOutUcastPkts
                    try:
                        ifOutUcastPktsTotal = ifOutUcastPktsTotal + int(ifOutUcastPkts)
                    except ValueError:
                        pass
                    #print 'ifOutUcastPktsTotal ',ifOutUcastPktsTotal

                    ifOutErrors = parts[13]
                    #print 'ifOutErrors', ifOutErrors
                    try:
                        ifOutErrorsTotal = ifOutErrorsTotal + int(ifOutErrors)
                    except ValueError:
                        pass
                    #print 'ifOutErrorsTotal ',ifOutErrorsTotal

                    ifOutDiscards = parts[14]
                    #print 'ifOutDiscards', ifOutDiscards
                    try:
                        ifOutDiscardsTotal = ifOutDiscardsTotal + int(ifOutDiscards)
                    except ValueError:
                        pass
                    #print 'ifOutDiscardsTotal ',ifOutDiscardsTotal


                    cur.execute('''INSERT OR IGNORE INTO WirelessFailure (ifInUcastPkts, ifInErrors, ifInDiscards, ifOutUcastPkts, ifOutErrors, ifOutDiscards)
                    VALUES (?, ?, ?, ?, ?, ? )''', (ifInUcastPkts, ifInErrors, ifInDiscards, ifOutUcastPkts, ifOutErrors, ifOutDiscards))

                    # conn.commit()
                    if (countF1 % 50) == 0 : conn.commit()




    break
conn.commit()
print '\nFiles: ',count
print 'f1 Lines: ',countF1
print 'ifInUcastPktsTotal: ',ifInUcastPktsTotal
print 'ifInErrorsTotal: ',ifInErrorsTotal
print 'ifInDiscardsTotal: ',ifInDiscardsTotal
print 'ifOutUcastPktsTotal: ',ifOutUcastPktsTotal
print 'ifOutErrorsTotal: ',ifOutErrorsTotal
print 'ifOutErrorsTotal: ',ifOutErrorsTotal
percentInPktsErrors = ifInErrorsTotal / float(ifInUcastPktsTotal)
percentOutPktsErrors = ifOutErrorsTotal / float(ifOutUcastPktsTotal)
percentInPktsDiscarded = ifInDiscardsTotal / float(ifInUcastPktsTotal)
percentOutPktsDiscarded = ifOutDiscardsTotal / float(ifOutUcastPktsTotal)
print 'percentInPktsErrors: %',percentInPktsErrors
print 'percentOutPktsErrors: %',percentOutPktsErrors
print 'percentInPktsDiscarded: %',percentInPktsDiscarded
print 'percentOutPktsDiscarded: %',percentOutPktsDiscarded



"""



        #time.sleep(1)

        print 'All Lines: ', countAllLines
        print 'c1 Lines: ', countC1
        print 'c2 Lines: ', countC2
        break
    f.close




extra code I might need

try:
            with open(name) as f: # No need to specify 'r': this is the default.
                sys.stdout.write(f.read())
        except IOError as exc:
            if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
                raise # Propagate other kinds of IOError.

OR

path = '/Users/robinhood/aa-workspace-python/GMANE/fall03/031101/*.gz'
        files=glob.glob(path)
        for file in files:
            print file
        break




    eachCompressedFile = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    #for f in fnmatch.filter(files, '*.snmp')]
    for f in files if f.endswith('.gz')]

    #for eachCompressedFile in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
    print eachCompressedFile

    fh=open(eachCompressedFile, 'r')

    # print '%s' % f.readlines()
    # f.close()
    #if you want to print only the filenames, use 'print file' instead of three previous lines




    try:
            fname = raw_input('Enter File Name: \n')
            if len(fname) == 0:
                fname = 'AcadBldg1AP1.snmp'

            if fname == "na na boo boo":
                print "NA NA BOO BOO TO YOU - You have been punk'd."
                exit()
            else:

                fh = open(fname)
                # print 'inside-else', fh

        except:
            print 'Bad File Name: ', fname
            exit()
"""