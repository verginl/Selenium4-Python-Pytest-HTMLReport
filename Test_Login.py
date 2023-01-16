from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest import mark
from _pytest.mark.structures import Mark
import pytest

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

@pytest.fixture
def setUp():
    driver = webdriver.Chrome(options=options)
    driver.minimize_window()
    driver.get("https://demoqa.com/login")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

#============================ TEST CASE LOGIN SUCCESS ============================#
@pytest.mark.loginsuccess
def test_login_success(setUp):
    txtUsername = setUp.find_element(By.ID, "userName")
    txtUsername.send_keys("verginardian")

    txtPassword = setUp.find_element(By.ID, "password")
    txtPassword.send_keys("Verginardian123*")

    btnLogin = setUp.find_element(By.XPATH, "//*[@id='login']")
    setUp.execute_script("arguments[0].click();", btnLogin)

    invalidText = setUp.find_element(By.XPATH,"//*[@id='userName-value']").text
    assert invalidText == "verginardian"  
#=================================================================================#  


#====================== DATA UNTUK TEST CASE LOGIN NEGATIF =======================#
AuthData = [
    ("verginardian","passwordsalah"),
    ("usernamesalah","Verginardian123*"),
    ("usernamesalah","passwordsalah") 
]
#=================================================================================#


#============================= TEST CASE LOGIN FAIL ==============================#
@pytest.mark.loginfail
@pytest.mark.parametrize('username,password',AuthData)
def test_login_fail(setUp,username,password):
    txtUsername = setUp.find_element(By.ID, "userName")
    txtUsername.send_keys(username)
    
    txtPassword = setUp.find_element(By.ID, "password")
    txtPassword.send_keys(password)
    
    btnLogin = setUp.find_element(By.XPATH, "//*[@id='login']")
    setUp.execute_script("arguments[0].click();", btnLogin)
    
    invalidText = setUp.find_element(By.XPATH,"//*[@id='name']").text
    assert invalidText == "Invalid username or password!"
#=================================================================================#