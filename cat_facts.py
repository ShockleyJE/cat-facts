
import smtplib
import random
from time import sleep

path = 'cf.txt'

in_file = open(path,'r')
facts = []
for line in in_file:
    if 158 > len(line[:-1]) > 5:
        facts.append(line[:-1])





send_to = [person1,person2,...]

server = smtplib.SMTP( 'smtp server', port )
server.starttls()
print 'connected'
server.login( 'username',password )
first = 'Thank you for signing up for Cat Facts! you will recieve fun facts about cats! MEOW >^< Text MEOW to stop.'

try:
    for person in send_to:
        server.sendmail('showmethecatfax@yahoo.com',person,first)
        print 'sent: {} to {}'.format(first,person)
        sleep(10)
        count = 0
        rangecount = 80
    for i in range(rangecount):
        ranger = rangecount
        if count == len(list):
            count = 0
        send = facts[random.randint(0,len(facts) -1 )]
        server.sendmail('showmethecatfax@yahoo.com', list[count], send)
        print 'message\n {}'.format(send)
        print 'to\n {}'.format(list[count])
        print
        sleep(5)
        count +=1
        rangecount -=1
        print str(rangecount) +  ' message left to send'
finally:
    server.quit()


