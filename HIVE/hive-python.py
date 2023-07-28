from pyhive import hive
host_name = "192.168.56.101"
port = 22
user = "cloudera"
password = "cloudera"
database="default"

select
=======
try:  
    conn = hive.Connection(host=host_name, port=port, username=user, password=password,
                           database=database, auth='CUSTOM')
    cur = conn.cursor()
    cur.execute('select *  from airqualityuci_duplicate limit 10')
    result = cur.fetchall()
    print(result)
except Exception as e:
    logging.error(str(e))
    
Join operation
================
from pyhive import hive
host_name = "192.168.56.101"
port = 22
user = "cloudera"
password = "cloudera"
database="hive_class_b1"

try:  
    conn = hive.Connection(host=host_name, port=port, username=user, password=password,
                           database=database, auth='CUSTOM')
    cur = conn.cursor()
    cur.execute('select * from customers c left join order o on c.id = o.CUSTOMER_ID')
    result = cur.fetchall()
    print(result)
except Exception as e:
    logging.error(str(e))
    
Drop Table operation
======================
from pyhive import hive
host_name = "192.168.56.101"
port = 22
user = "cloudera"
password = "cloudera"
database="hive_class_b1"


try:
    conn = hive.Connection(host=host_name, port=port, username=user, password=password,
                           database=database, auth='CUSTOM')
    cur = conn.cursor()
    cur.execute('drop table customers')
except Exception as e:
    logging.error(str(e))
    
Filter
=======
from pyhive import hive
host_name = "192.168.56.101"
port = 22
user = "cloudera"
password = "cloudera"
database="default"

try:  
    conn = hive.Connection(host=host_name, port=port, username=user, password=password,
                           database=database, auth='CUSTOM')
    cur = conn.cursor()
    cur.execute('select *  from airqualityuci_duplicate where date='31/12/2004')
    result = cur.fetchall()
    print(result)
except Exception as e:
    logging.error(str(e))