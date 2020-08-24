from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

movie_titles_list = []

driver.get("https://google.com")
print(f"Website name: {driver.title}")

search = driver.find_element_by_name("q")
search.clear()
search.send_keys("movies")
search.send_keys(Keys.RETURN)

try:
    # ensure that this html code actually exists

    # gets the div that holds the search results
    movie_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "extabar"))
    )

    movies_wrapper = movie_list.find_element_by_class_name("EDblX")
    movies = movies_wrapper.find_elements_by_class_name("MiPcId")

    for movie in movies:
        movie_title = movie.find_element_by_class_name("kltat")
        movie_titles_list.append(movie_title.text)

finally:
    driver.quit()
    for title in movie_titles_list:
        current_index = movie_titles_list.index(title) + 1
        print(f'{current_index}. {title}')
