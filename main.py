import mysql.connector as mc


conn= mc.connect(host='localhost',user='root',password='Ramailo2.',db='pythonSQL')
def read_data():
    cursor = conn.cursor()
    cursor.execute('show databases')
    databases = cursor.fetchall()
    for db_list in databases:
     print(db_list[0])

def main():
   read_data()

if __name__ == '__main__':
   main()