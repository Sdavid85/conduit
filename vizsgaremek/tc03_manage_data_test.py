def test_add_data():
    import time

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    new_article_title = "Új bejegyzés"

    try:
        driver.get("http://localhost:1667/")
        # Cookie accept:
        button_accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]').click()

        driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
        time.sleep(3)

        # Fill input fields:
        def fill_login(mail, pw):
            email = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
            password = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
            button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

            email.send_keys(mail)
            password.send_keys(pw)
            button.click()

        fill_login("milvus@example.com", "Abcd123$")

        time.sleep(2)

        new_articel = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
        time.sleep(2)

        def articel(title, about, content, tag):
            articel_title = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
            artical_about = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
            artical_content = driver.find_element_by_xpath('//*[@id="app"]//fieldset[3]/textarea')
            artical_tag = driver.find_element_by_xpath('//*[@id="app"]//fieldset[4]//input')
            publish_button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

            articel_title.send_keys(title)
            artical_about.send_keys(about)
            artical_content.send_keys(content)
            artical_tag.send_keys(tag)

            publish_button.click()

        articel("Új bejegyzés", "Próba", "Megnézem működik-e", "test")

        driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/h1').click()
        time.sleep(2)

        article_title = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/h1')
        assert (article_title.text == "Új bejegyzés")

        # Modify data
        # Edit article

        driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/span/a/span').click()
        time.sleep(2)
        modified_article_title = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
        modified_article_title.clear()
        articel("Módosított bejegyzés", "", "", "")

        driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
        time.sleep(2)
        title_list = []
        my_articles = driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
        for title in my_articles:
            title_list.append(title.text)
        assert (title_list[-1] == "Módosított bejegyzés")

        # Delete article

        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/span/button/span').click()


    finally:
        pass
        # driver.close()
