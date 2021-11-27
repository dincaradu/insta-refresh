import win32api, win32con, time, sys, random, logging
# from driver.bot import openInstagramStories
from bot import openInstagramStories

# logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

###################################
## Setting runtime variables
###################################
theAccountsFile = 'accounts.txt' # initially non-existent, use the example to create it
numberOfLikes = 20

minutesToViewStories = random.uniform(0.5, 1.5)

###################################
## Execution block
###################################
# Open the file
with open(theAccountsFile, 'r') as fp:
  # Read the lines
  accountsFile = fp.readlines()

  # Split the second row by comma to get the usernames
  usernames = accountsFile[1].split(", ")
  # split the third row by comma to get the passwords
  passwords = accountsFile[2].split(", ")

  # If we have the same amount of username, as we do password, proceed
  if len(usernames) == len(passwords):
    for y in range(260):
      for x in range(len(usernames) - 1):
        openInstagramStories(usernames[x], passwords[x], minutesToViewStories)
        # loveInstagramPosts(usernames[x], passwords[x])

sys.exit()