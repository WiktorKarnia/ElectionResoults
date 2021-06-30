import pandas
import time
wikipedia = pandas.read_html('https://en.wikipedia.org/wiki/2020_United_States_presidential_election')
election = wikipedia[2]

candidate_1 = election[1]
name_1 = candidate_1[1]
votes_1 = candidate_1[5]
popular_1 = candidate_1[7]

candidate_2 = election[2]
name_2 = candidate_2[1]
votes_2 = candidate_2[5]
popular_2 = candidate_2[7]

print(name_1 + ' ' + votes_1 + ' votes' + '        ' + name_2 + ' ' + votes_2 + ' votes')

if(votes_1 > votes_2):
    print("The next US president is: " + name_1)
else:
    print("The next US president is: " + name_2)

time.sleep(30)