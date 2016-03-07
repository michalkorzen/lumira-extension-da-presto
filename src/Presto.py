# -*- coding: utf-8 -*-
#imports
import pprint
import socket
import easygui
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import exceptions

from pyhive import presto

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

Mode = enum('PREVIEW', 'EDIT', 'REFRESH')
mode = 0

paramslist = []
key = ''
i = 0
query = ''
items=''
msg = "Enter Required Information"
title = "Presto Connector"
fieldNames = ["Host", "Port", "Catalog", "Schema", "SQL Query"]

fieldValues = []  # we start with blanks for the values
for i in range(5):
    fieldValues.append(i)

try:
        extra_entropy = 'cl;ad13 \0al;323kjd #(adl;k$#ajsd'.encode('ascii')
except AttributeError:
        extra_entropy = 'cl;ad13 \0al;323kjd #(adl;k$#ajsd'

for i in range(len(sys.argv)):
    if str(sys.argv[i]).lower() == "-mode" and (i + 1) < len(sys.argv):
        if str(sys.argv[i + 1]).lower() == "preview":
            mode = Mode.PREVIEW
        elif str(sys.argv[i + 1]).lower() == "edit":
            mode = Mode.EDIT
        elif str(sys.argv[i + 1]).lower() == "refresh":
            mode = Mode.REFRESH
    elif str(sys.argv[i]).lower() == "-size":
        size = int(sys.argv[i + 1])
    elif str(sys.argv[i]).lower() == "-params":
        params = str(sys.argv[i + 1])
        paramslist = params.split(';')

    i += 1

def setArgs(fieldValues):

    fieldValues[0] = ''
    fieldValues[1] = ''
    fieldValues[2] = ''
    fieldValues[3] = ''
    fieldValues[4] = ''
    return fieldValues

def parseArgs(fieldValues):

    #if paramslist is None: break

    for i in range(len(paramslist)):
        if paramslist[i].split('=')[0].lower() == 'host':
            easygui.msgbox('param: %s' % paramslist[i].split('=')[1])
            fieldValues[0] = paramslist[i].split('=')[1]
        elif paramslist[i].split('=')[0].lower() == 'port':
            fieldValues[1] = paramslist[i].split('=')[1]
        elif paramslist[i].split('=')[0].lower() == 'catalog':
            fieldValues[2] = paramslist[i].split('=')[1]
        elif paramslist[i].split('=')[0].lower() == 'schema':
            fieldValues[3] = paramslist[i].split('=')[1]
        elif paramslist[i].split('=')[0].lower() == 'query':
            fieldValues[4] = paramslist[i].split('=')[1]
        i += 1
    return fieldValues

def getScreenInput(fieldValues):

    fieldValues = easygui.multenterbox(msg = msg, title = title, fields = fieldNames, values = fieldValues )
        # make sure that none of the fields was left blank
    while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg += ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "":
            break # no problems found
        fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)

    return fieldValues

def printData(fieldValues):

    if fieldValues != None:

        print "beginDSInfo"
        print """fileName;#;true
    csv_first_row_has_column_names;true;true;
    csv_separator;|;true
    csv_number_grouping;,;true
    csv_number_decimal;.;true
    csv_date_format;d.M.yyyy;true"""
        print ''.join(['host;', fieldValues[0], ';true'])
        print ''.join(['port;', fieldValues[1], ';true'])
        print ''.join(['catalog;', fieldValues[2], ';true'])
        print ''.join(['schema;', fieldValues[3], ';true'])
        print ''.join(['query;', fieldValues[4], ';true'])
        print "endDSInfo"
        print "beginData"
        try:
            cursor = presto.connect(host=fieldValues[0], port = fieldValues[1], catalog=fieldValues[2], schema=fieldValues[3]).cursor()
            cursor.execute(fieldValues[4])

            columns = [i[0] for i in cursor.description]
            print ', '.join(columns)

            for values in cursor.fetchall():
                print ', '.join(str(value).replace(',', '.') for value in values)

        except Exception, e:
            easygui.msgbox('failed because of %s' % e.message)
            print "Error"
            print "Failed"

        print("endData")

    else:
        print("beginDSInfo")
        print("endDSInfo")
        print("beginData")
        print("""Error
User Cancelled""")
        print("endData")

if mode == Mode.PREVIEW:
    fieldValues = setArgs(fieldValues)
    fieldValues = getScreenInput(fieldValues)
    printData(fieldValues)
elif mode == Mode.EDIT:
    fieldValues = parseArgs(fieldValues)
    fieldValues = getScreenInput(fieldValues)
    printData(fieldValues)
elif mode == Mode.REFRESH:
    fieldValues = parseArgs(fieldValues)
    printData(fieldValues)
