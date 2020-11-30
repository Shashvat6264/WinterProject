from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import shutil
import os

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
	path = os.path.dirname(os.path.abspath(__file__))
	print(path)
	dirname = str(year)
	dirpath = os.path.join(path, dirname)
	if os.path.isdir(dirpath):
		shutil.rmtree(dirpath)
	os.mkdir(dirpath)

	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get("http://www.liiofindia.org/in/cases/cen/INSC/" + str(year) + "/")
	listitems = driver.find_elements_by_xpath('//li[@class="make-database"]')
	num_of_files = len(listitems)
	driver.close()
	
	# Storing in a file
	for i in range(1, num_of_files):
		f = open(dirpath + "/" + str(i) + ".txt", "w+")
		url = "http://www.liiofindia.org/in/cases/cen/INSC/" + str(year) + "/" + str(i) + ".html"
		getfile(url, f)


for i in range(1950, 2020):
	completefolder(i)

