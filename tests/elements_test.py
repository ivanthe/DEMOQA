import time

from pages.elements_page import TextBoxPage

url = "https://demoqa.com/text-box"
class TestElements:

    class TestTestBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_filds()
            output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
            assert full_name == output_name
            assert email == output_email
            assert current_address == output_cur_address
            assert permanent_address == output_per_address

