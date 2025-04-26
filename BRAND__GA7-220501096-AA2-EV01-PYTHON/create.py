import psycopg2 
  
conn = psycopg2.connect( 
    database="your-database", user='postgres', 
    password='your-password', host='localhost', port='5432'
) 
  
conn.autocommit = True
cursor = conn.cursor() 
  
sql = '''
       INSERT INTO products (name, description, image_url, price, discount_price,quantity, category_id, admin_id) 
       VALUES ('T-shirt', 'A comfortable cotton t-shirt', 'https://example.com/tshirt.jpg', 19.99, 14.99, 100, 1, 1),                     
'''
  
cursor.execute(sql) 
  
conn.commit() 
conn.close() 