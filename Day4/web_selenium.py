# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=options) # Requires chromedriver in the place where code resides

# For Safari, must turn on Remote ______ in Developer Settings of Safari

driver.get("https://www.saucedemo.com/v1/")
print("The title of the website is" + driver.title)


# Authentication

username = "performance_glitch_user" # performance_glitch_user, standard_user
password = "secret_sauce"


username_input = driver.find_element(By.ID,"user-name")
password_input = driver.find_element(By.XPATH,'//*[@id="password"]')
login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')


username_input.send_keys(username)
password_input.send_keys(password)
login_button.click() # or login_button.submit() , since it is a form so submit function is allowed



# Adding Only Tshirts to cart

items = driver.find_elements(By.CLASS_NAME, 'inventory_item')
print("Items available are: ")


for item in items:
    item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
    print(item_name)
    if "T-Shirt" in item_name:
        # #inventory_container > div > div:nth-child(3) > div.pricebar > button
        # since nth-child(3) depends on the div we select, we don't want that
        # As we want to find the same "add to cart" button in every div despite the child number for the div list
        # we remove the nth-child(3) and use it
        add_to_cart_button = item.find_element(By.CSS_SELECTOR, "#inventory_container > div > div > div.pricebar > button")
        add_to_cart_button.click()

# Go to Cart
cart_button = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
cart_button.click()

# Remove Item that cost more than 49 dollars


# Checking out
checkout_button = driver.find_element(By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button")
checkout_button.click()


# Input Information
input_fields = driver.find_elements(By.TAG_NAME, "input")
input_data = ["John", "Doe", "123124"]
for input_field, input_data in zip(input_fields,input_data):
    input_field.send_keys(input_data)

input_fields[-1].submit() # or find the continue element and click it


# Finish Checkout
# btn_action cart_button -> should be used as btn_action.cart_button


# Define an explicit wait with a timeout of 10 seconds
wait = WebDriverWait(driver, 10)

# Locate the finish button element using a CSS selector
finish_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_action.cart_button")))

# Click the finish button
finish_button.click()
