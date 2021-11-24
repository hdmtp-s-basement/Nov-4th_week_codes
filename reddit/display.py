from reddit_dose import *


def choose():
    choice = int(input("0 -> sub_comment_stream | 1 -> sub_submissions | 2 -> sub_submission_stream | 3 -> redditor_stream_comnts | 4 -> redditor_stream_submissions: "))
    if(choice == 0):
        sub_comment_stream(subreddit)
    elif(choice == 1):
        sub_submissions(subreddit)
    elif(choice == 2):
        sub_submission_stream(subreddit)
    elif(choice == 3):
        redditor_stream_comnts()
    elif(choice == 4):
        redditor_stream_submissions()

choose()