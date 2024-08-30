import pandas as pd
import os
from rdkit import Chem
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

df = pd.read_excel('/Users/diegodelozada/PycharmProjects/PFG/Data/modelSEED_Filtered_rxnInfo.xlsx')
count = 8294
smiles = df['REACTION_SMILE']
ID = df['ID']


chrome_driver_path = '/Users/diegodelozada/E-zyme/chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


# Abre Selenzyme
driver.get("http://selenzyme.synbiochem.co.uk/")
time.sleep(2)

for i in range(8294,len(smiles)):
	textBox = driver.find_element(By.NAME, 'smarts')
	textBox.send_keys(smiles[i])

	time.sleep(1)

	body_element = driver.find_element(By.TAG_NAME, 'body')
	actions = ActionChains(driver)
	actions.move_to_element_with_offset(body_element, 10, 10)  # 10, 10 son las coordenadas x, y relativas al elemento encontrado
	actions.click()
	actions.perform()

	submit_button = WebDriverWait(driver, 10).until(
	    EC.element_to_be_clickable((By.ID, "upload"))
	)

	close_button = driver.find_element(By.CLASS_NAME, "ui-icon-closethick")
	close_button.click()


	elemento_submit = driver.find_element(By.ID, 'upload')
	elemento_submit.click()

	time.sleep(7)
	try:
		table = driver.find_element(By.CSS_SELECTOR, 'table.dataframe.Selenzy')
	except:
		continue

	# Extraer todas las filas de la tabla
	rows = table.find_elements(By.TAG_NAME, 'tr')

	# Lista para guardar los datos
	data = []

	# Iterar sobre las filas y extraer las celdas
	for row in rows:
	    cols = row.find_elements(By.TAG_NAME, 'td')
	    cols = [ele.text.strip() for ele in cols]
	    data.append([ele for ele in cols if ele])  # Añadir los datos si no están vacíos

	# Convertir a DataFrame de pandas
	df_results = pd.DataFrame(data)

	# Guardar en un archivo CSV
	df_results.to_csv(f'Selenzyme_results/{ID[i]}.csv', index=False)

	new_query_link = driver.find_element(By.LINK_TEXT, "[New query]")
	new_query_link.click()
	time.sleep(2)

	print(count)
	count = count + 1

driver.quit()