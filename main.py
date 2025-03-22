import os 
# import nltk
import threading
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
# from langchain_community.document_loaders import DirectoryLoader
# from nltk.stem import PorterStemmer
# from nltk.corpus import stopwords



DATA_PATH = "/mnt/d/Books"

def browseCatalog(query):
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.get("https://librivox.org/")
    wait = WebDriverWait(driver, 5)
    action = ActionChains(driver)
    #input search
    searchBox = wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id=\"q\"]")))
    action.move_to_element(searchBox).click().send_keys(query).perform
    #submit search
    searchButton = wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id=\"searchsubmit\"]")))
    action.move_to_element(searchButton).click()
    action.perform()
    # result = wait.until(expected_conditions.presence_of_element_located((By.XPATH,"/html/body/div/div[3]/ul"))) 
    list = "No results found"
    try:
        list = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,"/html/body/div/div[3]/ul/li")))
    except:
        pass
    finally:
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
#     sentence = """At eight o'clock on Thursday morning
# ... Arthur didn't feel very good."""
    # stemmer = PorterStemmer
    # sentence = """('Хофштадтер, Дуглас Роберт - Gödel, Escher, Bach_ An Eternal Golden Braid (1999) - libgen.li', '.epub')"""
    # stopwords = stopwords.words('english') 
    # threads = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures= []
        for file in files:
            title,ext = os.path.splitext(file)
            # tokens = nltk.word_tokenize(title)
            title = title.replace("- libgen.li","")
            title = title.replace(".epub","")
            
            print("Start---------------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n")
            print(title)
            futures = [executor.submit(browseCatalog, title)]

            # thread = threading.Thread(target=browseCatalog,args=(title,))
            # threads.append(thread)
            # thread.start()
            # catalogList = browseCatalog(title)
            # print(catalogList)
            
            print("End---------------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n")
        for r in concurrent.futures.as_completed(futures):
            print(r.result)
    # for thread in threads:
    #     thread.join()
    
    
    
    for future in concurrent.futures.as_completed(futures):
        print(f"Result: {future.result()}")


if __name__=="__main__":
    main()