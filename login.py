user = raw_input("Username: ")

import getpass

sandi = getpass.getpass()

if sandi == 'akujomblo' and user == 'errorsystem':

	print "Kamu Berhasil Login"
	
else:

	print "Username atau Password Salah !"