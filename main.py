import praw
import time
from keep_alive import keep_alive
import csv
import random

# insert reddit dev information here
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="<console:TESTACCOUNT:1.0>",
    username= '',
    password=''
)

# posts everyday at 6am cst until the end of the year
def keepGoing():
  countDay = time.gmtime()[7]
  currentTime = time.gmtime()
  newRow = random.randint(1,45575)

  # reads csv file
  with open('file.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    rows = list(reader)
    dailyQuote = rows[newRow][0]

  myUsername = str(reddit.user.me())
  replyQuote = "I hope you have a great day, " + myUsername +"!" + "\n\n" + dailyQuote
  postTitle = "Day " + str(countDay) + ": Good morning!"

  while(countDay < 366):
    if currentTime[3] == 12:
      reddit.validate_on_submit=True
      reddit.subreddit("").submit(postTitle, selftext=replyQuote) # fill in subreddit name
      print("Your program has posted for today: Day " + str(countDay) + ".")
      time.sleep(86400)
    countDay = time.gmtime()[7]
    currentTime = time.gmtime()
    newRow = random.randint(1,45575)

keep_alive()
keepGoing()