from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class ShopSimulation:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def login(self):
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(2)  # Wait for the page to load

        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        login_button.click()

        time.sleep(2)  # Wait for the login to complete

    def add_to_cart(self, item_name):
        item = self.driver.find_element(By.XPATH, f"//div[text()='{item_name}']")
        item.click()

        time.sleep(2)  # Wait for the item page to load

        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    shop_sim = ShopSimulation("standard_user", "secret_sauce")
    shop_sim.login()
    shop_sim.add_to_cart("Sauce Labs Backpack")
    shop_sim.quit()
