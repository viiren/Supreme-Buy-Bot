from selenium import webdriver
from config import keys
import time
#from datetime import datetime
#from threading import Timer


#Timer which inputs time taken for each item to process. 
def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper

@timeme
def order():
    # Adds item to Cart
    driver.find_element_by_name('commit').click()

    #Time.Sleep essentially waits for the checkout button to load onto the screen
    time.sleep(.3)
    checkout_element = driver.find_element_by_class_name('checkout')
    checkout_element.click()

    #Fills Checkout Page 
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['phone_number'])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['street_address'])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip_code'])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
    driver.find_element_by_xpath('//*[@id="order_billing_country"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[10]').click()
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[9]').click()
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys['card_cvv'])
    driver.find_element_by_id('nnaerb').send_keys(keys['card_number'])
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()


if __name__ == '__main__':
        # Loads up chrome 
    driver = webdriver.Chrome('./chromedriver')

    #Gets the URL of the item you want to buy
    driver.get(keys['product_url'])
    order()

    
