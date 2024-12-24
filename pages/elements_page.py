import allure
import requests
from locators.elements_page_locators import *
import base64
import os
from generator.generator import generate_file, generated_person
from locators.elements_page_locators import *
from pages.base_page import BasePage
from datetime import datetime
import time
from selenium.common import TimeoutException
import random


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step('Fill all fields')
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address.replace("\n", " ")
        permanent_address = person_info.permanent_address.replace("\n", " ")
        with allure.step('filling fields'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('click submit button'):
            self.element_is_visible(self.locators.SUBMIT).click()

        return full_name, email, current_address, permanent_address

    @allure.step('Check filled form')
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]

        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step('Open full list')
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('Click random checkbox')
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step('Get checked checkboxes')
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element('xpath', self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.step('Get output result')
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step('Click on the radio button')
    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}
        button = self.element_is_visible(choices[choice])
        button.click()

    @allure.step('Get output result')
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step('Add new person')
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

            count -= 1

        return [person_info.firstname, person_info.lastname, str(person_info.age),
                person_info.email, str(person_info.salary), person_info.department]

    @allure.step('Get all people')
    def get_all_people(self):
        all_people = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []

        for person in all_people:
            data.append(person.text.splitlines())

        return data

    @allure.step('Search person')
    def search_person(self, keyword):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(keyword)

    @allure.step('Get searched person')
    def get_searched_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('Update person data')
    def update_person(self):
        person_info = next(generated_person())

        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(person_info.age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

        return str(person_info.age)

    @allure.step('Delete person')
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('Check person deletion')
    def check_person_deletion(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step('Check new tab forwarding link')
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


class FileUploadDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    @allure.step('Upload file')
    def upload_file(self):
        with allure.step('File generating'):
            filename, path = generate_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        return filename.split('/')[-1], text.split('\\')[-1]

    @allure.step('Download file')
    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        # define filename and filepath
        file_name = f"downloaded_image_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpeg"
        file_path = os.path.join(os.getcwd(), file_name)

        base64_data = link.split(",")[1]
        decoded_data = base64.b64decode(base64_data)

        with open(file_path, "wb") as file:
            file.write(decoded_data)
            check_file = os.path.exists(file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
        return check_file


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    @allure.step('Check button enabling')
    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step('Check button color changing')
    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    @allure.step('Check button appearing')
    def check_appear_of_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutException:
            return False
        return True


class ButtonsPage(BasePage):
    locators = ButtonLocators()

    @allure.step('Check button double click')
    def double_click(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))

    @allure.step('Check button right click')
    def right_click(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))

    @allure.step('Check button left click')
    def left_click(self):
        self.element_is_visible(self.locators.LEFT_CLICK_BUTTON).click()

    @allure.step('Get clicked button text')
    def get_clicked_button_text(self, element):
        return self.element_is_present(element).text
