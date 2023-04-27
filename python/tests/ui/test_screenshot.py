import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.web
def test_creation_modal(selenium, base_url):
    selenium.get(base_url + "/web/index.html")
    navbar = WebDriverWait(selenium, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.navbar-header')))