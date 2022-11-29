import boto3
import pymysql

# Retrieving the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Listing the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    name = bucket["Name"]
    print(f'  {name}')

'''
# To download a file from S3
s3. download_file('sels307', 'small_data.csv', 'download.csv')
print("Downloaded successfully")
'''

resp = s3.get_object(Bucket='sels307', Key='small_data.csv')

data = resp['Body'].read().decode('utf-8')
data = data.split("\n")
print(data)
print("Moving to RDS")

# rds_endpoint  = "selrds.c6z3we72kkmn.ap-south-1.rds.amazonaws.com"
# username = "admin"
# password = "*****" # RDS Mysql password
# db_name = "sel_aws" # RDS MySQL DB name
conn = None
try:
    conn = pymysql.connect(host='selrds.c6z3we72kkmn.ap-south-1.rds.amazonaws.com',
                           user='admin',
                           password='*****',
                           database='sel_aws',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor
                           )
    print("connection is successful")
except pymysql.MySQLError as e:
    print("ERROR: Unexpected error: Could not connect to MySQL instance.")

try:
    cur = conn.cursor()
    print("dropping old table")
    cur.execute("drop table Employees")
    conn.commit()
    print("Creating table Employees")
    cur.execute("create table Employees ( id INT NOT NULL AUTO_INCREMENT, Name varchar(255) NOT NULL, PRIMARY KEY (id))")
    conn.commit()
except:
    pass

with conn.cursor() as cur:
    for emp in data:  # Iterate over S3 csv file content and insert into MySQL database
        try:
            emp = emp.replace("\n","").split(",")
            emp_name = emp[1].split('\r')
            if emp_name[0] == "name":
                pass
            else:
                cur.execute('insert into Employees (Name) values("'+str(emp_name[0])+'")')
                conn.commit()
        except:
            continue

    cur.execute("select * from Employees")
    res = cur.fetchall()
    print("Printing records")
    for x in res:
        print(x)
    cur.execute("select count(*) from Employees")
    print("Total records on DB :"+str(cur.fetchall()[0]))

if conn:
    conn.commit()
