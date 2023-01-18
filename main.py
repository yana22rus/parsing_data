from time import sleep
from os import devnull
import json
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from db import *

driver = webdriver.Firefox(service_log_path=devnull)
driver.implicitly_wait(1)
driver.maximize_window()

driver.get("https://stepik.org/learn?auth=login")

sleep(1)

with open("authentication_data.json") as f:
    data = json.load(f)

driver.find_element(By.NAME, "login").send_keys(data["login"])

driver.find_element(By.NAME, "password").send_keys(data["password"])

driver.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()

sleep(3)

driver.get("https://stepik.org/lesson/6433/step/1?unit=1240")

sleep(5)

# TODO спарсить url в которых есть данные для парсинга, спарсить код

for x in range(302):

    d = {}

    try:

        if "Напишите программу" in driver.find_element(By.XPATH, "//h3").text:

            with open("Программирование_на_Python.txt", "a") as f:
                f.writelines(driver.current_url + "\n")

            sample_input1 = driver.find_element(By.CSS_SELECTOR, ".step-text__limit-value:nth-child(2)").text
            sample_output1 = driver.find_element(By.CSS_SELECTOR, ".step-text__limit-value:nth-child(4)").text

            d[sample_input1] = sample_output1

            sample_input2 = driver.find_element(By.CSS_SELECTOR, ".step-text__limit-value:nth-child(6)").text
            sample_output2 = driver.find_element(By.CSS_SELECTOR, ".step-text__limit-value:nth-child(8)").text

            d[sample_input2] = sample_output2

            # create_data(json.dumps(d))

            # driver.find_element(By.LINK_TEXT, "Ваши решения").click()
            #
            # driver.find_element(By.XPATH, "//a[@id='ember7065']/span[2]").click()
            #
            # print(driver.find_element(By.XPATH, "//code").text)
            #
            # print(json.dumps(d))

        driver.find_element(By.CSS_SELECTOR, ".lesson__next-btn").click()

    except Exception:

        print(Exception)

        driver.find_element(By.CSS_SELECTOR, ".lesson__next-btn").click()

        continue

driver.close()
