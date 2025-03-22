import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from langchain_community.document_loaders import DirectoryLoader




DATA_PATH = "/mnt/d/Books"

def browseCatalog(query):
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.get("https://librivox.org/")
    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)
    #input search
    searchBox = wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id=\"q\"]")))
    action.move_to_element(searchBox).click().send_keys(query).perform
    #submit search
    searchButton = wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id=\"searchsubmit\"]")))
    action.move_to_element(searchButton).click()
    action.perform()
    # result = wait.until(expected_conditions.presence_of_element_located((By.XPATH,"/html/body/div/div[3]/ul"))) 
    list = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,"/html/body/div/div[3]/ul/li")))
    driver.close()
    return list
def main():
    # results = browseCatalog("Hello")    
    # for item in results:
    #     print(f"{item}\n\n")
    
    # docs_loader = DirectoryLoader(DATA_PATH, glob="*.pdf")
    # docs = docs_loader.load()
    # print(docs)
    files =  os.listdir(DATA_PATH)
    for file in files:
        title = os.path.splitext(file)
        title = title.strip('.epub')
        title = title.strip( '.pdf')
        title = title.strip( '.libgen.li')
        title = title.strip( '.crdownload')

        print(title)

  
    

    


if __name__=="__main__":
    main()