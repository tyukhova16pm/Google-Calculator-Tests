from CalcLocators import Functions
import time

def test_calc_exp(browser):
	google_calc_test = Functions(browser)
	google_calc_test.go_to_site()
	google_calc_test.enter_word('Калькулятор')

	google_calc_test.click_on_the_calc()
	google_calc_test.press_button_one()
	google_calc_test.press_button_plus()
	google_calc_test.press_button_one()
	google_calc_test.press_button_res()

	result_element = google_calc_test.check_calc_result()
	assert '2' in result_element