#Author Name: Aiden Bernstein
#Date: 11/6/2022
#Program Name: Bernstein_Airport_code.py
#Purpose: Display the airport name, city and state based on the airport code that a user inputs

def main():
    name = {'ATL': 'Hartsfield–Jackson Atlanta International Airport',
            'DEN': 'Denver International Airport',
            'ORD': 'O\'Hare International Airport',
            'LAX': 'Los Angeles International Airport',
            'MCO': 'Orlando International Airport'}

    city = {'ATL': 'Atlanta',
            'DEN': 'Denver',
            'ORD': 'Chicago',
            'LAX': 'Los Angeles',
            'MCO': 'Orlando'}

    state = {'ATL': 'Georgia',
            'DEN': 'Denver',
            'ORD': 'Illinois',
            'LAX': 'California',
            'MCO': 'Florida'}

    search = input("Please enter airport code to lookup: ").upper()
    search_name = name.get(search)
    search_city = city.get(search)
    search_state = state.get(search)

    if search_name:
        print(f'{search}\'s name is {search_name}')

    if search_city:
        print(f'{search} is in the city of {search_city}')

    if search_state:
        print(f'{search} is in the state of {search_state}')

    if not search_name and not search_city and not search_state:
        print(f'{search} is not in the database')

main()