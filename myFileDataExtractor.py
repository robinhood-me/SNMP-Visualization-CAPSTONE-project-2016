#!/usr/bin/python2.7

#trying to extract some data out of a snmp file.

#open the file

#print 'hello, world'
# Well, I guess I can still program in python. NOT!

import sqlite3

countAllLines = 0
countC1 = 0
countC2 = 0
countF1 = 0

conn = sqlite3.connect('contentSNMP.sqlite')
cur = conn.cursor()
conn.text_factory = str

# 9-ifInUcastPkts  , 10-ifInErrors  ,  11-ifInDiscards  ,  13-ifOutUcastPkts  ,  14-ifOutErrors  ,  15-ifOutDiscards

cur.execute('''CREATE TABLE IF NOT EXISTS WirelessFailure
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, ifInUcastPkts INTEGER, ifInErrors INTEGER, ifInDiscards INTEGER, ifOutUcastPkts INTEGER, ifOutErrors INTEGER, ifOutDiscards INTEGER)''')


while True:
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
    fh = open(fname)
    # print 'non-else', fh

    ifInUcastPktsTotal = 0
    ifInErrorsTotal = 0
    ifInDiscardsTotal = 0
    ifOutUcastPktsTotal = 0
    ifOutErrorsTotal = 0
    ifOutDiscardsTotal = 0

    for line in fh:
        countAllLines = countAllLines + 1
        # print line

        if line.startswith("c1"):
            countC1 = countC1 + 1
            line = line.rstrip()
            print line

            parts = line.split(',')
            print parts

        if line.startswith("c2"):
            countC2 = countC2 + 1
            line = line.rstrip()
            print line

            parts = line.split(',')
            print parts

# 9-ifInUcastPkts  , 10-ifInErrors  ,  11-ifInDiscards  ,  13-ifOutUcastPkts  ,  14-ifOutErrors  ,  15-ifOutDiscards

        if line.startswith("if"):
            countF1 = countF1 + 1
            line = line.rstrip()
            #print line

            parts = line.split(',')
            #print parts
            #print parts[8]
            ifInUcastPkts = parts[8]
            print 'ifInUcastPkts: ', ifInUcastPkts
            ifInUcastPktsTotal = ifInUcastPktsTotal + int(ifInUcastPkts)
            print 'ifInUcastPktsTotal ',ifInUcastPktsTotal



            ifInErrors = parts[9]
            print 'ifInErrors', ifInErrors
            ifInErrorsTotal = ifInErrorsTotal + int(ifInErrors)
            print 'ifInErrorsTotal ',ifInErrorsTotal



            ifInDiscards = parts[10]
            print 'ifInDiscards', ifInDiscards
            ifInDiscardsTotal = ifInDiscardsTotal + int(ifInDiscards)
            print 'ifInDiscardsTotal ',ifInDiscardsTotal

            ifOutUcastPkts = parts[12]
            print 'ifOutUcastPkts', ifOutUcastPkts
            ifOutUcastPktsTotal = ifOutUcastPktsTotal + int(ifOutUcastPkts)
            print 'ifOutUcastPktsTotal ',ifOutUcastPktsTotal

            ifOutErrors = parts[13]
            print 'ifOutErrors', ifOutErrors
            ifOutErrorsTotal = ifOutErrorsTotal + int(ifOutErrors)
            print 'ifOutErrorsTotal ',ifOutErrorsTotal

            ifOutDiscards = parts[14]
            print 'ifOutDiscards', ifOutDiscards
            ifOutDiscardsTotal = ifOutDiscardsTotal + int(ifOutDiscards)
            print 'ifOutDiscardsTotal ',ifOutDiscardsTotal


            cur.execute('''INSERT OR IGNORE INTO WirelessFailure (ifInUcastPkts, ifInErrors, ifInDiscards, ifOutUcastPkts, ifOutErrors, ifOutDiscards)
            VALUES (?, ?, ?, ?, ?, ? )''', (ifInUcastPkts, ifInErrors, ifInDiscards, ifOutUcastPkts, ifOutErrors, ifOutDiscards))

            conn.commit()
            #time.sleep(1)

    print 'All Lines: ', countAllLines
    print 'c1 Lines: ', countC1
    print 'c2 Lines: ', countC2
    break




