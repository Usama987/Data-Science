import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
# Changing the data types of all strings in the module at once
from __future__ import unicode_literals
# Used to save the file as excel workbook
# Need to install this library
from xlwt import Workbook
# Used to open to corrupt excel file


options = Options()
options.add_argument("user-data-dir=C:\\Users\\mohdu\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe',options=options)

#####################Trends################
driver.get('https://business.facebook.com/latest/insights/overview?asset_id=639662719988468&nav_ref=bm_home_redirect')
time.sleep(2)
export = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/div')
export.click()
time.sleep(1)
exp_csv = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div/div')
exp_csv.click()
time.sleep(2)
filename = r'C:/Users/mohdu/Downloads/Trends.xls'
# Opening the file using 'utf-16' encoding
file1 = io.open(filename, "r", encoding="utf-16")
data = file1.readlines()

# Creating a workbook object
xldoc = Workbook()
# Adding a sheet to the workbook object
sheet = xldoc.add_sheet("Sheet1", cell_overwrite_ok=True)
# Iterating and saving the data to sheet
for i, row in enumerate(data):
    # Two things are done here
    # Removeing the '\n' which comes while reading the file using io.open
    # Getting the values after splitting using '\t'
    for j, val in enumerate(row.replace('\n', '').split('\t')):
        sheet.write(i, j, val)
    
# Saving the file as an excel file
xldoc.save('C:/Users/mohdu/Downloads/Trends.xlsx')
trends = pd.read_excel('C:/Users/mohdu/Downloads/Trends.xlsx')
file1.close()
os.remove("C:/Users/mohdu/Downloads/Trends.xls")
os.remove("C:/Users/mohdu/Downloads/Trends.xlsx")

facebook_page = trends.iloc[2:29]
insta_page = trends.iloc[32:59]
f_time = [i.split(',')[0][1:-1] for i in facebook_page[facebook_page.columns[0]]]
f_reach = [i.split(',')[1][1:-1] for i in facebook_page[facebook_page.columns[0]]]


############################Content#########################
#Content
driver.get('https://business.facebook.com/latest/insights/content?asset_id=639662719988468&nav_ref=bm_home_redirect')
time.sleep(1)
export = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[4]/div')
export.click()
time.sleep(1)
exp_csv = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div/div')
exp_csv.click()
time.sleep(2)
filename = r'C:/Users/mohdu/Downloads/Content.xls'
# Opening the file using 'utf-16' encoding
file1 = io.open(filename, "r", encoding="utf-16")
data = file1.readlines()

# Creating a workbook object
xldoc = Workbook()
# Adding a sheet to the workbook object
sheet = xldoc.add_sheet("Sheet1", cell_overwrite_ok=True)
# Iterating and saving the data to sheet
for i, row in enumerate(data):
    # Two things are done here
    # Removeing the '\n' which comes while reading the file using io.open
    # Getting the values after splitting using '\t'
    for j, val in enumerate(row.replace('\n', '').split('\t')):
        sheet.write(i, j, val)
    
# Saving the file as an excel file
xldoc.save('C:/Users/mohdu/Downloads/Content.xlsx')
Content = pd.read_excel('C:/Users/mohdu/Downloads/ Content.xlsx')
file1.close()
os.remove("C:/Users/mohdu/Downloads/Content.xls")
os.remove("C:/Users/mohdu/Downloads/Content.xlsx")

a = Content.loc[1]

Post=[]
p_time = []
Post_reach = []
Likes_reaction = []
Comments = [] 
Shares = []
Results = []
Cost_per_result = []
Link_clicks = []
for i in range(2,len(abc)):
    Post.append(Content['sep=,'][i].split(',')[0][1:-1])
    p_time.append(Content['sep=,'][i].split(',')[1][1:-1])
    Post_reach.append(Content['sep=,'][i].split(',')[2][1:-1])
    Likes_reaction.append(Content['sep=,'][i].split(',')[3][1:-1])
    Comments.append(Content['sep=,'][i].split(',')[4][1:-1])
    Shares.append(Content['sep=,'][i].split(',')[5][1:-1])
    Results.append(Content['sep=,'][i].split(',')[6][1:-1])
    Cost_per_result.append(Content['sep=,'][i].split(',')[7][1:-1])
    Link_clicks.append(Content['sep=,'][i].split(',')[8][1:-1])

##################################Audience######################
driver.get('https://business.facebook.com/latest/insights/people?asset_id=639662719988468&nav_id=231099476&nav_ref=bm_home_redirect')
time.sleep(1)
export = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/div')
export.click()
time.sleep(1)
exp_csv = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div/div')
exp_csv.click()
time.sleep(2)

filename = r'C:/Users/mohdu/Downloads/Audience.xls'
# Opening the file using 'utf-16' encoding
file1 = io.open(filename, "r", encoding="utf-16")
data = file1.readlines()

# Creating a workbook object
xldoc = Workbook()
# Adding a sheet to the workbook object
sheet = xldoc.add_sheet("Sheet1", cell_overwrite_ok=True)
# Iterating and saving the data to sheet
for i, row in enumerate(data):
    # Two things are done here
    # Removeing the '\n' which comes while reading the file using io.open
    # Getting the values after splitting using '\t'
    for j, val in enumerate(row.replace('\n', '').split('\t')):
        sheet.write(i, j, val)
    
# Saving the file as an excel file
xldoc.save('C:/Users/mohdu/Downloads/Audience.xlsx')
Audience = pd.read_excel('C:/Users/mohdu/Downloads/Audience.xlsx')
file1.close()
os.remove("C:/Users/mohdu/Downloads/Audience.xls")
os.remove("C:/Users/mohdu/Downloads/Audience.xlsx")

Facebook_page_likes = Audience.loc[2]
Insta_Followers = Audience.loc[5]
fb_gender = Audience.loc[6:14]
Age = [i.split(',')[0][1:-1] for i in fb_gender.loc[8:]['sep=,']]
Women = [i.split(',')[1][1:-1] for i in fb_gender.loc[8:]['sep=,']]
Men = [i.split(',')[2][1:-1] for i in fb_gender.loc[8:]['sep=,']]

Cities_Likes = Audience['sep=,'].loc[Audience[Audience['sep=,']=='"Facebook Page likes by top cities"'].index[0]+2:(Audience[Audience['sep=,']=='"Instagram followers by top cities"'].index[0]-1)]
City_Likes = [i.split(',')[-1][1:-1] for i in Cities_Likes]
Cities= [i.split(',')[0][1:] for i in Cities_Likes]