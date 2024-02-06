import requests
from generator.generator import generated_person
from locators.elements_page_locators import LinksPageLocators, TextBoxPageLocators, WebTablePageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address.replace("\n", " ")
        permanent_address = person_info.permanent_address.replace("\n", " ")
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
       
        return full_name, email, current_address, permanent_address


    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]

        return full_name, email, current_address, permanent_address


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self, count=1):
        while count != 0:
            person_info = next(generated_person())
            
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person_info.firstname)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person_info.lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person_info.email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(person_info.age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(person_info.salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(person_info.department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

            count-=1

        return [person_info.firstname, person_info.lastname, str(person_info.age), 
                person_info.email, str(person_info.salary), person_info.department]
    
    def get_all_people(self):
        all_people = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        
        for person in all_people:
            data.append(person.text.splitlines())

        return data
    
    def search_person(self, keyword):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(keyword)

    def get_searched_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()
    
    def update_person(self):
        person_info = next(generated_person())

        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(person_info.age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        
        return str(person_info.age)
        
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_person_deletion(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text
    

class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')

        response = requests.get(link_href)

        if response.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, response.status_code
