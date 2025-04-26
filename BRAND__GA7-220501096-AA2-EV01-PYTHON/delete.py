import psycopg2 
  
conn = psycopg2.connect( 
    database="your-database", user='postgres', 
    password='your-password', host='localhost', port='5432'
) 
  
conn.autocommit = True
cursor = conn.cursor() 
  
# Debe incluir el ID del producto que desea actualizar y el nuevo valor de cada campo que desea cambiar.

sql = '''
       DELETE FROM products
       WHERE id=1;                    
'''
  
cursor.execute(sql) 
  
conn.commit() 
conn.close() 