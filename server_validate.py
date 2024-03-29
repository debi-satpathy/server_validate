import pandas as pd
import subprocess
import xtelnet
import httplib2
import time
from selenium import webdriver


def ping_check(ip):
    for i in ip:
        proc=subprocess.Popen(['ping ',i],stdout=subprocess.PIPE)
        stdout,stderr=proc.communicate()
        if proc.returncode ==0:
            print('{} is up'.format(i))
            #print("Ping output:")
            #print(stdout.decode('ASCII'))
        else:
            print('{} is down'.format(i))
def telnet_check(ip):
    #print(ip)
    t=xtelnet.session()
    try:
        t.connect(ip,username='root',password='toor',p=23,timeout=5)
        response=t.execute('echo Connected Successfully')
        print(response)
        t.close()
    except Exception as e:
        print("{}Connection could not be established. Please check manually".format(ip))

def url_check(url): 
    url='http://'+str(url)
    ht=httplib2.Http()
    response=ht.request(url,'HEAD')
    if int(response[0]['status'])  == 200:
        print('Response Code: '+response[0]['status'])
        print("{} URL is up.".format(url))
    else:
        print("Response Code: "+response[0]['status'])
        print("Website is down.")


def find_text(url,search_text):
    url="https://"+url
    print(url)
    driver = webdriver.Chrome(executable_path=r"C:\Users\91700\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\chromedriver_win32\chromedriver",service_log_path=None)
    driver.get(url);
    time.sleep(10)
    button = driver.find_element_by_link_text(search_text)
    if button:
        print("Search found !!")
    else:
        print("Search not found!!")
    driver.close()
def main():
    server =pd.read_excel(r"D:\codes\server_validate\server_input.xlsx")
    #ping_check(server['ping'].dropna())
    #telnet_check(server['telnet'].dropna())
    for i in range(len(server.index)):
        if pd.isnull(server['url'][i]):
            continue
        #url_check(server.loc[i,'url'])
        if pd.isnull(server['find text'][i]):
            continue
        #print(server.loc[i,'find text'])
        find_text(server['url'][i],server.loc[i,'find text'])
        

if __name__=='__main__':
    main()
