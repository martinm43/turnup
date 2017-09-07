#-*-coding:utf8;-*-
#qpy:2
#qpy:console

def storeselect(range=5):
  import os
  cwd=os.getcwd()+'/'

  import sqlite3

  conn=sqlite3.connect(cwd+'lcbo_db.sqlite')
  c=conn.cursor()

  from location import coord_termux, coord_ip
  
  a=coord_termux()
  if a==None:
	print('GPS based locations from termux unsuccessful, using IP address: ')
	a=coord_ip()
  location_lat=str(a[0])
  location_lng=str(a[1])

  str_input='SELECT name, id AS distance FROM stores ORDER BY (('+location_lat+' - latitude)*('+location_lat+' - latitude)) + (('+location_lng+' - longitude)*('+location_lng+' - longitude)) ASC LIMIT '+str(range)
  g=c.execute(str_input).fetchall()

  return g
  
  
if __name__=='__main__':
  print storeselect()