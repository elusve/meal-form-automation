from FillForm import fillForm
from FillForm import setup
from FillForm import teardown
from FillForm import cookiesClick
from FillForm import updateDate
from GetDate import calendar26 as calendar

def main():
    driver = setup()
    try:
        cookiesClick(driver)
        for date in calendar:
            updateDate(date)
            fillForm(driver, "breakfast")
            fillForm(driver, "lunch")
            fillForm(driver, "dinner")
            if input("quit").lower().strip() == "quit":
                break
    finally:
        teardown(driver)
main()