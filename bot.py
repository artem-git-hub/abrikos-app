import telebot
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



bot = telebot.TeleBot("Тут тег бота")

@bot.message_handler(content_types = ['text'])
def get_text(massage):
	if massage.text.lower() == "привет":
		bot.send_message(massage.chat.id, "HIEUHHsuhsihsgseid")


		chrome_options = webdriver.ChromeOptions()
		chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-dev-shm-usage")
		chrome_options.add_argument("--no-sandbox")
		driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

		driver.get('https://filecr.com/windows/photoshop-adobe/')
		but = driver.find_element_by_xpath('//*[@id="sh_pdf_download-2"]/form/a')
		driver.execute_script("arguments[0].click();", but)
		sleep(10)

		a = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[2]/a')
		link = a.get_attribute('href')


		bot.send_message(massage.chat.id,link)


bot.polling(none_stop = True, interval = 0)