def test_double_click(driver):
    driver.get("")

    clickable =driver.find_element(By.ID,"")
    ActionChains(driver)\
    .double_click(clickable)\
    .drag_and_drop(draggaable,dropable)\
    .perform()

    assert driver.find_element(By.)