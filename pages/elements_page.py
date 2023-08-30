import random
import time
import pyautogui as pag
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from generator.generator import generator_person, webtable_generator_person
from locators.elements_page_locators import TextBoxElementsLocator, CheckBoxLocators, RadioButtonLocators, \
    WebTableLocators, ButtonsLocators, LinkPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class TextBoxPage(BasePage):
    locator = TextBoxElementsLocator()

    def fill_all_filds(self):
        person_info = next(generator_person())
        full_name = person_info.full_name
        email = person_info.email
        current_adress = person_info.current_address
        permanent_adress = person_info.permanent_address
        self.element_is_present(self.locator.FULL_NAME).send_keys(full_name)
        self.element_is_present(self.locator.EMAIL).send_keys(email)
        self.element_is_present(self.locator.CURRENT_ADDRESS).send_keys(current_adress)
        self.element_is_present(self.locator.PERMANENT_ADDRESS).send_keys(permanent_adress)

        self.element_is_present(self.locator.SUBMIT_BUTTON).click()

        return full_name, email, current_adress, permanent_adress
        # self.element_is_visible(self.*TextBoxElementsLocator.FULL_NAME).send_keys()

    def check_filled_form(self):
        full_name = self.element_is_present(self.locator.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locator.CREATED_EMAIL).text.split(':')[1]
        current_adress = self.element_is_present(self.locator.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_adress = self.element_is_present(self.locator.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_adress, permanent_adress


class CheckBoxPage(BasePage):
    locator = CheckBoxLocators

    def open_full_list(self):
        self.element_is_visible(self.locator.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.element_are_visible(self.locator.ITEM_LIST)

        """   ====
        Below is one of the ways to click random list items implemented using a WHILE-loop
        ===   """

        """count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item_list[random.randint(1, 15)])
                item.click()
                count -=1
                #print(item.text)
            else:
                break"""

        random_value = random.randint(1, len(item_list))
        for i in range(0, random_value):
            item = item_list[random.randint(1, 15)]
            self.go_to_element(item)
            item.click()

    def get_list_with_clicked_item(self):
        checked_item = self.element_are_present(self.locator.CHECKED_ITEM)
        data = []
        for box in checked_item:
            title_item = box.find_element(By.XPATH, self.locator.TITLE_ITEM)
            data.append(title_item.text.lower().replace(" ", "").split('.')[0])
        return data

    def get_list_with_results(self):
        result_item = self.element_are_present(self.locator.RESULT_ITEM)
        data = []
        for box in result_item:
            data.append(box.text.lower())
        return data

    def compare_results(self, clicked_items, result_item):
        assert clicked_items == result_item, "Результат не совпадает"


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators

    def get_radiobuttons_quantity(self):
        radioButtons_list = self.element_are_present(self.locators.RADIO_BUTTONS_LIST)
        return len(radioButtons_list)

    def click_radio_buttons(self, choise):
        choises = {"yes": self.locators.YES_BUTTON,
                   "impessive": self.locators.IMPRESSIVE_BUTTON,
                   "no": self.locators.NO_BUTTON
                   }
        self.element_is_clickable(choises[choise]).click()

    def get_results(self):
        text = self.element_is_present(self.locators.ACTUAL_RESULT).text
        return text


class WebTablePage(BasePage):
    locators = WebTableLocators

    def check_reg_form_is_appeard(self):
        try:
            self.element_is_present(self.locators.REGISTRATION_FORM)
        except TimeoutException:
            return False
        return True

    def click_add_button(self):
        self.element_is_present(self.locators.ADD_BUTTON).click()
        assert self.check_reg_form_is_appeard() == True, 'Форма регистрации не появилась'

    def fill_registration_form(self):
        person_info = next(webtable_generator_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        new_added_person = [first_name, last_name, str(age), email, str(salary), department]
        self.element_is_present(self.locators.FIRST_NAME_REG_FORM).send_keys(first_name)
        self.element_is_present(self.locators.LAST_NAME_RAG_FORM).send_keys(last_name)
        self.element_is_present(self.locators.EMAIL_REG_FORM).send_keys(email)
        self.element_is_present(self.locators.AGE_REG_FORM).send_keys(age)
        self.element_is_present(self.locators.SALARY_REG_FORM).send_keys(salary)
        self.element_is_present(self.locators.DEPARTMEMT_REG_FORM).send_keys(department)
        self.element_is_present(self.locators.SUBMIT_BUTTON_REG_FORM).click()
        return new_added_person

    def get_table_data(self):
        people_data = self.element_are_present(self.locators.PEOPLE_DATA)
        data = []
        for index in people_data:
            data.append(index.text.splitlines())
        return data

    def check_new_person_in_table(self, new_person, full_list):
        assert new_person in full_list, "ДАННЫЕ НОВОГО СОТРУДНИКА НЕ ВНЕСЕНЫ В ТАБЛИЦУ ИЛИ ВНЕСЕНЫ НЕ КОРРЕКТНО!!!"

    def search_some_person(self, key_word):
        self.element_is_present(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(webtable_generator_person())
        index = random.randint(0, 5)
        time.sleep(2)
        if index == 0:
            self.element_is_present(self.locators.FIRST_NAME_REG_FORM).clear()
            self.element_is_present(self.locators.FIRST_NAME_REG_FORM).send_keys(person_info.first_name)
            data = [index, person_info.first_name]
        if index == 1:
            self.element_is_present(self.locators.LAST_NAME_RAG_FORM).clear()
            self.element_is_present(self.locators.LAST_NAME_RAG_FORM).send_keys(person_info.last_name)
            data = [index, person_info.last_name]
        if index == 2:
            self.element_is_present(self.locators.AGE_REG_FORM).clear()
            self.element_is_present(self.locators.AGE_REG_FORM).send_keys(person_info.age)
            data = [index, str(person_info.age)]
        if index == 3:
            self.element_is_present(self.locators.EMAIL_REG_FORM).clear()
            self.element_is_present(self.locators.EMAIL_REG_FORM).send_keys(person_info.email)
            data = [index, person_info.email]
        if index == 4:
            self.element_is_present(self.locators.SALARY_REG_FORM).clear()
            self.element_is_present(self.locators.SALARY_REG_FORM).send_keys(person_info.salary)
            data = [index, str(person_info.salary)]
        if index == 5:
            self.element_is_present(self.locators.DEPARTMEMT_REG_FORM).clear()
            self.element_is_present(self.locators.DEPARTMEMT_REG_FORM).send_keys(person_info.department)
            data = [index, person_info.department]
        self.element_is_visible(self.locators.SUBMIT_BUTTON_REG_FORM).click()
        return data

    def get_updated_person(self, new_person, data):
        updated_person = []
        for box in new_person:
            updated_person.append(box)
        updated_person[data[0]] = data[1]
        return updated_person

    def clear_input_search(self):
        self.element_is_present(self.locators.SEARCH_INPUT).click()
        self.element_is_present(self.locators.SEARCH_INPUT).clear()
        time.sleep(20)
        """self.element_is_present(self.locators.SEARCH_INPUT).send_keys(pag.hotkey('ctrl', 'a'))
        time.sleep(2)
        self.element_is_present(self.locators.SEARCH_INPUT).send_keys(pag.press('delete'))
        time.sleep(1)"""
        #self.element_is_present(self.locators.SEARCH_INPUT).send_keys('Insurance')
        #self.element_is_present(self.locators.SEARCH_INPUT).clear()

        time.sleep(5)

    def update_random_record(self):

        records_list = self.element_are_present(self.locators.UPDATE_BUTTON)
        random_record = random.randint(1, len(records_list))-1
        old_person_data = self.get_table_data()[random_record]
        res = records_list[random_record].find_element(By.XPATH, self.locators.ROW_PARENT)
        res.find_element(By.CSS_SELECTOR, 'span[class=mr-2]').click()
        self.update_person_info()
        new_person_data = self.get_table_data()[random_record]
        return old_person_data, new_person_data

class ButtonsPage(BasePage):
    locators = ButtonsLocators

    def click_left_button(self):
        self.element_is_present(self.locators.BUTTON_LEFT_CLICK).click()

    def click_left_button_double_click(self):
        action = ActionChains(self.driver)
        action.double_click(on_element=self.element_is_present(self.locators.BUTTON_DOUBLE_CLICK))
        action.perform()

    def click_right_button(self):
        action = ActionChains(self.driver)
        action.context_click(on_element=self.element_is_present(self.locators.BUTTON_RIGHT_CLICK)).perform()

    def get_result_of_button_double_click(self):
        return self.element_is_present(self.locators.RESULT_DOUBLE_CLICK).text

    def get_result_of_right_button_click(self):
        return self.element_is_present(self.locators.RESULT_RIGHT_CLICK).text

    def get_result_of_button_click(self):
        return self.element_is_present(self.locators.RESULT_LEFT_CLICK).text

class LinksPage(BasePage):
    locators = LinkPageLocators

    def check_opened_page(self):
        simple_link = self.element_is_visible(self.locators.HOME_SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code



