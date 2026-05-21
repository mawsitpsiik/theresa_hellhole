import LCD1602 as L6
import random

L6.init(0x27, 1)

answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "Outlook good", "Ask again later", "Cannot predict now", "Reply hazy, retry", "Don't count on it", "My sources say no", "Outlook not so good"]


which_one = random.randint(0,11)
gar =str(answers[which_one])

L6.write(0,0,gar)


