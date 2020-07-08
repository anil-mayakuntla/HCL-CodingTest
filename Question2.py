import pysftp
import csv
import MySQLdb

myhostname='' #Server name
myusername='' #Username
mypassword='' #Password

remoteFolderPath='' #Folder path in remote server
localFolderPath='' #Folder path in local machine for downloading

downloadedFiles=set()

dbhostname='' #db Server name
dbname='' #db name
dbusername='' #db username
dbpassword='' #db password

try:
    mydb=MySQLdb.connect(host=dbhostname, user=dbusername, password=dbpassword, db=dbname)
    cursor=mydb.cursor()

    with pysftp.Connection(host=myhostname, username=myusername, password=mypassword) as sftp:
        sftp.Connection.chdir(remoteFolderPath)
        flag=True
        while(flag):
            remoteFiles=set(sftp.listdir())
            newFiles=remoteFiles-downloadedFiles

            for nFile in newFiles:
                sftp.get(remoteFolderPath+nFile, localFolderPath+nFile)
                try:
                    with open(localFolderPath+nFile) as csv_file:
                        csv_reader=csv.reader(csv_file, delimiter=',')
                        line=0
                        for row in csv_reader:
                            if line==0:
                                continue
                                line+=1
                            else:
                                cursor.execute('INSERT INTO mytable(Result Time, Granularity Period, Object Name, Cell ID, CallAttemps) VALUES ("%s","%s","%s","%s","%s")', row)
                                mydb.commit()
                except OSError:
                    print('unable to open file '+nFile)
                finally:
                    downloadedFiles.add(nFile)
                    newFiles.remove(nFile)
                    
except:
    print('Some Error')
finally:
    cursor.close()