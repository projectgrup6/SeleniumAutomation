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
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")  # Fixes some issues on Windows
    options.add_argument("--window-size=1920,1080")  # Set browser resolution
    options.add_argument("--no-sandbox")  # Required for Jenkins/Linux
    options.add_argument("--disable-dev-shm-usage")  # Helps with memory issues
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


