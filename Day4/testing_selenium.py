from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import init, Fore, Style


# Initialize colorama
init(autoreset=True)

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

def print_colored(text, color):
    colors = {"red": Fore.RED, "green": Fore.GREEN, "reset": Style.RESET_ALL}
    print(colors[color] + text + colors["reset"])

try:
    # Test 1: Open the website
    driver.get("https://www.saucedemo.com/v1/")
    print_colored("Test 1 Passed: The title of the website is " + driver.title, "green")
except Exception as e:
    print_colored("Test 1 Failed: " + str(e), "red")

# Authentication
username = "problem_user"  # performance_glitch_user, standard_user, problem_user, locked_out_user
password = "secret_sauce"

try:
    # Test 2: Find and interact with username and password input fields, and login button
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    print_colored("Test 2 Passed: Authentication successful", "green")
except Exception as e:
    print_colored("Test 2 Failed: " + str(e), "red")

try:
    # Test 3: Find and print all available items
    items = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    print_colored("Test 3 Passed: Items available are: ", "green")
    for item in items:
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        print(item_name)
except Exception as e:
    print_colored("Test 3 Failed: " + str(e), "red")

try:
    # Test 4: Add only T-Shirts to the cart
    for item in items:
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        if "T-Shirt" in item_name:
            add_to_cart_button = item.find_element(By.CSS_SELECTOR, "#inventory_container > div > div > div.pricebar > button")
            add_to_cart_button.click()
    print_colored("Test 4 Passed: T-Shirts added to cart", "green")
except Exception as e:
    print_colored("Test 4 Failed: " + str(e), "red")

try:
    # Test 5: Go to cart
    cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button.click()
    print_colored("Test 5 Passed: Navigated to cart", "green")
except Exception as e:
    print_colored("Test 5 Failed: " + str(e), "red")

try:
    # Test 6: Checkout
    checkout_button = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button")
    checkout_button.click()
    print_colored("Test 6 Passed: Checkout initiated", "green")
except Exception as e:
    print_colored("Test 6 Failed: " + str(e), "red")

try:
    # Test 7: Input user information for checkout
    input_fields = driver.find_elements(By.TAG_NAME, "input")
    input_data = ["John", "Doe", "123124"]
    for input_field, data in zip(input_fields, input_data):
        input_field.send_keys(data)
    input_fields[-1].submit()
    print_colored("Test 7 Passed: User information submitted", "green")
except Exception as e:
    print_colored("Test 7 Failed: " + str(e), "red")

try:
    # Test 8: Finish checkout
    finish_button = driver.find_element(By.CLASS_NAME, "btn_action.cart_button")
    finish_button.click()
    print_colored("Test 8 Passed: Checkout finished", "green")
except Exception as e:
    print_colored("Test 8 Failed: " + str(e), "red")


try:
    # Test 9: Logout
    menu_slider = driver.find_element(By.XPATH, '//*[@id="menu_button_container"]/div/div[3]/div/button')
    menu_slider.click()
    logout_button = driver.find_element(By.ID, "logout_sidebar_link")
    logout_button.click()
    print_colored("Test 9 Passed: Logout", "green")
except Exception as e:
    print_colored("Test 9 Failed: " + str(e), "red")
