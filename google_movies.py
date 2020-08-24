# Tutorial inspo: https://www.youtube.com/watch?v=OISEEL5eBqg (should be 2nd vid in series, wrong link)

# technically should work with other search results that have an app bar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# path may differ
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

movie_titles_list = []

driver.get("https://google.com")
print(f"Website name: {driver.title}")

# access search bar, clears it first, then searches movies and clicks enter
# can 1 line this by doing: search.send_keys("one liner", Keys.RETURN)
search = driver.find_element_by_name("q")
search.clear()
search.send_keys("movies")
search.send_keys(Keys.RETURN)

# ensure that this html code actually exists
try:
    # gets the app bar that holds the search results
    movie_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "extabar"))
    )

    # wrapper div that holds the a tag; a tags hold the individual movie titles
    movies_wrapper = movie_list.find_element_by_class_name("EDblX")
    movies = movies_wrapper.find_elements_by_class_name("MiPcId")

    for movie in movies:
        # returns the div text for the title
        movie_title = movie.find_element_by_class_name("kltat")
        movie_titles_list.append(movie_title.text)

finally:
    # close browser
    driver.quit()
    
    # iterates over all titles while nubmering them
    for title in movie_titles_list:
        current_index = movie_titles_list.index(title) + 1
        print(f'{current_index}. {title}')
