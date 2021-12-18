import random
import string
# Password Manager class
class PassMan():
	# constructer
	def __init__(self):
		while True:
			self.site_name = str(input('Enter your site name : '))
			if self.site_name == '':
				print('Enter your site name ! ')
			else:
				break
		while True:
			self.name = str(input('Enter your username : '))
			if self.name == '':
				print('Enter your username ! ')
			else:
				break
		while True:
			self.email = str(input('Enter your email : '))
			if '@' and '.com' not in self.email:
				if self.email == '':
					print('Your email invalid ! ')
			else:
				break
		while True:
			self.lng = input('Enter your length of password : ')
			if str(self.lng) == '':
				print('Enter your length of pass ! ')
			else:
				self.lng = int(self.lng)
				break
	# a method for generate
	def password_generator(self):
		self.characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')
		random.shuffle(self.characters)
		self.password = []
		for i in range(self.lng):
			self.password.append(random.choice(self.characters))
		random.shuffle(self.password)
		self.final_pass = ''.join(self.password)
	# a method for generate code
	def code_gen(self):
		self.str_number = list(string.digits)
		random.shuffle(self.str_number)
		self.user_code = []
		for i in range(6):
			self.user_code.append(random.choice(self.str_number))
		random.shuffle(self.user_code)
		self.final_user_code = ''.join(self.user_code)
	# a method for return name , email & pass
	def information(self):
		self.user_information = []
		self.user_information.append(self.name)
		self.user_information.append(self.email)
		self.user_information.append(self.site_name)
		self.user_information.append(self.final_pass)
		self.user_information.append(self.final_user_code)
		return self.user_information

