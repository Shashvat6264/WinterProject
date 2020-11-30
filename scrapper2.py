from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import shutil
import os
import threading

def getfile(url, f):
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)

	driver.get(url)

	headings = driver.find_elements_by_xpath('//h2[@class="make-database"]')
	paras = driver.find_elements_by_tag_name('p')

	f.write(headings[0].text + '\n')
	for i in paras:
		f.write(i.text + '\n')

	# Close browser once teask is completed
	driver.close()

def completefolder(year):
	# Creating directory
	path = os.path.abspath(os.getcwd())
	print(path)
	dirname = str(year)
	path = os.path.join(path, "Data")
	dirpath = os.path.join(path, dirname)
	if os.path.isdir(dirpath):
		shutil.rmtree(dirpath)
	os.mkdir(dirpath)

	# Get number of urls
	# try:
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get("http://www.liiofindia.org/in/cases/cen/INSC/" + str(year) + "/")
	listitems = driver.find_elements_by_xpath('//li[@class="make-database"]')
	num_of_files = len(listitems)
	driver.close()
		
		# Storing in a file
	for i in range(1, num_of_files+1):
		# for i in range(1, 3):
			f = open(dirpath + "/" + str(i) + ".txt", "w+")
			url = "http://www.liiofindia.org/in/cases/cen/INSC/" + str(year) + "/" + str(i) + ".html"
		# thread = getthread(i, year, dirpath)
		# thread.start()
			getfile(url, f)
	# except:
		# print("Error in "+str(year)+"\n")


class getthread(threading.Thread):
	def __init__(self, threadID, year, dirpath):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.year = year
		self.dirpath = dirpath

	def run(self):
		for i in range(0, 10):
			print("Start thread " + str(self.year) + ": file number " + str(self.threadID))
			f = open(self.dirpath + "/" + str(self.threadID) + ".txt", "w+")
			url = "http://www.liiofindia.org/in/cases/cen/INSC/" + str(self.year) + "/" + str(self.threadID + i) + ".html"
			try:
				getfile(url, f)
				print("Year " + str(self.year) + ": file number" + str(self.threadID) + " Downloaded \n")
			except:
				print("Error in " + str(self.year) + ": file number " + str(self.threadID) + "\n")

class yearthread(threading.Thread):
	def __init__(self, threadID, year):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.year = year

	def run(self):
		print("Start thread " + str(self.threadID) + "\n")
		# for i in range(0, 2):
		completefolder(self.year)

for i in range(1950, 1960):
	thread = yearthread(i-1949, i)
	thread.start()
	# completefolder(i)