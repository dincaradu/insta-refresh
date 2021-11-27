import win32api, win32con, time, sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

###################################
## Setting variables
###################################
usernames = []
passwords = []

with open('accounts.txt', 'r') as fp:
  accountsFile = fp.readlines()

  

  usernames = accountsFile[0].split(', ')
  passwords = accountsFile[1].split(', ')

minutesToViewStories = 5
numberOfLikes = 20

###################################
## Functions 
###################################
def getToInstaAndDenyEverything(username, password):
  driver = webdriver.Chrome("driver\chromedriver.exe")
  driver.get('https://www.instagram.com')

  accept_cookies_button = driver.find_elements_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")[0]
  accept_cookies_button.click()

  time.sleep(3)

  user_input = driver.find_elements_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')[0]
  user_input.send_keys(username)


  pass_input = driver.find_elements_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')[0]
  pass_input.send_keys(password)

  time.sleep(3)

  login_button = driver.find_elements_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")[0]
  login_button.click()

  time.sleep(7)

  dont_save_button = driver.find_elements_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")[0]
  dont_save_button.click()

  time.sleep(5)

  not_now_button = driver.find_elements_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")[0]
  not_now_button.click()

  time.sleep(5)

  return driver

def openInstagramStories(username, password):
  driver = getToInstaAndDenyEverything(username, password)

  open_story_button = driver.find_elements_by_xpath("/html/body/div[1]/section/main/section/div/div[1]/div/div/div/div/ul/li[3]/div/button")[0]
  open_story_button.click()

  time.sleep(minutesToViewStories * 60)

  driver.close()

  time.sleep(5)

def loveInstagramPosts(username, password):
  driver = getToInstaAndDenyEverything(username, password)

  actions = ActionChains(driver)

  for p in range(1, numberOfLikes):
    # postElement = '/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[%d]' % p
    # postEl = driver.find_elements_by_xpath(postElement)
    
    # actions.move_to_element(postEl).click().perform()
    # driver.execute_script("arguments[0].scrollIntoView();", postEl)

    scrollHeight = "window.scrollTo(0, %d);" % (p * 888)
    driver.execute_script(scrollHeight)

    time.sleep(2)

    # likeElement = '//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[%d]/div[3]/section[1]/span[1]/button' % p
    likeElement = '//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[%d]/div[2]/div' % p
    likeButton = driver.find_elements_by_xpath(likeElement)[0]

    # likeButton.click()
    actions.double_click(likeButton).perform()

    time.sleep(3)

  # dont_save_button = driver.find_elements_by_xpath("/html/body/div[1]/section/main/section/div/div[1]/div/div/div/div/ul/li[3]/div/button")[0]
  # dont_save_button.click()

  # time.sleep(minutesToViewStories * 60)

  driver.close()

  time.sleep(5)

# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
# click(960, 540)

###################################
## Execution block
###################################

for y in range(260):
  for x in range(6):
    openInstagramStories(usernames[x], passwords[x])
    # loveInstagramPosts(usernames[x], passwords[x])

sys.exit()