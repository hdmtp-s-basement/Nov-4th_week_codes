from github_contributions import GithubUser
import datetime

user = GithubUser('hdmtp')
contribs = user.contributions()

contribs_2021 = user.contributions(start_date='2021-11-22', end_date=str(datetime.datetime.now()))
#print(sum([day.count for day in contribs_2021.days]))


sc = "\n"+f"**{datetime.date.today()}** | **{sum([day.count for day in contribs_2021.days])}**"

f = open("README.md", "a")
f.write(sc)
f.close()

