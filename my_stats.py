from github_contributions import GithubUser
import datetime
import pytz 
   
tz_NY = pytz.timezone('Asia/Kolkata')

user = GithubUser('hdmtp')
contribs = user.contributions()

contribs_2021 = user.contributions(start_date='2021-11-22', end_date=str(datetime.now(tz_NY)))
#print(sum([day.count for day in contribs_2021.days]))


sc = "\n"+f"**{datetime.datetime.now()}** | **{sum([day.count for day in contribs_2021.days])}**"

f = open("README.md", "a")
f.write(sc)
f.close()

