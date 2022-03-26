import pytest
from selenium.webdriver import Chrome

@pytest.fixture(scope="session")
def browser():
  driver = Chrome()
  yield driver
  driver.quit()