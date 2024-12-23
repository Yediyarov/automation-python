import random
from pages.elements_page import *
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

    class TestCheckBox:
        
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'checkboxes have not been selected'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == "No", "'No' have not been selected"
            
            
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

            keyword = web_table_page.add_new_person()[random.randint(0, 5)]
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
   
    class TestLinks:

        def test_check_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()

            href_link, current_url = links_page.check_new_tab_simple_link()

            assert href_link == current_url, "the link is broken or url is incorrect"

    class TestFileUploadDownload:

        def test_upload_file(self, driver):
            file_upload_page = FileUploadDownloadPage(driver, "https://demoqa.com/upload-download")
            file_upload_page.open()
            filename, result = file_upload_page.upload_file()
            assert filename == result, "The file has not been uploaded"

        def test_download_file(self, driver):
            file_download_page = FileUploadDownloadPage(driver, "https://demoqa.com/upload-download")
            file_download_page.open()
            check = file_download_page.download_file()
            assert check is True, "The file has not been downloaded"
            
    class TestDynamicPropertiesPage:
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, 'Button did not enable after 5 second'

        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            assert color_after != color_before, 'colors have not been changed'

        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_of_button()
            assert appear is True, 'button did not appear after 5 second'
    
    
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
            