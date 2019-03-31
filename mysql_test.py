from model import OperateMySQL
import MySQLdb
url = "localhost"
username = "root"
pwd = "6964433"
dbname = "jinyong"
db = MySQLdb.connect(url, username, pwd, dbname, charset='utf8')
cursor = db.cursor()
filename = 'novel.txt'
#filename = 'name.txt'
efile=[]
with open(filename,'r') as file_read:
    while True:
        lines = file_read.readline()
        if not lines:
            break
        efile.append(lines)

for i in efile:
    print(i)
    #cursor.execute("INSERT INTO relation (Names) values ('%s')" %(i))
    cursor.execute("INSERT INTO novel (NovelName) values ('%s')" %(i))
    db.commit()

cursor.execute("select * from relation")
res = cursor.fetchall()
print res

