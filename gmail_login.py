from selenium import webdriver
browser,password,userName= webdriver.Chrome("chromedriver_linux64/chromedriver"),'email','password'
browser.maximize_window()
browser.get("https://www.facebook.com/")
a=browser.find_element_by_xpath('//*[@id="email"]')
a.send_keys(userName)
a=browser.find_element_by_xpath('//*[@id="pass"]')
a.send_keys(password)
browser.find_element_by_xpath('//*[@id="u_0_b"]').click()
