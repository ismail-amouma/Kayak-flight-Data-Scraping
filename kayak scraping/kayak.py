from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from openpyxl import Workbook
mounths=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
url="https://www.kayak.com/flights"

def month_to_int(month):
    switch = {
        'January' :1,         
        'February' :2,         
        'March' :3,           
        'April' :4,              
        'May' :5, 
        'June' :6,
        'July' :7, 
        'August' :8, 
        'September' :9, 
        'October' :10, 
        'November' :11, 
        'December' :12    
    }
    return switch.get(month)  
def set_up_driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    global driver
    driver = webdriver.Chrome(service=service)
    
    
def first_page():
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(url)

def place(place_from,place_to):
    remove=driver.find_element(By.CSS_SELECTOR,'div[aria-label="Remove"]')
    time.sleep(1)
    remove.click()

    origin_input=driver.find_element(By.CSS_SELECTOR,'input[aria-label="Flight origin input"]')
    time.sleep(2)
    origin_input.send_keys(place_from)
    time.sleep(1)
    destin_input=driver.find_element(By.CSS_SELECTOR,'input[aria-label="Flight destination input"]')
    time.sleep(2)
    destin_input.send_keys(place_to)

def set_date(start_date="D-M-Y",end_date="D-M-Y"):
    year_st=start_date.split("-")[2]
    month_st=start_date.split("-")[1]
    day_st=start_date.split("-")[0]
    year_en=end_date.split("-")[2]
    month_en=end_date.split("-")[1]
    day_en=end_date.split("-")[0]

    calendar_button=driver.find_element(By.CSS_SELECTOR,'span[aria-label="Start date calendar input"]')
    time.sleep(1)
    calendar_button.click()
    if int(year_st)>int(year_en):
        print("please switch betwen start and end date")
    try:
        #chose date for start date
        while int(year_st)>int(driver.find_element(By.XPATH,"(//div[@class='wHSr-monthName'])[1]").text.split()[1]):

            next_mounth=driver.find_element(By.CSS_SELECTOR,'button[aria-label="Next Month"]')
            next_mounth.click()

        while int(month_st)>month_to_int(driver.find_element(By.XPATH,"(//div[@class='wHSr-monthName'])[1]").text.split()[0]):
            next_mounth=driver.find_element(By.CSS_SELECTOR,'button[aria-label="Next Month"]')
            next_mounth.click()
            
        date1=mounths[int(month_st)-1]+" "+day_st+", "+year_st
        start=driver.find_element(By.CSS_SELECTOR,f'div[aria-label="{date1}"]')
        start.click()
        
    # end date end chose
        while int(year_en)>int(driver.find_element(By.XPATH,"(//div[@class='wHSr-monthName'])[1]").text.split()[1]):
            next_mounth=driver.find_element(By.CSS_SELECTOR,'button[aria-label="Next Month"]')
            next_mounth.click()

        while int(month_en)>month_to_int(driver.find_element(By.XPATH,"(//div[@class='wHSr-monthName'])[1]").text.split()[0]):
            next_mounth=driver.find_element(By.CSS_SELECTOR,'button[aria-label="Next Month"]')
            next_mounth.click()
            
        date2=mounths[int(month_en)-1]+" "+day_en+", "+year_en
        start2=driver.find_element(By.CSS_SELECTOR,f'div[aria-label="{date2}"]')
        start2.click()
    except:
        print("your date is invalide")
def search():
    search=driver.find_element(By.CSS_SELECTOR,'button[aria-label="Search"]')
    driver.execute_script("arguments[0].click();", search)
    time.sleep(20)
def load_more():

    while True:
        try:
            more = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[class="moreButton"]'))
            )
            driver.execute_script("arguments[0].click();", more)
        except:
            break

