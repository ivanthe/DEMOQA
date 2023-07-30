import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage

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
            webtable_page.check_new_person_in_table(new_person, full_list)

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
            webtable_page.click_add_button()
            new_person = webtable_page.fill_registration_form()  #Создаем новые данные
            webtable_page.search_some_person(new_person[1])   # Ищем новосозданного человека в списке
            new_value = webtable_page.update_person_info()  #Изменяем данные новосозданного человека и возвращаем
                                                            # номер пункта, который измеряли и новое значение
            updated_person = webtable_page.get_updated_person(new_person, new_value) #На основании данных новосозданного
                                                            # человека, создаем новый списко после обновления
            webtable_page.search_some_person('')        #Удаляем фильтр поиска
            full_list = webtable_page.get_table_data()      #Получаем полный список
            assert new_person not in full_list, "Данные об измененном сотруднике присуствуют в списае после изменения"
            assert updated_person in full_list, "Измененные данные отсутствуют в списке"







