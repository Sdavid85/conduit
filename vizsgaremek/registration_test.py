def test_registration():
    import time

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    driver.get("http://localhost:1667/#/")

    # Accept cookies
    driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]').click()

    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()

    time.sleep(3)


    def registration(un, em, pw):
        user_name = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
        email = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
        password = driver.find_element_by_xpath('//*[@id="app"]//fieldset[3]/input')
        button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

        user_name.send_keys(un)
        email.send_keys(em)
        password.send_keys(pw)
        button.click()


    registration("Milvus", "milvus1@example.com", "Abcd123$")

    time.sleep(3)

    alert_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
    ref_text = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]').text
    print(ref_text)
    # Checking correct alert messages coming...
    alert_button.click()

    # Checking registrated user name:
    user_page = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
    time.sleep(2)
    user_name = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/h4').text
    time.sleep(2)
    print(driver.current_url)
    print(user_name)
    if driver.current_url == f"http://localhost:1667/#/@{user_name}/":
        print("Registrated with correct user name")
