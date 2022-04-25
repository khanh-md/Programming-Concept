# Driver - Ameena Mohammed - U39296299
# Navigator - Khanh Dong - U14837275
# A program that acts like an 8-ball machine.
# It asks a user for questions and randomly answers.
import random
def main():
    while True:
        ques = str(input('What is your question?'))
        ans = random.randint(0,19)
        response(ans)
        ques2 = input('Would you like to ask another question? ').lower()
        if ques2 == 'no':
            break
    
    
    
    





def response(ans):
    posres = ['It is certain', 'It is decidely so','Without a doubt','Yes-definitely','You may rely on it.'
              ,'As I see it, yes.','Most likely','Outlook good.','Yes',
              'Signs point to yes.',' Reply hazy, try again.','Ask again later.',
              'Better not tell you now.','Cannot predict now.',' Concentrate and ask again.',"Don't count on it.",
              'My reply is no.','My sources say no.','Outlook not so good.','Very doubtful.']

    print(posres[ans])
     
  
  
main()
