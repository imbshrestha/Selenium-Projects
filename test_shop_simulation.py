import pytest
from selenium.webdriver.common.by import By
from shop_simulation import ShopSimulation

@pytest.fixture
def shop_sim(mocker):
    # Mock Chrome WebDriver
    mocker.patch('shop_simulation.webdriver.Chrome')
    return ShopSimulation("standard_user", "secret_sauce")

def test_login(shop_sim, mocker):
    mocker.patch.object(shop_sim.driver, 'get')
    mocker.patch.object(shop_sim.driver, 'find_element')
    mocker.patch.object(shop_sim.driver, 'quit')

    shop_sim.login()

    shop_sim.driver.get.assert_called_with("https://www.saucedemo.com/")
    assert shop_sim.driver.find_element.call_count == 3  # user-name, password, login button

def test_add_to_cart(shop_sim, mocker):
    mocker.patch.object(shop_sim.driver, 'find_element')
    mocker.patch.object(shop_sim.driver, 'quit')

    shop_sim.add_to_cart("Sauce Labs Backpack")

    assert shop_sim.driver.find_element.call_count == 2  # item and add to cart button

def test_quit(shop_sim, mocker):
    mocker.patch.object(shop_sim.driver, 'quit')

    shop_sim.quit()

    shop_sim.driver.quit.assert_called_once()
