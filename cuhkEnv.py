from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument("headless")
class personal:
    def __init__(self, ide, password):
        self.id = ide
        self.password = password

    def __repr__(self):
        return "personal({}, {})".format(self.id, self.password)

    def login(self):
        global driver

        driver = webdriver.Chrome(executable_path="C:/Chromedriver.exe")
        #chrome_options=options
        driver.get("https://cusis.cuhk.edu.hk/psp/csprd/?cmd=login")
        time.sleep(1)
        username = driver.find_element_by_name("userid")
        password = driver.find_element_by_name("pwd")
        username.send_keys(self.id)
        password.send_keys(self.password)
        driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]/table[2]/tbody/tr[5]/td[3]/input").click()
        search = driver.find_element_by_name("SEARCH_TEXT")
        search.send_keys("academic requirements")
        driver.find_element_by_xpath("//*[@id='Nav']/table/tbody/tr[2]/td/form/table/tbody/tr/td[2]/a/img").click()
        driver.find_element_by_xpath("//*[@id='PORTAL_SRCH_OUT_URL$0']").click()
        driver.switch_to_frame("TargetContent")

    
    @staticmethod
    def my_academics():
        driver.find_element_by_xpath("//*[@id='ACE_width']/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td[11]/a").click()
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        name = soup.find("span", {"class" : "PALEVEL0PRIMARY"}).get_text()
        span = soup.find_all("span", {"class":"PSEDITBOX_DISPONLY"})
        college = span[0].get_text()
        major = span[1].get_text()
        print("Name: {}, College: {}, Major: {}".format(name, college, major))
            
    @staticmethod
    def academic_requirements():
        """ views the courses that are required, unfolds and print out their information"""

        driver.find_element_by_xpath("//*[@id='DERIVED_SAA_DPR_SSS_EXPAND_ALL']").click()
        for i in range(25):
            try:
                driver.find_element_by_xpath("//*[@id='SAA_ACRSE_VW$fviewall$" + str(i) + "']").click()
            except NoSuchElementException:
                pass
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find_all("table", {"class": "PSLEVEL4GRIDNBO"})

        count=1
        code_list = []
        code_taken = []

        global code_name
        code_name = {}
        
        print("\n-----courses not taken-----\n")
        for tab in table:
            tr_list = tab.find_all("tr")
            for tr in tr_list:
                td_list = tr.find_all("td")
                if len(td_list) == 6:
                    code = td_list[0].get_text().strip()
                    name = td_list[1].get_text().strip()
                    credit = td_list[2].get_text().strip()
                    when = td_list[3].get_text().strip()
                    grade = td_list[4].get_text().strip()
                    if code in code_list or len(when) > 0 or len(code) != 8:
                        if code in code_taken or name[5:]=="EXEMPT":
                            pass
                        else:
                            code_taken.extend((code, name, credit, when, grade))
                    else:
                        space = 35-len(name)
                        code_list.append(code)
                        print("{}. {} - {} {} {} credits".format(count, code, name, "-"*space, credit))
                        count+=1
                        code_name[code] = name
                else:
                    pass 
            
        print("\n-------courses taken-------\n")
        
        for i in range(int(len(code_taken)/5)):
            space = 35-len(code_taken[5*i+1])
            print("{}. {} - {} {} credit: {} / term: {} / grade: {}".format(i+1, code_taken[5*i], code_taken[5*i+1], "-"*space,  code_taken[5*i+2],code_taken[5*i+3],code_taken[5*i+4]))

        # url = "javascript:submitAction_win0(document.win0,'CRSE_DESCR$0');"
        # driver.find_element_by_xpath('//a[@href="'+url+'"]').click()

    @staticmethod
    def change_frame():
        driver.switch_to_frame("TargetContent")

    @staticmethod
    def get_time(code):
        driver.find_element_by_partial_link_text(code_name[code]).click()
        driver.find_element_by_xpath("//*[@id='DERIVED_SAA_CRS_SSR_PB_GO']").click()
        print(code_name[code])
        view_all_click = 1
        try:
            driver.find_element_by_xpath("//*[@id='CLASS_TBL_VW5$fviewall$0']").click()
        except NoSuchElementException:
            view_all_click = 0

        # table = CLASS_MTGPAT$scroll$0
        # different class sections are classified by their first letter of string

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        section = soup.find_all("table", {"class": "PSLEVEL1GRIDNBO"})[2:]
        first_letter = ""
        k=0
        lecture =True
        # n_possibility = 0
        list_lecture = []
        list_possibility = []  
        """
        list_possibility = [
            [[(course, lec_or_tut, day, start, end), ()], (), (),()], -- possibility 1 // list in list[0] is the compulsary, others are selective
            [[(course, lec_or_tut, day, start, end), ()], (), (),()], -- possibility 2
            [[(course, lec_or_tut, day, start, end), ()], (), (),()]  -- possibility 3
        ]   
        can have list_possibility[][][]
        """
        for sec_tr in section: # all frames
            sec_tr = sec_tr.find_all("tr")[1:] # remove section / seesion / statue bar
            order=1
            for sec_td in sec_tr: # lecture / day / time etc
                sec_td = sec_td.find_all("td")
                if len(sec_td) < 5: 
                    k+=1
                    section_name = sec_td[0].get_text().strip()
                    if section_name[0] == first_letter:
                        pass
                    else:
                        list_lecture = [[],[]]
                        print("\n")
                        k=0

                    if k<1: # lectures 
                        print("-------", section_name,"-------")
                        lecture = True
                    else:   # tutorials
                        print("-----", section_name,"     ")
                        lecture = False

                else:
                    day = sec_td[0].get_text().strip()
                    start = sec_td[1].get_text().strip()
                    end = sec_td[2].get_text().strip()
                    place = sec_td[3].get_text().strip()
                    print("{}. {}, {} ~ {}, {}".format(order, day, start, end, place))
                    order+=1
                    if lecture == True:
                        list_lecture[0].append((section_name, day, start, end))
                    else:
                        list_lecture[1].append((section_name, day, start, end))
                        if list_lecture in list_possibility:
                            pass
                        else:
                            list_possibility.append(list_lecture)
                        
                        
                first_letter = section_name[0]

        print(len(list_possibility[0]), "possibilities")
        for i in range(len(list_possibility)):
            print(list_possibility[i])
        
        # print(list_possibility)
        # view_all_click_and_time = [view_all_click, n_possibility, list_possibility]
        # return view_all_click_and_time
        return view_all_click, list_possibility

    @staticmethod
    def go_back():
        driver.back()

    @staticmethod
    def close():
        driver.close()

    @staticmethod
    def check_error():
        try:
            driver.find_element_by_id("login_error")
            return True
        except NoSuchElementException:  #spelling error making this code not work as expected
            return False

