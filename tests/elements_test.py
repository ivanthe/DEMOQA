import time

from pages.elements_page import TextBoxPage, CheckBoxPage

url = "https://demoqa.com/text-box"
class TestElements:

    class TestTestBox:
        url = "https://demoqa.com/text-box"

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, self.url)
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_filds()
            output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
            assert full_name == output_name
            assert email == output_email
            assert current_address == output_cur_address
            assert permanent_address == output_per_address

    class TestCheckBox:
        url = 'https://demoqa.com/checkbox'

        def test_checkbox(self, driver):
            checkbox_page = CheckBoxPage(driver, self.url)
            checkbox_page.open()
            checkbox_page.open_full_list()
            checkbox_page.click_random_checkbox()
            clicked_items = checkbox_page.get_list_with_clicked_item()
            result_item = checkbox_page.get_list_with_results()
            checkbox_page.compare_results(clicked_items, result_item)
            time.sleep(1)

