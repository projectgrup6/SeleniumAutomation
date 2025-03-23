from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
edge_path=r"C:\Users\lavan\Downloads\edgedriver_win64\msedgedriver.exe"
@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--start-maximized")  # Open in full screen
    options.add_argument("--remote-allow-origins=*")  # Allow remote connections
    if "--headless" in options.arguments:
        options.arguments.remove("--headless")
    services = Service(executable_path=edge_path)
    driver = webdriver.Edge(service=services, options=options)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()
def test_login(driver):
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
    username.send_keys("Admin")
    password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
    password.send_keys("admin123")
    button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
    button.click()
    time.sleep(8)


