import ftplib
from datetime import datetime as dt

FTPHOST="127.0.0.1"
FTPPORT="21"
FTPUSER="roka"
FTPPASS="imlujia100"
FTPHOME="~/ftproot/"

LASTTIME_DIR="20180930"
LASTTIME_FILE="t_AA123401_xxxx.dat"

tlasttime = dt.strptime(LASTTIME_DIR, '%Y%m%d')

ftp = ftplib.FTP()
ftp.connect(FTPHOST, FTPPORT)
ftp.login(FTPUSER, FTPPASS)

data = []

ftp.cwd(FTPHOME)         # change directory
#ftp.dir(data.append)
items = ftp.nlst()
print(items)

for subdir in items:
    tdate = dt.strptime(subdir, '%Y%m%d')
    print("chkdate:",str(tdate > tlasttime))
    if tdate >= tlasttime:
        print("OK")
    else:
        print("NG")

    ftp.cwd(FTPHOME + subdir)
    subfiles = ftp.nlst()
    print(subfiles)
    print('---')

    sorted = list()
    lines = []
    dirs = ftp.retrlines('LIST -lrt', lines.append)
    print(lines)
    for line in lines:
        print(line.split()[8])
#    times = list()
#    for dir in dirs:
#        print("dir:", dir)
#        times.append(dt.strptime(dir, '%m-%d-%y %I:%M%p'))
#        for i in range(0,len(times)):
#            for dir in dirs:
#                if dir.startswith(times[i]):
#                    sorted.append(dir)
#                    break

ftp.quit()

for line in data:
    print "-", line
