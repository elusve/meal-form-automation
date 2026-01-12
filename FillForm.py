from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# constants feel free to change/personalize
INFO_ACTIONS = [
    {"type": "input", "by": By.ID, "locator": "input_3_1_3", "value": "John"}, # first name
    {"type": "input", "by": By.ID, "locator": "input_3_1_6", "value": "Doe"}, # last name
    {"type": "input", "by": By.ID, "locator": "input_3_2", "value": "123456789"}, # student number
    {"type": "input", "by": By.ID, "locator": "input_3_3", "value": "123-456-7890"}, # phone number
    {"type": "input", "by": By.ID, "locator": "input_3_4", "value": "johndoe@gmail.com"}, # email
    {"type": "input", "by": By.ID, "locator": "input_3_5", "value": "01/01/26"} # date
]
MEAL_ACTIONS = {
    "breakfast": [
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_46_0"}, # meal plan
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_6_0"}, # meal type
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_43_0"}, # entree
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_45_1"}, # side 1
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_48_4"}, # side 2
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_37_0"}, # dessert
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_33_1"}, # fruit
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_34_1"} # beverage
    ],
    "lunch": [
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_46_0"}, # meal plan
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_6_1"}, # meal type
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_49_0"}, # entree
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_29_2"}, # side 1
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_30_1"}, # side 2
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_31_1"}, # dessert
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_36_0"}, # fruit
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_32_0"} # beverage
    ],
    "dinner": [
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_46_0"}, # meal plan
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_6_2"}, # meal type
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_49_0"}, # entree
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_29_2"}, # side 1
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_30_1"}, # side 2
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_31_1"}, # dessert
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_36_0"}, # fruit
    {"type": "click", "by": By.CSS_SELECTOR, "locator": "#choice_3_32_0"} # beverage
    ]
}

# removed time.sleep and used selenium's expected conditions method and explicit waits method .
def waitAction(driver, action):
    wait = WebDriverWait(driver, timeout=5)

    if action["type"] == "input": # waits until textbox is visible, clears existing text, types value into field
        element = wait.until(EC.visibility_of_element_located((action["by"], action["locator"])))
        element.clear()
        element.send_keys(action["value"])
    elif action["type"] == "click": # waits until button is visible and clickable, clicks button
        element = wait.until(EC.element_to_be_clickable((action["by"], action["locator"])))
        element.click()
    else: # action["type"] not in ["input", "click"] also tested for in Tester.py
        raise ValueError("Unknown action type: " + action["type"])
    

# fills in form for you
def fillForm(mealType: str) -> None:
    mealType = mealType.lower().strip()
    if mealType not in MEAL_ACTIONS: # input not in ["breakfast", "lunch", "dinner"]
        raise ValueError("Unknown meal type: " + mealType)

    driver = webdriver.Chrome()
    driver.get("https://dining.carleton.ca/boxed-meals/")

    for action in INFO_ACTIONS:
        waitAction(driver, action)

    for action in MEAL_ACTIONS[mealType]:
        waitAction(driver, action)

    input("quit")
    driver.quit()







    

