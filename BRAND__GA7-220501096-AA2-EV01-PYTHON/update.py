import psycopg2 
  
conn = psycopg2.connect( 
    database="your-database", user='postgres', 
    password='your-password', host='localhost', port='5432'
) 
  
conn.autocommit = True
cursor = conn.cursor() 
  
# Debe incluir el ID del producto que desea actualizar y el nuevo valor de cada campo que desea cambiar.

sql = '''
       UPDATE products
       SET name = 'Updated T-shirt', description = 'An updated comfortable cotton t-shirt', price = 17.99, discount_price = 12.99, quantity = 150
       WHERE id = 1;                    
'''
  
cursor.execute(sql) 
  
conn.commit() 
conn.close() 