def test_modify_data():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    import time

    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    new_username = "Milvus1"

    try:
        driver.get("http://localhost:1667/#/")
        # Cookie accept:
        button_accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]').click()

        # Activate Sign in input field:
        login = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
        time.sleep(3)
        login.click()


        def sign_in(em, pw):
            email = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
            password = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
            button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

            email.send_keys(em)
            password.send_keys(pw)
            button.click()


        sign_in("milvus@example.com", "Abcd123$")

        time.sleep(3)

        user_page = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
        time.sleep(2)
        edit_profile=driver.find_element_by_xpath('//*[@id="app"]/div/div[1]//a').click()
        time.sleep(3)

        def profile_edition(username, email, password):
            profile_username=driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
            profile_email = driver.find_element_by_xpath('//*[@id="app"]//fieldset[4]/input')
            profile_password = driver.find_element_by_xpath('//*[@id="app"]//fieldset[5]/input')
            update_button=driver.find_element_by_xpath('//*[@id="app"]//fieldset/button')


            profile_username.clear()
            profile_username.send_keys(username)
            profile_email.clear()
            profile_email.send_keys(email)
            profile_password.clear()
            profile_password.send_keys(password)
            update_button.click()


        profile_edition("Milvus1", "milvus01@example.com", "Abcd1234$")

        time.sleep(3)
        confirm_button = driver.find_element_by_xpath('/html/body/div[2]//button')
        ref_text = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]').text
        print(ref_text)
        # Checking correct alert messages coming...
        confirm_button.click()

        un = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
        assert (un.text == new_username)
        print(un.text)

    finally:
        pass
        # driver.close()