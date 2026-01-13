from FillForm import fillForm
from FillForm import setup
from FillForm import teardown
from FillForm import cookiesClick

def main():
    driver = setup()
    try:
        cookiesClick(driver)
        fillForm(driver, "breakfast")
        fillForm(driver, "lunch")
        fillForm(driver, "dinner")
    finally:
        teardown(driver)
main()