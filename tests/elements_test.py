import random
from pages.elements_page import TextBoxPage, WebTablePage
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