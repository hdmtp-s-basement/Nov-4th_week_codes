from github_contributions import GithubUser
from datetime import datetime    
import pytz    

tz_NY = pytz.timezone('Asia/Kolkata')   
datetime_NY = datetime.now(tz_NY)  

user = GithubUser('hdmtp')
contribs = user.contributions()

contribs_2021 = user.contributions(start_date='2021-11-22', end_date=datetime_NY.strftime("%Y-%m-%d %H:%M:%S.%f"))
#print(sum([day.count for day in contribs_2021.days]))


sc = "\n"+f"**{datetime.datetime.now()}** | **{sum([day.count for day in contribs_2021.days])}**"

f = open("README.md", "a")
f.write(sc)
f.close()

