import time
from generator.generator import generator_person
from locators.elements_page_locators import TextBoxElementsLocator
from pages.base_page import BasePage

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
