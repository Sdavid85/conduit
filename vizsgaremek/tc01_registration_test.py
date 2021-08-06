def test_registration():
    import time

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    try:
        driver.get("http://localhost:1667/#/")

        # Accept cookies
        accept_btn = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]')
        accept_btn.click()

        # Registration
        sign_up_btn = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a')
        sign_up_btn.click()

        time.sleep(2)

        def registration(un, em, pw):
            user_name = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
            email = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
            password = driver.find_element_by_xpath('//*[@id="app"]//fieldset[3]/input')
            button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

            user_name.send_keys(un)
            email.send_keys(em)
            password.send_keys(pw)
            button.click()

        registration("Milvus", "milvus@example.com", "Abcd123$")
        time.sleep(3)

        # Check feedback message
        feedback = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]')
        assert feedback.text == "Your registration was successful!"

        driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button').click()

    finally:
        pass
    # driver.close()
