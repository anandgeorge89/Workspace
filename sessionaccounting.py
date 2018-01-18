import sqlite3
import datetime
hostname = 'localhost'
username = 'ageorge'
password1 = '8aSkn+Y&L@5ApN$N'
database = 'sms'
Tunport = '9999'
# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()
    command = "SELECT id, tstamp, accounting_session_id, device_mac, service_tier_code,service_id, flight_identity, device_category, accounting_type,octets_rx, octets_tx, packets_rx, packets_tx, session_time, tail_id,wan_ip_address, active_modem_mac_address, device_type, user_agent FROM rbo.session_accounting where tail_id = 'N324RA' ORDER BY tstamp desc limit 10000000"
    #command = "SELECT FROM rbo.session_accounting where tail_id = 'N324RA'  ORDER BY tstamp desc limit 100"
    cur.execute( command )
    rows = list(cur.fetchall())
    wanipmapping = {}
    Finallist = []
    AggregateList = []
    starttime = 1
    endtime = 2
    bucketsize = 600 
    for row1 in rows:
        row = list(row1)
        #print (row)
        if (row[15] != " ") and (row[15] != None):
            #print (row[15])
            wanipmapping[row[3]] = row[15]
            #print (wanipmapping)
    for row1 in rows:
        row = list(row1)
        if (row[15] != " ") or (row[15] != None):
            row[15] = wanipmapping[row[3]]
            print (row[15])
            row[1]= int(row[1].timestamp())
            Finallist.append(row)
        #row[]
        #listrow = list(row)
        #listrow[1]= int(listrow[1].timestamp())
        #print (row[1][1])
    print ("FinalListlength \n")
    print (len(Finallist))

    for timeslice in range (starttime,endtime,bucketsize):
        for wanip in wanipmapping.itervalues():
	    totalRxBytes =0
	    totalTxBytes =0
	    prevRxByte=0
	    prevTxByte=0
            for elementslist in Finallist
		if (elementslist[15] == wanip) and (elementslist[1]<timeslice+bucketsize):
		    if prevRxByte < elementslist[9]:
			totalRxBytes = totalRxBytes + (elementslist[9]-prevRxByte)
			totalTxBytes = totalTxBytes + (elementslist[10]-prevTxByte)
		    else:
			totalRxBytes = totalRxBytes + elementslist[9]
			totalTxBytes = totalTxBytes + elementslist[10]
		prevRxByte = elementslist[9]
		prevRxByte = elementslist[10]
		
		else:
		    break
	    AggregateBucket=dict{}
	    AggregateBucket["wanip"]=wanip
	    AggregateBucket["starttime"]=starttime
            AggregateBucket["endtime"]=endtime
            AggregateBucket["totalRxBytes"]=totalRxBytes
	    AggregateBucket["totalTxBytes"]=totalTxBytes
	    
	    AggregateList.append(AggregateBucket)

    print (AggregateList)

              




print ("Using psycopg2…")
import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password1, dbname=database, port=Tunport )
doQuery( myConnection )
myConnection.close()

#iprint "Using PyGreSQL…"
#import pgdb
#myConnection = pgdb.connect( host=hostname, user=username, password=password, database=database )
#doQuery( myConnection )
#myConnection.close()
