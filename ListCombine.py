#!/usr/bin/python3

import sys
import time
import argparse
import os
from termcolor import colored

final_list = []

def humanbytes(B):
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)

def generate_wordlist(args):
	# Open and read in first wordlist
	with open(args.wordlist) as f:
		words = []
		for line in f:
			words.append(line.strip())


		if (args.prepend and args.append):
			print('[*] Generating wordlist using method: {} and {} (This might take some time, depending on your wordlists...)'.format(colored('Prepending', 'yellow'), colored('Appending', 'yellow')))
			tmp_list = []
			password_list = []

			time1 = time.time()

			with open(args.prepend) as p, open(args.append) as a:
				for prepend in p:
					for word in words:
						_word = prepend.strip()+word.strip()

						if _word not in final_list:
							tmp_list.append(_word)

				for append in a:
					for word in tmp_list:
						_word = word.strip() + append.strip()
						if _word not in final_list:
							final_list.append(_word)

			time2 = time.time()
			print('[*] Generated ' + colored('{}'.format(len(final_list)), 'green') + ' passwords in ' + colored('{:02f}'.format((time2-time1)), 'green') + ' seconds')

		else:
			if args.prepend:
				print('[*] Generating wordlist using method: {} (This might take some time, depending on your wordlists...)'.format(colored('Prepending', 'yellow')))
				time1 = time.time()
				with open(args.prepend) as p:
					for prepend in p:
						for word in words:
							_word = prepend.strip()+word.strip()

							if _word not in final_list:
								final_list.append(_word)

				time2 = time.time()
				print('[*] Generated ' + colored('{}'.format(len(final_list)), 'green') + ' passwords in ' + colored('{:02f}'.format((time2-time1)), 'green') + ' seconds')

			if args.append:
				print('[*] Generating wordlist using method: {} (This might take some time, depending on your wordlists...)'.format(colored('Appending', 'yellow')))
				time1 = time.time()
				with open(args.append) as a:
					for append in a:
						for word in words:
							_word = word.strip()+append.strip()

							if _word not in final_list:
								final_list.append(_word)

				time2 = time.time()
				print('[*] Generated ' + colored('{}'.format(len(final_list)), 'green') + ' passwords in ' + colored('{:02f}'.format((time2-time1)), 'green') + ' seconds')

	with open(args.outfile, 'w') as w:
		_bytes = w.write('\n'.join(final_list))
		print('[*] Wordlist written to: ' + colored('{}'.format(args.outfile), 'green'))
		print('[*] Size of wordlist: ' + colored('{}'.format(humanbytes(_bytes)), 'green'))
		print('[*] Enjoy your password spraying! :)')

def main_screen():
	print('\n')
	print(colored("▄█        ▄█     ▄████████     ███      ▄████████  ▄██████▄    ▄▄▄▄███▄▄▄▄   ▀█████████▄   ▄█  ███▄▄▄▄      ▄████████", 'yellow'))
	print(colored("███       ███    ███    ███ ▀█████████▄ ███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄   ███    ███", 'yellow'))
	print(colored("███       ███▌   ███    █▀     ▀███▀▀██ ███    █▀  ███    ███ ███   ███   ███   ███    ███ ███▌ ███   ███   ███    █▀ ", 'yellow'))
	print(colored("███       ███▌   ███            ███   ▀ ███        ███    ███ ███   ███   ███  ▄███▄▄▄██▀  ███▌ ███   ███  ▄███▄▄▄    ", 'yellow'))
	print(colored("███       ███▌ ▀███████████     ███     ███        ███    ███ ███   ███   ███ ▀▀███▀▀▀██▄  ███▌ ███   ███ ▀▀███▀▀▀    ", 'yellow'))
	print(colored("███       ███           ███     ███     ███    █▄  ███    ███ ███   ███   ███   ███    ██▄ ███  ███   ███   ███    █▄ ", 'yellow'))
	print(colored("███▌    ▄ ███     ▄█    ███     ███     ███    ███ ███    ███ ███   ███   ███   ███    ███ ███  ███   ███   ███    ███", 'yellow'))
	print(colored("█████▄▄██ █▀    ▄████████▀     ▄████▀   ████████▀   ▀██████▀   ▀█   ███   █▀  ▄█████████▀  █▀    ▀█   █▀    ██████████", 'yellow')) 
	print(colored("▀", 'yellow'))
	print(colored("                     Version: 1.0", 'red'))
	print(colored("                          By: s1gh", 'blue'))
	print("\n")

def main():
	main_screen()
	parser = argparse.ArgumentParser(description="ListCombiner - Tool for generating small wordlists for targeted attacks")
	parser.add_argument('-w',dest='wordlist',required=True,help="Main wordlist")
	parser.add_argument('-p',dest='prepend',required=False,help="Wordlist to prepend to main wordlist")
	parser.add_argument('-a',dest='append',required=False,help="Wordlist to append to main wordlist")
	parser.add_argument('-o',dest='outfile',required=True,help="File to write the final wordlist to")


	if len(sys.argv)<3:
		parser.print_help()
		sys.exit(0)

	args = parser.parse_args()
	generate_wordlist(args)


if __name__ == '__main__':
    main()
    sys.exit(0)
