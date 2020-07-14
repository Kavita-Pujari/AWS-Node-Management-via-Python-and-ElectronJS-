import bottle_websocket
from datetime import datetime
import json
import sys
import eel
import time
import argparse
import os
import platform
import shutil
import shlex
import re
import traceback
import tempfile
from os import path
import sqlite3
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote 
import csv
import re
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import Select
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from urllib.parse import urlparse 
from urllib.request import urlopen
from multiprocessing import Process
from geopy.geocoders import Nominatim


class CaptureStderr:
    """ Capture stderr and forward it onto eel.addOutput """
    filters = []
    ui_started = False # Don't send messages until the UI has started (or is close)

    def __init__(self):
        self.original = sys.stderr # Keep track of original

    def start(self):
        """ Start filtering and redirecting stderr """
        sys.stderr = self

    def stop(self):
        """ Stop filtering and redirecting stderr """
        sys.stderr = self.original

    def add_filter(self, filter_expression):
        self.filters.append(re.compile(filter_expression))

    def write(self, message):
        """ When sys.stderr.write is called, it will re directed here """

        # Filter pre-defined lines that don't need to be sent
        for single_filter in self.filters:
            if not single_filter.match(message) is None:
                return

        if self.ui_started:
            # Send making sure there is a newline at the end
            if message.endswith('\n'):
                eel.addOutput(message)
            else:
                eel.addOutput(message + '\n')
        else:
            self.original.write(message)
            self.original.flush()


# These modules capture stderr so we need to make sure they get our object
cs = CaptureStderr()
cs.add_filter('[0-9]+ ([a-z]|[A-Z])+: [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3} - - \[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\] "GET')
cs.add_filter('\s$')
cs.start()

# Pre-defined variables by Python
DEFAULT_RECURSION_LIMIT = sys.getrecursionlimit()

# Some variables to help with arguments and how they are passed around (can also be used when being imported)
filename = None
disable_chrome = False

# Setup eels root folder
web_location = 'web'
web_path = os.path.dirname(os.path.realpath(__file__)) + '/' + web_location
eel.init(web_path)

# Use the same temporary directory to speed up consecutive builds
temporary_directory = tempfile.mkdtemp()


@eel.expose
def ask_login(log_email, log_password):
    if(log_email =="kavitapujari55@gmail.com" and log_password =="kavi@1234"):
        eel.relocation("node.html")
    else:
        eel.error_alert("Dude Barabar Password Daal")  
 
    log_url = "https://console.aws.amazon.com/console/home"
    driver.get(log_url)
    
    conn = sqlite3.connect('final_db.db')
    cursor = conn.execute("SELECT id, user_no, password from CRED where id = 1 ")
    for row in cursor:
        user_id = row[0]
        num_ber = row[1]
        pass_word = row[2]

    username = driver.find_element_by_id("resolving_input")
    username.send_keys(str(num_ber))
    driver.find_element_by_id("next_button").click()

    time.sleep(30)
    
    password = driver.find_element_by_id("password")
    password.send_keys(str(pass_word))
    driver.find_element_by_id('signin_button').click()

    time.sleep(20)
    name5=driver.find_element_by_link_text("EC2")
    name5.click()
    time.sleep(20)
    driver.find_element_by_id("gwt-debug-leftNav-Instances").click()
    time.sleep(20)    

@eel.expose
def ask_update(log_email, log_password):
    try:
        conn = sqlite3.connect('final_db.db')
        conn.execute(''' DELETE from CRED WHERE id = 1 ''')
        conn.execute(''' INSERT INTO CRED(id,user_no,password) VALUES(?,?,?)''',(1,log_email,log_password))
        conn.commit()
        eel.error_alert("Credentials Are Updated !")
    except:
        eel.error_alert("Unable To Update Credentials !")


@eel.expose
def ask_Remove():
    try:
        conn = sqlite3.connect('final_db.db')
        conn.execute(''' DELETE from CRED WHERE id = 1 ''')
        conn.commit()
        eel.delete_alert("Credentials Are Deleted !")
    except:
        eel.error_alert("Unable To Update Credentials !")

@eel.expose
def get_username():
    try:
        conn = sqlite3.connect('final_db.db')
        cursor = conn.execute("SELECT id, user_no, password from CRED where id = 1 ")
        for row in cursor:
            user_id = row[0]
            num_ber = row[1]
            pass_word = row[2]
            #print(num_ber)
            #print(pass_word
        return num_ber,pass_word
    except:
        num_ber = ""
        pass_word = ""
        return num_ber,pass_word
        
