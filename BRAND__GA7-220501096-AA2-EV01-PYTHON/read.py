import psycopg2 
  
conn = psycopg2.connect( 
    database="your-database", user='postgres', 
    password='your-password', host='localhost', port='5432'
) 
  
conn.autocommit = True
cursor = conn.cursor() 

sql = '''
       SELECT * FROM products                
'''
  
cursor.execute(sql) 
  
conn.commit() 
conn.close() 