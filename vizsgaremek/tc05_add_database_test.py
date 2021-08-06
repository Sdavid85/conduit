def test_add_database():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    import csv
    import time
    from selenium.common.exceptions import NoSuchElementException

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

        time.sleep(2)

        new_article = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
        new_article.click()
        time.sleep(2)

        article_title = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
        article_about = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
        article_content = driver.find_element_by_xpath('//*[@id="app"]//fieldset[3]/textarea')
        article_tag = driver.find_element_by_xpath('//*[@id="app"]//fieldset[4]//input')
        publish_btn = driver.find_element_by_xpath('//*[@id="app"]//form/button')

        with open('./database.csv', 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                article_title.send_keys(row[0])
                article_about.send_keys(row[1])
                article_content.send_keys(row[2])
                article_tag.send_keys(row[3])
                publish_btn.click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
                time.sleep(2)

        my_articles = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
        my_articles.click()
        time.sleep(2)

        article_title_list = []

        page_count = 1

        while True:
            time.sleep(2)
            article_titles = driver.find_elements_by_xpath('//*[@id="app"]//div[2]//a/h1')

            for title in article_titles:
                article_title_list.append(title.text)

            try:
                page_count += 1
                driver.find_element_by_link_text(str(page_count)).click()
            except NoSuchElementException:
                # Stop loop if no more page available
                break

        # Assertion
        csv_my_titles = []
        with open('./database.csv', 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                csv_my_titles.append(row[0])

        assert len(article_title_list) == len(csv_my_titles)

    finally:
        driver.close()
