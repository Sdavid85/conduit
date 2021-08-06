def test_save_data():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.common.exceptions import NoSuchElementException
    import time

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    try:
        driver.get("http://localhost:1667/")

        # Accept cookies
        accept_btn = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
        accept_btn.click()

        # Login
        login = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
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

        article_title_list = []
        page_count = 1

        # List the title of the articles
        while True:
            time.sleep(3)
            article_titles = driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
            for title in article_titles:
                article_title_list.append(title.text)
            try:
                page_count += 1
                driver.find_element_by_link_text(str(page_count)).click()
            except NoSuchElementException:
                break

        # Writing to csv file:
        with open('titles.csv', 'w', encoding='utf-8') as file:
            file.write(f'{article_title_list}')

        # Assertion
        with open('titles.csv', 'r') as csvfile:
            result = csvfile.read()
        csv_title_list = result[1:len(result) - 1].replace("'", "").split(",")

        assert len(article_title_list) == len(csv_title_list)

    finally:
        pass
    # driver.close()
