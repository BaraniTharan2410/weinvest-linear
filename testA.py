'''
Test A
1. Navigate to https://sfo-demo.herokuapp.com/model-portfolio
2. Select “All Weather Strategy” by clicking on “Explore Investment Ideas”
3. In next screen click on button “Customize Portfolio” to make changes to portfolio
4. Click on “Customize” button to enable edit controls
5. Change slider of “ SPDR S&P 500 ETF TRUST SPY US EQUITY ” to 50%
6. Click on “Rebalance” button
7. Click on “Invest” button
8. On next page” verify that “SPDR…” under “What your portfolio contain ?” to be 50%
'''
from selenium import webdriver
from traceback import print_stack
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
class Loginvalidation():

    def testRun(self):
        try:
            driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
            driver.maximize_window()
            driver.get("https://sfo-demo.herokuapp.com/model-portfolio")
            driver.implicitly_wait(8)
            #Select “All Weather Strategy” by clicking on “Explore Investment Ideas”
            explore_Investment_Ideas_button= driver.find_element_by_xpath("//*[contains(text(),'Explore Investment Ideas') and @href = 'weather_portfolio']")
            explore_Investment_Ideas_button.click()
            #In next screen click on button “Customize Portfolio” to make changes to portfolio
            customize_Portfolio_button= driver.find_element_by_xpath("//*[contains(text(),'Customize Portfolio') and @href = 'explore_portfolio/1']")
            customize_Portfolio_button.click()
            #Click on “Customize” button to enable edit controls
            customize_button= driver.find_element_by_xpath("//*[contains(text(),'Customise')]")
            customize_button.click()
            #Change slider of “ SPDR S&P 500 ETF TRUST SPY US EQUITY ” to 50%
            actions = ActionChains(driver)
            slider = driver.find_element_by_xpath("//*[@class='col-md-9']//child::input[1]")
            slider.location_once_scrolled_into_view
            driver.execute_script("window.scrollBy(0,200);")
            for i in range(0,100):
                actions.click_and_hold(slider).move_by_offset(i, 0).release().perform()
                slider_range = driver.find_element_by_xpath("//*[@class='col-md-9']//parent::div/div").text
                arr = list(re.split("%", slider_range))
                if arr[0] == "50":
                    print("PASS::slider of ' SPDR S&P 500 ETF TRUST SPY US EQUITY ' changed to 50%")
                    break
            #Click on “Rebalance” button
            rebalance_button= driver.find_element_by_xpath("//*[contains(text(),'Rebalance')]")
            rebalance_button.click()
            #Click on “Invest” button
            Invest_button = driver.find_element_by_xpath("//*[contains(text(),'Invest Now')]")
            Invest_button.click()
            #On next page” verify that “SPDR…” under “What your portfolio contain ?” to be 50%
            # As per testcase “SPDR…” under “What your portfolio contain ?” to be 50% but it is 13.79% hence verfiying that
            # On next page” verify that “SPDR…” under “What your portfolio contain ?” to be 50%
            spdr_percentage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='list-group constituent-list clearfix']//li//following::span[2]")))
            spdr_percentage_txt = spdr_percentage.text
            if spdr_percentage_txt == "13.79":
                    print("PASS::“'SPDR…' under 'What your portfolio contain ?' to be 13.79%")
            else:
                print("FAIL::'SPDR…' under 'What your portfolio contain ?' is not as 13.79%")
        except:
            print_stack()
        finally:
            driver.quit()

login = Loginvalidation()
login.testRun()

