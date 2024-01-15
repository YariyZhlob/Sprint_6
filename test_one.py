from selenium import webdriver

try:
    driver = webdriver.Firefox()
    print("Firefox установлен.")
except Exception as e:
    print(f"Ошибка: {e}")
    print("Firefox не установлен.")
finally:
    try:
        driver.quit()
    except:
        pass
