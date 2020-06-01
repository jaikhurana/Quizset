import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford','Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe','New York': 'Albany','North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia','West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for filecount in range(35):
       quizfile=open('quiz'+str(filecount+1)+'.txt','w')
       answerfile=open('ans'+str(filecount+1)+'.txt','w')
       quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
       
       states=list(capitals.keys())
       random.shuffle(states)
   
       for quesnum in range(50):
            correctans=(capitals[states[quesnum]])
            wrongans=list(capitals.values())
            del wrongans[wrongans.index(correctans)]
            wrongans=random.sample(wrongans,3)
            options=wrongans+[correctans]
            random.shuffle(options)
            quizfile.write(f'{quesnum + 1}. What is the capital of {states[quesnum]}?\n')
            for i in range(4):
                quizfile.write(f"  {'ABCD'[i]}.{options[i]}\n")
            
            quizfile.write('\n')
            
            answerfile.write(f"{quesnum + 1}.{'ABCD'[options.index(correctans)]}")
            answerfile.write('\n');

answerfile.close()
quizfile.close()

            

