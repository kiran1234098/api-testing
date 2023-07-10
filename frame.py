        iframe = driver.find_element(By.CSS_SELECTOR,"#modal > iframe")
        driver.switch_to.frame(iframe)
        driver.find_element(By.Tag_NAME,'button').click()

        driver.switch_to.frame('bottonframe')
        driver.find_element(By.TAG_NAME,'button').click()
        driver.switch_to.default_content()
