def test_signinout():
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
        cookie_panel = driver.find_element_by_id('cookie-policy-panel')
        # Accept cookies
        accept_btn = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]')
        accept_btn.click()

        # Login
        login = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
        login.click()

        time.sleep(3)

        username = "Milvus"

        def sign_in(em, pw):
            email = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
            password = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
            button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

            email.send_keys(em)
            password.send_keys(pw)
            button.click()

        sign_in("milvus@example.com", "Abcd123$")

        time.sleep(3)

        # Sign in check
        un = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
        assert (un.text == username)

        # Log out
        driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a').click()
        time.sleep(3)

        # Log out check
        assert (login.text == "Sign in")

        # Cookie management check
        driver.get("http://localhost:1667/#/")
        time.sleep(3)

        # Első próbálkozás
        # assert not cookie_panel.is_displayed()

        # Második próbálkozás
        # if cookie_panel.is_displayed():
        #    print("Element found!")
        # else:
        #    print("Element not found!")
    finally:
        pass
    # driver.close()