def scraping(type,flight1,flight2):
    list=[]
    flights_list=driver.find_elements(By.CSS_SELECTOR,'div[class="resultWrapper"]')
    stops_cites=driver.find_elements(By.XPATH,'//div[@class="section stops"]/div[2]')
    duration=driver.find_elements(By.XPATH,'//div[@class="section duration allow-multi-modal-icons"]/div[1]')
    cites=[stop.text for stop in stops_cites]
    flight1_stop_cites=cites[::2]
    flight2_stop_cites=cites[1::2]
    flights_duration=[dur.text for dur in duration]
    flight1_dur=flights_duration[::2]
    flight2_dur=flights_duration[1::2]
    i,j,m=1,1,0
    for flight in flights_list:
        price=flight.find_element(By.CSS_SELECTOR,'span[class="price-text"]').text 
        flight1_date=flight.find_element(By.XPATH,f'(//span[@class="depart-time base-time"])[{i}]').text+" "+flight.find_element(By.XPATH,f'(//span[@class="time-meridiem meridiem"])[{j}]').text+" - "+flight.find_element(By.XPATH,f'(//span[@class="arrival-time base-time"])[{i}]').text+" "+flight.find_element(By.XPATH,f'(//span[@class="time-meridiem meridiem"])[{j+1}]').text
        flight2_date=flight.find_element(By.XPATH,f'(//span[@class="depart-time base-time"])[{i+1}]').text+" "+flight.find_element(By.XPATH,f'(//span[@class="time-meridiem meridiem"])[{j+2}]').text+" - "+flight.find_element(By.XPATH,f'(//span[@class="arrival-time base-time"])[{i+1}]').text+" "+flight.find_element(By.XPATH,f'(//span[@class="time-meridiem meridiem"])[{j+3}]').text
        flight1_company=flight.find_element(By.XPATH,f'(//div[@dir="ltr"])[{i}]').text
        flight2_company=flight.find_element(By.XPATH,f'(//div[@dir="ltr"])[{i+1}]').text
        flight1_stops=flight.find_element(By.XPATH,f'(//div[@class="section stops"]/div)[{j}]').text
        flight2_stops=flight.find_element(By.XPATH,f'(//div[@class="section stops"]/div)[{j+2}]').text
        liste_to_append=[type,flight1,flight1_date,flight1_company,flight1_stops,flight1_stop_cites[m],flight1_dur[m].replace(" ",":"),flight2,flight2_date,flight2_company,flight2_stops,flight2_stop_cites[m],flight2_dur[m].replace(" ",":"),price]
        #append method won't work
        list+=[liste_to_append]
        m+=1
        i+=2
        j+=4
    return list

def kayak_scraping(flight1,flight2,start_date,end_date):
    x=flight1+" "+flight2
    y=flight2+" "+flight1
    z=start_date+" "+end_date
    load_more()
    list_b=scraping("Best",x,y)
    print("best done")
    botton1=WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '(//a[@data-code = "duration"])'
            )))
    driver.execute_script("arguments[0].click();", botton1)
    load_more()
    list_q=scraping("Quickest",x,y)
    print("quickest done")
    botton2=WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '(//a[@data-code = "price"])'
            )))
    driver.execute_script("arguments[0].click();", botton2)    
    load_more()
    list_c=scraping("Cheapest",x,y)
    print("cheapest done")
    final_list=[list_c,list_b,list_q]
    wb = Workbook()
    page = wb.active
    headers = ['Type','Out Flight','Out Date', 'Out Airline ', 'Out Stops', 'Out Cities',"out Duration",
    "Return Flight","Return Date",'Return Airline ', 'Return Stops', 'Return Cities',"Return Duration","Price"]
    page.append(headers)
    print("making file")
    for list in final_list:
            for row in list:
                if row[4]=="nonstop":
                    row[5]="NULL"
                if row[10]=="nonstop":
                    row[11]="NULL"
                page.append(row)
    wb.save(filename=f'Final_results_{x}_{z}_of_scraping.xlsx')