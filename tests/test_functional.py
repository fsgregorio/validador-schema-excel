from selenium import webdriver
import pytest
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Inicia o Streamlit em background
    streamlit_process = subprocess.Popen(["streamlit", "run", "src/frontend.py"])
    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(10)
    yield driver
    # Cleanup: fecha o WebDriver e mata o processo do Streamlit
    driver.quit()
    streamlit_process.kill()

def test_app_opens(driver):
    driver.get("http://localhost:8501")
    
    # Aguarda até que o elemento <h1> esteja presente, com timeout de 10 segundos
    wait = WebDriverWait(driver, 10)
    h1_elem = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    p_elem = wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    
    # Verifica o título da página e os textos dos elementos
    assert driver.title == "Excel Validator"
    assert h1_elem.text == "Excel Validator"
    assert p_elem.text == "Upload an Excel file and we will validate it for you."
