import time
import xlwt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

############################
# Creating an output file
############################
my_xls = xlwt.Workbook(encoding='ascii') # Creating a workbook
my_sheet1 = my_xls.add_sheet("Baddies") # Adding sheet to store urls per keyword
xls_saved = 'Content_Sizes.xls'

####
line_sheet1 = 0
col_sheet1 = 0
col_sheet2 = 1

##################

driver = webdriver.Chrome("C:\\Users\\nicol\\Desktop\\Scripts\\chromedriver.exe")
driver.maximize_window()
##################

Tags = ["VC01_2000055",	"VC01_200198"]


#################################################################################
#################################################################################

def page_test(tag):

    # Going to pindgom tools
    driver.get('https://tools.pingdom.com/')
    time.sleep(1)

    # Pasting the URL in the Search function
    URL_Test = driver.find_element_by_id("urlinput")
    URL_Test.send_keys("http://tag.fast-thinking.co.uk/tag.html?TagID="+ tag)
    time.sleep(1)

    # Starting the test
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="urlform"]/div[2]/button').click()

    # Fetching main result to evaluate if investigation needed
    time.sleep(3)
    page_size = driver.find_element_by_xpath("//*[@id='content']/div[1]/div[3]/div[4]/div[2]")

    time.sleep(3)
    raw_size = (page_size.text).split()
    size = raw_size[0] # fetch only the numerical size
    int_size = float(size) # transforms text for flow control

    if int_size > 120:
        print tag, " " + str(int_size)
        my_sheet1.write(line_sheet1, col_sheet1,tag)
        my_sheet1.write(line_sheet1, col_sheet2, int_size)

    time.sleep(2)

for tag in Tags:
    page_test(tag)
    line_sheet1 += 1

time.sleep(5) # Let the user actually see something!
driver.close() # Closes current tab

my_xls.save(xls_saved)
