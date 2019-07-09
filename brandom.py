import requests
import logging
import time
import sys

from array import *

#logging setup

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

#create function we can deamonize to create and maintain entropy pool

def EntropyPool():

	#initialize binary array

	barray = array("B")

	#set poolsize to maintain

	poolsize = 4096

	#open random file for writing binary

	#variable to count bytes writen

	bcnt = 0

	with open("brandom", 'wb') as bf:

		try:

			while True:

				#check poolize

				logging.warning("filesize: " + str(bf.tell()))

				if bf.tell() < poolsize:

					logging.warning("creating pool ...")

					r = requests.get('https://www.random.org/cgi-bin/randbyte?nbytes=1000&format=b')

					logging.warning(r.text)

					a = r.text.split()

					for n in a:

						bcnt = bcnt + 1

						if bcnt <= poolsize:

							barray.append(int(n,2))

					logging.warning("counter: " + str(bcnt))

					barray.tofile(bf)

					barray = array("B")

				else:

					bf.seek(0)

					bcnt = 0

					logging.warning("pool at size ...")

				time.sleep(.25)

		except Exception as e:

			logging.warning(e)

			logging.warning("Unexpected error:" + str(sys.exc_info()[0]))

			raise


#fill the pool

EntropyPool()