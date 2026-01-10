from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# constants
FIRST_NAME = "John"
LAST_NAME = "Doe"
STU_NUM = "123456789"
PHONE_NUM = "123-456-7890"
EMAIL = "johndoe@gmail.com"

# fills in form for you
def fillForm(date: str, mealType: int) -> None:

    driver = webdriver.Chrome()
    driver.get("https://dining.carleton.ca/boxed-meals/")
    sleep(5)

    # locators
    firstNameBox = driver.find_element(By.ID, "input_3_1_3")
    lastNameBox = driver.find_element(By.ID, "input_3_1_6")
    stuNumBox = driver.find_element(By.ID, "input_3_2")
    mealPlanButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_46_0")
    phoneNumBox = driver.find_element(By.ID, "input_3_3")
    emailBox = driver.find_element(By.ID, "input_3_4")
    dateBox = driver.find_element(By.ID, "input_3_5")

    mealTypeButton = 0
    entreeTypeButton = 0
    side1TypeButton = 0
    side2TypeButton = 0
    dessertTypeButton = 0
    fruitTypeButton = 0
    beverageTypeButton = 0

    match mealType:
        case 0:
            mealTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_6_0")
            entreeTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_43_0")
            side1TypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_45_1")
            side2TypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_48_4")
            dessertTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_37_0")
            fruitTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_33_1")
            beverageTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_34_1")
        case 1:
            mealTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_6_1")
            entreeTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_49_0")
            side1TypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_29_2")
            side2TypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_30_1")
            dessertTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_31_1")
            fruitTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_36_0")
            beverageTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_32_0")
        case 2:
            mealTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_6_2")
            entreeTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_49_0")
            side1TypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_29_2")
            side2TypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_30_1")
            dessertTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_31_1")
            fruitTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_36_0")
            beverageTypeButton = driver.find_element(By.CSS_SELECTOR, "#choice_3_32_0")
        case _:
            driver.quit()
    
    #
    firstNameBox.send_keys(FIRST_NAME)
    lastNameBox.send_keys(LAST_NAME)
    stuNumBox.send_keys(STU_NUM)
    mealPlanButton.click()
    phoneNumBox.send_keys(PHONE_NUM)
    emailBox.send_keys(EMAIL)
    dateBox.send_keys(date)
    mealTypeButton.click()
    entreeTypeButton.click()
    side1TypeButton.click()
    side2TypeButton.click()
    dessertTypeButton.click()
    fruitTypeButton.click()
    beverageTypeButton.click()

    sleep(20)
    driver.quit()







    

