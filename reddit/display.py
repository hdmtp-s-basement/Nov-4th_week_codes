from reddit_dose import *


def choose():
    choice = int(input("0 -> sub_comment_stream | 1 -> sub_submissions_hot | 2 -> sub_submission_stream | 3 -> redditor_stream_comnts | 4 -> redditor_stream_submissions: "))
    if(choice == 0):
        sub_comment_stream()
    elif(choice == 1):
        sub_submissions_hot()
    elif(choice == 2):
        sub_submission_stream()
    elif(choice == 3):
        redditor_stream_comnts()
    elif(choice == 4):
        redditor_stream_submissions()

choose()