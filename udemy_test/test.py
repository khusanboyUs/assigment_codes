"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
questions=open("tests.txt","r")
question=[i.strip() for i in questions.readlines()]
questions.close()

print(question)
result=[]

for n in question:
    print(f"{n.split('=')[0]}= ?")
    user_input=input('What is your response? ')
    if user_input == n.split("=")[1]:
        print('Correct')
        result.append(1)
    else:
        print('incorrect')

r=open('result.txt','w')
re=r.write(f"Your final score is {len(result)}{'/'}4")
r.close()

