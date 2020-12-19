'''
Test C
1. Navigate to https://sfo-demo.herokuapp.com/model-portfolio
2. Check whether tabs with below texts are available (Where X, Y are are numbers)
    a. “X Portfolio recommendations based on your preferences”
    b. “Y other portfolio choices available”
3. Resize browser window to 375 x 667
4. Check whether tabs with below texts are available now (Where X, Y are are numbers)
    a. “Recommended (X)”
    b. “Others (Y)”
    c. Check X, Y are same as in step 2
'''
from selenium import webdriver
from traceback import print_stack
import re

class Loginvalidation():

    def testRun(self):
        try:
            driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
            driver.maximize_window()
            # Check whether tabs with texts are available in normal resolution
            driver.get("https://sfo-demo.herokuapp.com/model-portfolio")
            driver.implicitly_wait(8)
            #check tabs with text “X Portfolio recommendations based on your preferences”
            recommendations = driver.find_element_by_xpath("//*[@href='#selected-model-portfolios']").text
            recommendations_num = re.findall(r'(\d+) Portfolio recommendations based on your preferences', recommendations)
            if re.match(r'[0-9]+ Portfolio recommendations based on your preferences', recommendations):
                print("PASS::tabs with text 'X Portfolio recommendations based on your preferences'")
            #check tabs with text “Y other portfolio choices available”
            other_portfolio = driver.find_element_by_xpath("//*[@href='#remaining-model-portfolios']").text
            other_portfolionum = re.findall(r'(\d+) other portfolio choices available', other_portfolio)
            if re.match(r'[0-9]+ other portfolio choices available', other_portfolio):
                print("PASS::tabs with text 'Y other portfolio choices available'")
            #Resize browser window to 375 x 667
            driver.set_window_size(375,667)
            # check tabs with text “Recommended (X)”
            Recommended_min = driver.find_element_by_xpath("//*[contains(text(),'Recommended')]").text
            Recommended_minnum = re.findall(r'Recommended \((\d+)\)', Recommended_min)
            if re.match(r'Recommended \(+[0-9]+\)', Recommended_min):
                print("PASS::tabs with text 'Recommended (X)'")
            # check tabs with text “Others (Y)“
            others_min = driver.find_element_by_xpath("//*[contains(text(),'Others')]").text
            others_minnum = re.findall(r'Others \((\d+)\)', others_min)
            if re.match(r'Others \(+[0-9]+\)', others_min):
                print("PASS::tabs with text 'Others (Y)'")
            #Check X, Y are same as in normal resolution and standard resolution
            if recommendations_num == Recommended_minnum and other_portfolionum == others_minnum:
                print("x and y numbers are same")
            else:
                print("x and y numbers are not same")
        except:
            print_stack()
        finally:
            driver.quit()

login = Loginvalidation()
login.testRun()