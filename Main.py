from FillForm import fillForm
from FillForm import setup
from FillForm import teardown
from FillForm import cookiesClick
from GetDate import calendar26 as calendar

def main():
    driver = setup()
    try:
        cookiesClick(driver)
        for date in calendar:
            fillForm(driver, date, "breakfast")
            fillForm(driver, date, "lunch")
            fillForm(driver, date, "dinner")
            if input("quit").lower().strip() == "quit":
                break
    finally:
        teardown(driver)
main()