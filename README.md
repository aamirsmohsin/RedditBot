# RedditBot

### Project

RedditBot uses the Python Reddit API Wrapper (PRAW) to interact with Reddit's API. It accesses CSV and JSON files to generate content for post and comment submissions each day.

### Hosting

keep_alive.py creates a web application using Flask, which is visited every five minutes by [UptimeRobot](https://uptimerobot.com/) to keep the web application online and the bot running.
