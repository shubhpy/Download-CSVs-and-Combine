from selenium import webdriver
import time
import os

SUB_CODE = "BCCL"
WAIT_TIME = 15

browser = webdriver.Firefox()
browser.get('')
time.sleep(WAIT_TIME)

# new_url = browser.current_url
# print (new_url)

# login_code = new_url.split("LOGIN_DESKTOP:")[1][:-5]
# print (login_code)

# browser.get(access_url)
# "MPL","DVC",
Cust_Names = ["WBPDCL","NFL","UPRVUNL"]

# Cust_Names = list()
# elements = browser.find_elements_by_tag_name("option")
# for e in elements:
#     if e.text!="Select Consumer":
#         Cust_Names.append(e.text)

while len(Cust_Names):
    print ("Cust_Names Length" , len(Cust_Names))
    elements = browser.find_elements_by_tag_name("option")
    for e in elements:
        CUST_CODE = e.text
        if CUST_CODE!="Select Consumer" and (CUST_CODE in Cust_Names):
            print (CUST_CODE)
            e.click()
            time.sleep(WAIT_TIME)
            
            class_elements = browser.find_element_by_class_name("t-Login-buttons")
            class_elements.click()
            time.sleep(WAIT_TIME)

            id_elements = browser.find_element_by_id("1_menubar_7")
            id_elements.click()
            time.sleep(WAIT_TIME)
            
            class_elements_2 = browser.find_elements_by_class_name("t-Report-cell")
            for ce2 in class_elements_2:
                if ce2.text == SUB_CODE:
                    ce2.click()
                    time.sleep(WAIT_TIME)
                    
                    Areas = list()
                    class_elements_3 = browser.find_elements_by_class_name("t-Report-cell")
                    for ce3 in class_elements_3:
                        if ce3.get_attribute("headers") == "UNIT_NAME":
                            Areas.append(ce3.text)

                    while len(Areas):
                        print (Areas)
                        class_elements_3 = browser.find_elements_by_class_name("t-Report-cell")
                        for ce3 in class_elements_3:
                            AREA_NAME = ce3.text
                            if ce3.get_attribute("headers") == "UNIT_NAME" and (AREA_NAME in Areas):
                                ce3.click()
                                
                                time.sleep(WAIT_TIME)

                                actions_element = browser.find_element_by_id("R98039203420796323_actions_button")
                                print(actions_element.text)
                                actions_element.click()
                                # time.sleep(WAIT_TIME)
                                
                                download_element = browser.find_element_by_id("R98039203420796323_actions_menu_14i")
                                print (download_element.text)
                                download_element.click()
                                time.sleep(WAIT_TIME-5)                        

                                options_element = browser.find_element_by_class_name("a-IRR-iconList-link")
                                print (options_element.text)
                                options_element.click()
                                time.sleep(WAIT_TIME)

                                print (SUB_CODE+"_"+CUST_CODE+"_"+AREA_NAME +".csv")
                                os.rename("/home/shubhanshu/Downloads/new.csv", "/home/shubhanshu/Downloads/"+SUB_CODE+"_"+CUST_CODE+"_"+AREA_NAME +".csv")
                                
                                Areas.remove(AREA_NAME)
                                
                                print (Areas)
                                browser.back()
                                time.sleep(WAIT_TIME)
                                break
                    
                    break
            Cust_Names.remove(CUST_CODE)
            browser.back()
            time.sleep(WAIT_TIME)
            browser.back()
            time.sleep(WAIT_TIME)
            browser.back()
            time.sleep(WAIT_TIME)
            print ("Cust_Names Length" , len(Cust_Names))
            break
