import sqlite3
import hashlib

# database class
class UsersData():
	# constructer and connect to sqlite databes
	def __init__(self):
		try:
			self.connect = sqlite3.connect('users_database.db')
			self.cursor = self.connect.cursor()
		except Exception as e :
			print(e)
	# a method for create table
	def create_table(self):
		qCreate = """
			CREATE TABLE IF NOT EXISTS usersTable (site_name varchar(200), name varchar(100) , email varchar(100) , password varchar(100) , user_code varchar(100))
		"""
		self.cursor.execute(qCreate)
		self.connect.commit()
	# a method for save information in table
	def insert_into_table(self, site_name, name , email , password , user_code):
		self.site_name = site_name
		self.name = name
		self.email = email
		self.password = password
		self.user_code = user_code
		qInsert = """
			INSERT INTO usersTable (site_name, name , email , password , user_code)
			VALUES (?, ? , ? , ? , ? )
		"""
		self.cursor.execute(qInsert, (self.site_name, self.name , self.email , self.password , self.user_code))
		self.connect.commit()
	# a method for update pass in forget
	def update_into_table(self , password , email):
		self.password = password
		self.email = email
		qUpdate = """
			UPDATE usersTable SET password = ? WHERE email = ?
		"""
		self.cursor.execute(qUpdate, (self.password, self.email))
		self.connect.commit()
	# a method for check email to exist
	def email_check(self , email):
		self.email = email
		qSelect = """
			SELECT * FROM usersTable
		"""
		self.cursor.execute(qSelect)
		self.data = self.cursor.fetchall()
		for self.user_info in self.data:
			if self.email == self.user_info[2]:
				return True
		return False
	# a method for login
	def login_check(self , name , password):
		self.password = password
		self.name = name
		qSelect = """
			SELECT * FROM usersTable
		"""
		self.cursor.execute(qSelect)
		self.data = self.cursor.fetchall()
		for self.user_info in self.data:
			if self.password == self.user_info[3]:
				if self.name == self.user_info[0]:
					return self.user_info
		return ''
