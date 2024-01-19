from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from multiprocessing import Pool
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import time

successful_accounts = 0
failed_accounts = 0


def process_seed_phrase(seed_phrase, proxy_data):
    metamask_password = 'ayodude0'
    extention_path = f'C:/Users/user/Desktop/metamask-chrome-11.7.2.crx'  #сюда путь к расширению обязательно указывайте свой путь этот путь ради примера

    ip, port, proxy_login, proxy_password = proxy_data.split(':')

    options = Options()

    #вставляйте сюда удаляя этот текст

    options.add_argument(f"user-agent={UserAgent().random}")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_extension(extention_path)

    proxy_options = {
        'proxy': {
            "https": f"https://{proxy_login}:{proxy_password}@{ip}:{port}"
        }
    }

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options,
                              seleniumwire_options=proxy_options,
                              )
    # stealth(driver,
    #         languages=['en-US', 'en'],
    #         vendor='Google Inc.',
    #         platform='Win32',
    #         webgl_vendor='Intel Inc.',
    #         renderer='Intel Iris OpenGL Engine',
    #         fix_hairline=True)

    driver.implicitly_wait(15)
    driver.maximize_window()
    time.sleep(3)
    metamask_handle = driver.window_handles[1]
    general_handle = driver.window_handles[0]
    driver.switch_to.window(metamask_handle)
    driver.close()
    time.sleep(1)
    driver.switch_to.window(general_handle)
    driver.get("chrome-extension://mjhmoaiphclhkpanfgkpmaafipgnljfc/home.html#onboarding/welcome")
    time.sleep(3)
    driver.find_element(by=By.XPATH, value='//*[@id="onboarding__terms-checkbox"]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[3]/button').click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div/button[1]').click()
    recovery_phrase = seed_phrase.split()

    for num, word in enumerate(recovery_phrase):
        element_id = f'import-srp__srp-word-{num}'
        driver.find_element(by=By.ID, value=element_id).send_keys(word)
    time.sleep(0.5)
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/button').click()
    # #вводим пароль

    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(metamask_password)
    time.sleep(0.5)
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(metamask_password)
    time.sleep(0.5)
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/h5/span').click()
    time.sleep(0.5)
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button').click()
    time.sleep(3)
    #oznokomleniye
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button').click()
    time.sleep(0.5)
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button').click()
    time.sleep(0.5)
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button').click()
    time.sleep(2)
    #ubirayem banner
    driver.find_element(by=By.XPATH, value='//*[@id="popover-content"]/div/div/section/div[1]/div/button/span').click()
    time.sleep(1)


    #-------------------------Galxe---https://galxe.com/Berachain/campaign/GCTN3ttM4T
    url = 'https://galxe.com/Berachain/campaign/GCTN3ttM4T'
    driver.get(url)
    #login //*[@id="ga-data-campaign-model-2"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/button
    driver.find_element(by=By.XPATH, value='//*[@id="ga-data-campaign-model-2"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/button').click()
    #metamask_select //*[@id="app"]/div[4]/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[4]/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div').click()
    time.sleep(0.5)
    driver.switch_to.window(driver.window_handles[-1])
    #delee //*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]').click()
    #podklyucitsa //*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]').click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])
    #voyty //*[@id="app-content"]/div/div/div/div[5]/footer/button[2]
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div/div/div[5]/footer/button[2]').click()
    time.sleep(3)
    print('вошел')
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    #claimed-button //*[@id="ga-data-campaign-model-2"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/button
    claimed_button = driver.find_elements(by=By.XPATH, value='//*[@id="ga-data-campaign-model-2"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/button')
    # task-uncompleted //*[@id="ga-data-campaign-model-2"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/button
    task_uncompleted = driver.find_elements(by=By.XPATH, value='//*[@id="ga-data-campaign-model-2"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/button')
    # task-completed //*[@id="ga-data-campaign-model-2"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/button
    task_completed = driver.find_elements(by=By.XPATH, value='//*[@id="ga-data-campaign-model-2"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/button')
    if claimed_button:
        print('ХП уже была заклеймлена')
    elif task_uncompleted:
        time.sleep(0.5)
        # click-task //*[@id="ga-data-campaign-model-2"]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/button
        driver.find_element(by=By.XPATH, value='//*[@id="ga-data-campaign-model-2"]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/button').click()
        print('сейчас перешел на страницу с краном')
        galxe_handle = driver.window_handles[0]
        time.sleep(5)
        driver.switch_to.window(galxe_handle)
        time.sleep(5)
        #ждем появления элемента
        element_to_wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ga-data-campaign-model-2"]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/button/div[2]/div/div/div/div/div/div'))
        )
        # Продолжайте выполнение действий после успешного появления элемента
        element_to_wait.click()
        #check-in //*[@id="ga-data-campaign-model-2"]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/button/div[2]/div/div/div/div/div/div
        # driver.find_element(by=By.XPATH, value='//*[@id="ga-data-campaign-model-2"]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/button/div[2]/div/div/div/div/div/div').click()
        time.sleep(5)
        task_completed_1 = driver.find_elements(by=By.XPATH, value='//*[@id="ga-data-campaign-model-2"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/button')
        #task-completed-claim-points //*[@id="ga-data-campaign-model-2"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/button
        if task_completed_1:
            driver.find_element(by=By.XPATH, value='//*[@id="ga-data-campaign-model-2"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/button').click()
            print('Сделал от начала и буду клеймить поинты')
            time.sleep(3)
            #transaction-has-been-submited //*[@id="app"]/div[7]/div/div/div/div[1]/div[1]/div[1]
            # transaction_been_submited = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[7]/div/div/div/div[1]/div[1]/div[1]')
            # if transaction_been_submited.text == 'Transaction has been submitted':
            print('Заклеймлил поинты')
    elif task_completed:
        print('Кто то тыкал до меня но не заклеймил, исправляю')
        driver.find_element(by=By.XPATH, value='//*[@id="ga-data-campaign-model-2"]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/button').click()
        time.sleep(2)
        #transaction submited //*[@id="app"]/div[5]/div/div/div/div[1]/div[1]/div[1]
        transaction_submited = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[5]/div/div/div/div[1]/div[1]/div[1]')
        time.sleep(2)
        if transaction_submited.text == 'Transaction has been submitted':
            print("Заклеймлил поинты")
    driver.quit()



with open('seed_phrase.txt', 'r') as seed_file, open('proxies.txt', 'r') as proxy_file, open('failed_accounts.txt', 'w') as failed_file:
    seed_phrases = seed_file.readlines()
    proxies = proxy_file.readlines()

    for account_number, (seed_phrase, proxy_data) in enumerate(zip(seed_phrases, proxies), start=1):
        print('#-------------------------------------------------------------------')
        print(f"Обработка аккаунта {account_number}")
        print('#-------------------------------------------------------------------')

        try:
            process_seed_phrase(seed_phrase.strip(), proxy_data.strip())
            successful_accounts += 1
        except Exception as e:
            print(f"Ошибка при обработке аккаунта {account_number}: {e}")
            failed_accounts += 1
            failed_file.write(f"Аккаунт {account_number}: {seed_phrase.strip()}\n")
print(f'#-------------------------------------------------------------------')
print(f"Общее количество успешных аккаунтов: {successful_accounts}")
print(f"Общее количество аккаунтов с ошибками: {failed_accounts}")
