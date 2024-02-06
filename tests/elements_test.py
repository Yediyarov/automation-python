import random
from locators.elements_page_locators import ButtonLocators
from pages.elements_page import ButtonsPage, TextBoxPage, WebTablePage
import time

class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()

            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current address does not match"
            assert permanent_address == output_per_addr, "the permanent address does not match"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()

            new_person = web_table_page.add_new_person()
            all_people = web_table_page.get_all_people()

            assert new_person in all_people
            
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()

            keyword = web_table_page.add_new_person()[random.randint(0,5)]
            web_table_page.search_person(keyword)
            searched_person = web_table_page.get_searched_person()
            
            assert keyword in searched_person, "the person was not found in the table"

        def test_update_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()

            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_person(last_name)
            age = web_table_page.update_person()
            row = web_table_page.get_searched_person()
            time.sleep(5)
            assert age in row, "the person card has not been changed"

        def test_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()

            email = web_table_page.add_new_person()[3]
            web_table_page.search_person(email)

            web_table_page.delete_person()

            text = web_table_page.check_person_deletion()

            assert text == 'No rows found'

    class TestButtons:
        locators = ButtonLocators()
            
        def test_button_double_click(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()

            button_page.double_click()

            double_click_message = button_page.get_clicked_button_text(self.locators.DOUBLE_CLICK_MESSAGE)

            assert double_click_message == "You have done a double click",  "The double click button was not pressed"

        def test_button_right_click(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()

            button_page.right_click()

            right_click_message = button_page.get_clicked_button_text(self.locators.RIGHT_CLICK_MESSAGE)

            assert right_click_message == "You have done a right click",  "The right click button was not pressed"

        def test_button_left_click(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()

            button_page.left_click()

            left_click_message = button_page.get_clicked_button_text(self.locators.LEFT_CLICK_MESSAGE)

            assert left_click_message == "You have done a dynamic click",  "The left click button was not pressed"