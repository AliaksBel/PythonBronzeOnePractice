import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")
        
        # Заполнить поля
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@mail.com")
        
        # Отправить
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # Проверить регистрацию
        time.sleep(5)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    
    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")
        
        # Заполнить поля
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@mail.com")
        
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        time.sleep(5)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()