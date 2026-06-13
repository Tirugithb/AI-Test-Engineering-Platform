import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)

def setup_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

def test_mandatory_field_validation(driver):
    driver.get("http://example.com/form")
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error"))
        )
        assert "This field is required" in error_message.text
    except Exception as e:
        logging.error(f"Error during mandatory field validation: {e}")
    finally:
        logging.info("Mandatory field validation completed.")

def test_equivalence_partitioning(driver):
    input_field = driver.find_element(By.ID, "username")
    test_cases = ["validUser", "us", "a" * 21]  # valid, too short, too long
    expected_messages = [None, "Username must be at least 3 characters.", "Username cannot be more than 20 characters."]

    for i, test_case in enumerate(test_cases):
        input_field.clear()
        input_field.send_keys(test_case)
        driver.find_element(By.ID, "submit").click()

        try:
            if expected_messages[i]:
                error_message = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "error"))
                )
                assert expected_messages[i] in error_message.text
            else:
                assert driver.current_url == "http://example.com/success"
        except Exception as e:
            logging.error(f"Error in equivalence partitioning test case {i}: {e}")

def cleanup(driver):
    driver.quit()

if __name__ == "__main__":
    driver = setup_driver()
    try:
        test_mandatory_field_validation(driver)
        test_equivalence_partitioning(driver)
    finally:
        cleanup(driver)