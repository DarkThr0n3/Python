#Lovely dictionaries

#create a mapping of state to abbr

states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

cities['NY'] = 'Ney York'
cities['OR'] = 'Portland'

print('-'*10)

print("NY State has:",cities['NY'])
print("OR state has",cities['OR'])

print('-'*10)
print('Michigan abbr is:',states['Michigan'])
print('Florida abbr is', states['Florida'])

print('-'*10)
print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])

print('-'*10,"INTERESTING STUFF,'-'*10")
for state , abbr in list(states.items()):
    print(f"{state} is abbreviated {abbr}")
    print(f"and has city {cities[abbr]}")

print('-'*10)
for abbr,city in list(cities.items()):
    print(f"{abbr} has the city {city}")

print('-'*20)

state = states.get('Texas')

if not state:
    print("Sorry, no texas")

#get a city with a default value
city = cities.get('TX','NONE PRESENT SO THIS')
print(f"The city for the state 'TX' is : {city}")
