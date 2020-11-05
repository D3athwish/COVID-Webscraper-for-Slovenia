from selenium import webdriver


def x_path_send_keys(string, country):
    return driver.find_element_by_xpath(string).send_keys(country)


def x_path_click(string):
    return driver.find_element_by_xpath(string).click()


def x_path_output(string):
    return driver.find_element_by_xpath(string).text


driver = webdriver.Firefox()

# Open website and minimize window
driver.get("https://www.worldometers.info/coronavirus/")
driver.minimize_window()

# Scroll down to data table
driver.execute_script("window.scrollTo(0,2000)")

# Enter Slovenia into searchbox
x_path_send_keys("/html/body/div[3]/div[3]/div/div[4]/div[1]/div/div/div[1]/div[2]/div/label/input", "Slovenia")

# Click column button and select newly recovered by day and click
x_path_click("/html/body/div[3]/div[3]/div/div[3]/ul/div/button")
x_path_click("/html/body/div[3]/div[3]/div/div[3]/ul/div/ul/li[6]")

# Get latest data
current_infected = x_path_output("/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]/tr/td[9]")
new_recovered = x_path_output("/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]/tr/td[8]")
new_infected = x_path_output("/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]/tr/td[4]")
new_deaths = x_path_output("/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]/tr/td[6]")

# Output data
print(current_infected + " people in Slovenia are infected.")
print(new_infected[1:] + " people in Slovenia have been infected today.")
print(new_deaths[1:] + " people in Slovenia have died today.")
print(new_recovered[1:] + " people in Slovenia have recovered today.")

driver.close()