@eel.expose
def insert_history():
    conn = sqlite3.connect('final_db.db')
    cursor = conn.execute("SELECT URL, FILENAME, DATE from HISTORY")
    for row in cursor:
        URL = row[0]
        FILENAME = row[1]
        DATE = row[2]
        return URL,FILENAME,DATE


@eel.expose
def start_all():

    #for selection of all instances
    
    name7=driver.find_element_by_class_name("GB5AGWGDBID")
    name7.click()
    time.sleep(10)

    #for action button drop down
    driver.find_element_by_class_name("GB5AGWGDCRB").click()
    driver.find_element_by_id("gwt-debug-menu-instance-state").click()
    driver.find_element_by_id("gwt-debug-action-start-instances").click()
    driver.find_element_by_id("gwt-debug-dialogBoxSubmitButton-button").click() 
    

@eel.expose
def stop_all():       
    
    #for action button drop down
    driver.find_element_by_class_name("GB5AGWGDCRB").click()
    driver.find_element_by_id("gwt-debug-menu-instance-state").click()
    driver.find_element_by_id("gwt-debug-action-stop-instances").click()
    driver.find_element_by_id("gwt-debug-dialogBoxSubmitButton-button").click() 

'''
@eel.expose
def update_status3(jd_city):    

    html_source = driver.page_source
    html_source = BeautifulSoup(html_source, "html.parser")

    rating = html_source.find_all('div', {'class': 'GLIWNNXDBTG'})
    
    lable = rating[5].find_all('label', {'class': 'GLIWNNXDOWD'})
    
    instancs_name = rating[5].find_all('div', {'class': 'GLIWNNXDBOB'})
    for i in range(0,len(instancs_name)):
        print(str(instancs_name[i].text))
        
    result = []
    for i in range(0,len(lable)):
        print(str(lable[i]))
        text = str(lable[i])
        pool = BeautifulSoup(text, "html.parser")
        for tag in pool.findAll(True,{'id':True}) :
            result.append(tag['id'])

    for i in range(0,len(instancs_name)):
        print(str(instancs_name[i].text)+"-> "+result[i])
        eel.AddRow(str(instancs_name[i].text) , result[i] )
        
    print(result[0])
    time.sleep(5)
    driver.find_element_by_id(str(result[1])).click()

    html_source = driver.page_source
    html_source = BeautifulSoup(html_source, "html.parser")

    rating = html_source.find_all('div', {'class': 'GLIWNNXDBTG'})
    
    lable = rating[5].find_all('label', {'class': 'GLIWNNXDOWD'})
    
    instancs_name = rating[5].find_all('div', {'class': 'GLIWNNXDBOB'})
    for i in range(0,len(instancs_name)):
        print(str(instancs_name[i].text))
        
    result = []
    for i in range(0,len(lable)):
        print(str(lable[i]))
        text = str(lable[i])
        pool = BeautifulSoup(text, "html.parser")
        for tag in pool.findAll(True,{'id':True}) :
            result.append(tag['id'])

    for i in range(0,len(instancs_name)):
        print(str(instancs_name[i].text)+"-> "+result[i])
        eel.AddRow(str(instancs_name[i].text) , result[i] )
                
    driver.find_element_by_id(str(result[int(jd_city)])).click()
    
    #for action button drop down
    driver.find_element_by_class_name("GGVUFA2CGWD").click()
    driver.find_element_by_id("gwt-debug-menu-instance-state").click()
    driver.find_element_by_id("gwt-debug-action-start-instances").click()
    driver.find_element_by_id("gwt-debug-dialogBoxSubmitButton-button").click()
 '''   
def check_arguments():
    """ Check arguments passed """
    global filename
    global disable_chrome

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs='?', help="pass a file into the interface")
    parser.add_argument("-nc", "--no-chrome", action="store_true", help="do not open in chromes app mode")
    args = parser.parse_args()
    if args.filename is not None:
        filename = args.filename
    disable_chrome = args.no_chrome
    
def run():
    """ Open the interface """
    if __name__ == '__main__':
        check_arguments()
    cs.start()
    eel.start('login.html', size=(2000, 2000))
    ''' 
    try:
        if eel.chrome.get_instance_path() is not None and not disable_chrome:
            #eel.init(path.dirname(__file__) + "/web")
            eel.start('login.html', size=(2000, 2000), options={'port': 0})
        else:
            #eel.init(path.dirname(__file__) + "/web")
            eel.start('login.html', size=(2000, 2000), options={'port': 0, 'mode': 'user selection'})
    except (SystemExit, KeyboardInterrupt):
        pass # This is what the bottle server raises
    '''
    shutil.rmtree(temporary_directory)


if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.set_page_load_timeout(20)
    run()
