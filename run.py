import os
import pyfiglet
from backend import PassMan
from database import UsersData
from colorama import Fore, Back, Style
# main function
def main():
	# for interface 
	print()
	print('****************************************************************')  
	print()
	print(Fore.RED + pyfiglet.figlet_format("Dirty - Hacker") + Style.RESET_ALL)
	print()
	print('****************************************************************')
	print("\n*          My github is : https://github.com/yasin-pro/        *")
	print()
	print('****************************************************************')
	print()
	# create a table in database
	db = UsersData()
	db.create_table()
	# question for reqister or login
	question = input('Are you want to (L)ogin or (R)egister ? ')
	if question == 'L' or question == 'l':
		# question for forget pass
		question_for_pass_forget = input('Are forget your password ? (Y) or (N) ')
		# process for recovering pass
		if question_for_pass_forget == 'Y' or question_for_pass_forget == 'y':
			email = str(input('Enter your email address : '))
			check_email = db.email_check(email)
			if check_email:
				password = str(input('Enter your new Password : '))
				db.update_into_table(password , email)
				print()
				print(Fore.GREEN+' [+] ' + Fore.GREEN+'Your password is changed successfuly ! '+Style.RESET_ALL)
				print()
			else:
				print()
				print(Fore.GREEN+' [+] ' + Fore.RED+'Your email not founded ! '+Style.RESET_ALL)
				print()
		# proccess for login
		elif question_for_pass_forget == 'N' or question_for_pass_forget == 'n':
			name = str(input('Enter your username : '))
			password = str(input('Enter your password : '))
			check = db.login_check(name,password)
			if check != '':
				print()
				print(Fore.GREEN+' [+] ' + Fore.GREEN+'Your logging proccess is successfuly ! '+Style.RESET_ALL)
				print()
				print(f'''

	Your information

	Your site name : {check[2]} 

	Your email : {check[1]}

	Your user_code : {check[4]}

			''')
			else:
				print()
				print(Fore.GREEN+' [+] ' + Fore.RED+'Your logging proccess is failed ! '+Style.RESET_ALL)
				print()
		else:
			print('Try again ! ')
	elif question == 'R' or question == 'r':
		# Call password manager class for save user information for reqister
		pass_man = PassMan()
		pass_man.password_generator()
		pass_man.code_gen()
		user_information = pass_man.information()
		# Save in database table
		db.insert_into_table(user_information[2],user_information[0],user_information[1] , user_information[3] ,user_information[4])
		print()
		print(Fore.GREEN+' [+] ' + Fore.GREEN+'Your reqister proccess is successfuly ! '+Style.RESET_ALL)
		print()
		print(f'''

	Your information

	Your username : {user_information[0]}

	Your site name : {user_information[2]} 

	Your email : {user_information[1]}

	Your password : {user_information[3]}

	Your user_code : {user_information[4]}

			''')
	else:
		print('Try again ! ')
# call main function
if __name__ == '__main__': main()