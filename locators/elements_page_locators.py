from selenium.webdriver.common.by import By
   
class TextBoxPageLocators:
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class WebTablePageLocators:
    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")

    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.XPATH, "//input[@id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")



class ButtonLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    LEFT_CLICK_BUTTON = (By.XPATH, "//div[3]/button[1]")

    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    LEFT_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')