import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTabelPage

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

    class TestRafioButtom:
        url = 'https://demoqa.com/radio-button'

        def test_click_radiobutton(self, driver):
            radiobutton_page = RadioButtonPage(driver, self.url)
            radiobutton_page.open()
            radiobutton_page.click_radio_buttons('yes')
            assert radiobutton_page.get_results() == "Yes", "РЕЗУЛЬТАТ С КНОПОКЙ YES НЕКОРРЕКТНЫЙ!!!!"
            radiobutton_page.click_radio_buttons('impessive')
            assert radiobutton_page.get_results() == "Impressive", "РЕЗУЛЬТАТ С КНОПОКЙ IMPRESSIVE НЕКОРРЕКТНЫЙ!!!!"
            radiobutton_page.click_radio_buttons('no')
            assert radiobutton_page.get_results() == "No", "РЕЗУЛЬТАТ С КНОПОКЙ NO НЕКОРРЕКТНЫЙ!!!!"


    class TestWebTables:
        url = 'https://demoqa.com/webtables'

        def test_webtable_add_person(self, driver):
            webtabel_page = WebTabelPage(driver, self.url)
            webtabel_page.open()
            webtabel_page.click_add_button()
            webtabel_page.fill_registration_form()



