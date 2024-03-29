import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    ImagesPage

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
            webtable_page = WebTablePage(driver, self.url)
            webtable_page.open()
            webtable_page.click_add_button()
            new_person = webtable_page.fill_registration_form()
            full_list = webtable_page.get_table_data()
            assert new_person in full_list, "ДАННЫЕ НОВОГО СОТРУДНИКА НЕ ВНЕСЕНЫ В ТАБЛИЦУ ИЛИ ВНЕСЕНЫ НЕ КОРРЕКТНО!!!"


        def test_webtable_search_function(self,driver):
            webtable_page = WebTablePage(driver, self.url)
            webtable_page.open()
            webtable_page.click_add_button()
            new_person = webtable_page.fill_registration_form()[random.randint(0, 6)]
            """webtable_page.search_some_person(new_person[random.randint(0, 6)])
            full_list = webtable_page.get_table_data()
            webtable_page.check_new_person_in_table(new_person, full_list)"""
            webtable_page.search_some_person(new_person)
            table_result = webtable_page.check_search_person()
            assert new_person in table_result, f"Ключевого слова {new_person} не найдено в списках кнопкой Search"
            time.sleep(5)

        def test_webtable_person_info(self, driver):
            webtable_page = WebTablePage(driver, self.url)
            webtable_page.open()
            old_person_data, new_person_data = webtable_page.update_random_record()
            print('СТАРЫЕ -  ', old_person_data)
            print('НОВЫЕ  -  ', new_person_data)
            full_list = webtable_page.get_table_data()
            assert new_person_data in full_list, "ДАННЫЕ НОВОГО СОТРУДНИКА НЕ ВНЕСЕНЫ В ТАБЛИЦУ ИЛИ " \
                                                 "ВНЕСЕНЫ НЕ КОРРЕКТНО!!!"
            assert old_person_data not in full_list, "Старые данные сотрудника присутствуют в базе"

    class TestButtons:
        url = 'https://demoqa.com/buttons'

        def test_left_button_double_click(self, driver):
            buttons_page = ButtonsPage(driver, self.url)
            buttons_page.open()
            buttons_page.click_left_button_double_click()
            actual_result = buttons_page.get_result_of_button_double_click()
            assert actual_result == 'You have done a double click', "Актуальное сообщение не соответствует ожидаемому " \
                                                                    "при нажатии Double Click Me"

        def test_right_button_click(self, driver):
            buttons_page = ButtonsPage(driver, self.url)
            buttons_page.open()
            buttons_page.click_right_button()
            time.sleep(5)
            actual_result = buttons_page.get_result_of_right_button_click()
            assert actual_result == 'You have done a right click', "Актуальное сообщение не соответствует ожидаемому " \
                                                                   "при нажании Right Click Me"

        def test_left_button_click(self, driver):
            buttons_page = ButtonsPage(driver, self.url)
            buttons_page.open()
            buttons_page.click_left_button()
            actual_result = buttons_page.get_result_of_button_click()
            assert actual_result == 'You have done a dynamic click', "Актуальное сообщение не соответствует ожидаемому " \
                                                                     "при нажании Click Me"

    class TestLinks:
        url = 'https://demoqa.com/links'

        def test_working_link(self, driver):
            links_page = LinksPage(driver, self.url)
            links_page.open()
            href_link, current_ulr = links_page.check_opened_page()
            assert href_link == current_ulr, f"Ожидался переход по ссылке {href_link}  , действильено перешли " \
                                             f"на {current_ulr}"

        def test_bad_request_link(self, driver):
            links_page = LinksPage(driver, self.url)
            links_page.open()
            response_code = links_page.check_bad_request_link('https://demoqa.com/bad-request')
            assert response_code == 400


    class TestImages:
        url = 'https://demoqa.com/broken'

        def test_images(self, driver):
            images_page = ImagesPage(driver, self.url)
            images_page.open()
            results = images_page.check_images()
            assert len(results) == 0, f'Следующие картинки сломаны: {results}'

        def test_links_are_working(self, driver):
            images_page = ImagesPage(driver, self.url)
            images_page.open()
            results = images_page.check_links()
            assert len(results) == 0, f'следующие ссылки сломаны, имеют статус код и ведут на страницу: {results}'




