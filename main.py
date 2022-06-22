import praw
import time
import csv
import json
import random
from keep_alive import keep_alive

# praw instance
reddit = praw.Reddit(client_id="yz9gB5sz6WsbERC4_qHaKg",
                    client_secret="Up3QyiT1Igz_nOsacUC2i7Cbww5jcw",
                    user_agent="<console:TESTACCOUNT:1.0>",
                    username= 'Test-Account-Bot',
                    password='PurelyForFun'
)

# reads csv file
quotes = []
with open('file.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for line in reader:
        quotes.append(line)

# reads json file
jokes = {} # index -> tuple(question, answer)
with open('jokes.json') as f:
    data = json.load(f)
    for index, value in enumerate(data):
        jokes[index] = (value["question"], value["answer"])

# submits a post to a subreddit
def subredditPost(day_of_year):
    random_row = random.randint(1,45575)
    dailyQuote = quotes[random_row][0]

    replyQuote = "I hope you have a great day, Aamir!" + "\n\n" + "Here's a quote to start your day:" + "\n\n" + ">" "\"" + dailyQuote + "\""
  
    postTitle = "Day " + str(day_of_year) + ": Good Morning, Aamir!"
  
    # submit post
    reddit.validate_on_submit=True
    reddit.subreddit("HelloUser").submit(postTitle, selftext=replyQuote)
    print("Your program has posted for today: Day " + str(day_of_year))

# replies to a comment by delivering a joke
replied_comments = []
def reply_to_comment():
    jokeIndex = random.randint(0, len(jokes) - 1)
    jokeQuestion = jokes[jokeIndex][0]
    jokeAnswer = jokes[jokeIndex][1]

    joke = jokeQuestion + "\n" + jokeAnswer

    # finds a comment with "joke" in it and replies
    for comment in reddit.subreddit("HelloUser").comments(limit=None):
        if "joke" in comment.body and comment.id not in replied_comments:
            comment.reply("Here's a joke:\n\n" + joke)
            replied_comments.append(comment.id)
            print("You've replied to a comment!")

# votes on 5 trending posts
def vote_content():
    subreddit = reddit.subreddit("funny")
    hot_funny = subreddit.hot(limit=5)

    for submission in hot_funny:
        print(submission.title)
        if submission.num_comments > 100:
            submission.upvote()
            print("You have upvoted a post!")
        else:
            submission.downvote()
            print("You have downvoted a post :(")

# befriends a user
def friendRequest(name):
    if reddit.redditor(name).is_friend:
        print("You are already friends with " + name + ".")
    else:
        reddit.redditor(name).friend()
        print("You have friended " + name + ".")

# block unverified users
def blockUser(name):
    if not reddit.redditor(name).has_verified_email:
        reddit.redditor(name).block()
        print("You have blocked " + name + ".")
    else:
        print("The user " + name + " is verified")

# calling functions once a day

day_of_year = time.gmtime()[7]
currentTime = time.gmtime()

keep_alive()
while(day_of_year < 366):
    if currentTime[3] == 12:
        subredditPost(day_of_year)
        reply_to_comment()
        vote_content()
        print("Bot paused until tomorrow.")
        time.sleep(86400)
    # update variables
    day_of_year = time.gmtime()[7]
    currentTime = time.gmtime()