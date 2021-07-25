def test_paging():
    import time

    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    try:
        driver.get("http://localhost:1667/#/")
        # Cookie accept:
        driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]').click()

        # Activate Sign in input field:
        driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()

        time.sleep(3)

        def sign_in(em, pw):
            email = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
            password = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
            button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

            email.send_keys(em)
            password.send_keys(pw)
            button.click()

        sign_in("milvus@example.com", "Abcd123$")

        time.sleep(3)
        feed_title_list = []
        page_count = 1

        while True:
            time.sleep(2)
            feed_titles = driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
            for feed in feed_titles:
                feed_title_list.append(feed.text)
            try:
                page_count += 1
                driver.find_element_by_link_text(str(page_count)).click()
            # driver.find_element_by_xpath('//*[@id="app"]//nav/ul/li[%]/a')
            except NoSuchElementException:
                # Stop loop if no more page available
                break
        print("The title-list of Global feeds: ", feed_title_list)
        print("Number of Global feeds: ", len(feed_title_list))

    finally:
        pass
        # driver.close()
