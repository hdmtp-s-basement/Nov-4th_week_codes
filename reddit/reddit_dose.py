import praw
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def authenticate():
    reddit = praw.Reddit(
        client_id=os.environ.get("id"),
        client_secret=os.environ.get("secret"),
        user_agent='random bullshit go brrr..',
    )
    return reddit

reddit = authenticate()

if reddit.read_only:
	print("\tAll set, ready to explore Reddit!\t")

def sub_comment_stream():
    sub = str(input("Enter subreddit name: "))
    subreddit = reddit.subreddit(sub)
    for comment in subreddit.stream.comments(skip_existing=True, pause_after=5):
        print("\n")
        print(comment.body)
        print("=====")
        print(comment.author)
        print("\n\t---------------------\n\t")

def sub_submission_stream():
    sub = str(input("Enter subreddit name: "))
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.stream.submissions(skip_existing=True, pause_after=5):
        print("\n")
        print(submission.body)
        print("=====")
        print(submission.author)
        print("\n\t---------------------\n\t")


def sub_submissions():
    sub = str(input("Enter subreddit name: "))
    subreddit = reddit.subreddit(sub)
    limit = int(input("Limit: "))
    for submission in subreddit.hot(limit=limit):
        print("\n")
        print(submission.title)
        print("=====")
        print(submission.author)
        print("\n\t---------------------\n\t")

def redditor_stream_comnts():
    user = str(input("reddit username: "))
    for comment in reddit.redditor(user).stream.comments():
        print("\n")
        print(comment.body)
        print("\n")

def redditor_stream_submissions():
    user = str(input("reddit username: "))
    for submission in reddit.redditor(user).stream.submissions():
        print("\n")
        print(submission.title)
        print("\n")