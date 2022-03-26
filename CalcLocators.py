from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Chrome_Locators:
	LOCATOR_GOOGLE_SEARCH_FIELD = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
	LOCATOR_GOOGLE_CALC = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div[2]')


class Calc_Locators:
	LOCATOR_BUTTON_ZERO = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[1]/div/div')
	LOCATOR_BUTTON_ONE = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[1]/div/div')
	LOCATOR_BUTTON_TWO = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div')
	LOCATOR_BUTTON_THREE = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[3]/div/div')
	LOCATOR_BUTTON_FOUR = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[1]/div/div')
	LOCATOR_BUTTON_FIVE = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[2]/div/div')
	LOCATOR_BUTTON_SIX = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[3]/div/div')
	LOCATOR_BUTTON_SEVEN = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[1]/div/div')
	LOCATOR_BUTTON_EIGHT = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[2]/div/div')
	LOCATOR_BUTTON_NINE = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[3]/div/div')
	
	LOCATOR_BUTTON_PLUS = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[4]/div/div')
	LOCATOR_BUTTON_SUBTRAC = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[4]/div/div')
	LOCATOR_BUTTON_MP = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[4]/div/div')
	LOCATOR_BUTTON_DV = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[4]/div/div')
	LOCATOR_BUTTON_RES = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div')
	
	# MORE BUTTONS 

	LOCATOR_BUTTON_REC_RESULT = (By.CSS_SELECTOR, "#cwos") 

class Functions (BasePage):

	def enter_word(self, word):
		search_field = self.find_element(Chrome_Locators.LOCATOR_GOOGLE_SEARCH_FIELD)
		search_field.click()
		search_field.send_keys(word)
		search_field.send_keys(Keys.RETURN)
		return search_field

	def click_on_the_calc(self):
		return self.find_element(Chrome_Locators.LOCATOR_GOOGLE_CALC).click()

	def check_calc_result(self):
		result = self.find_element(Calc_Locators.LOCATOR_BUTTON_REC_RESULT)
		true_res=result.get_attribute("innerHTML")
		return true_res
    
	def press_button_zero (self):
		calc_input=self.find_element(Calc_Locators.LOCATOR_BUTTON_ZERO)
		return calc_input.send_keys(Keys.RETURN)


	def press_button_one (self):
		calc_input=self.find_element(Calc_Locators.LOCATOR_BUTTON_ONE)
		return calc_input.send_keys(Keys.RETURN)
		
	#MORE FUNC
	
	def press_button_plus(self):
		calc_input=self.find_element(Calc_Locators.LOCATOR_BUTTON_PLUS)
		return calc_input.send_keys(Keys.RETURN)
	
	def press_button_res(self):
		calc_input=self.find_element(Calc_Locators.LOCATOR_BUTTON_RES)
		return calc_input.send_keys(Keys.RETURN)