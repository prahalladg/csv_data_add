  



import csv
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

f_name = ['James', 'Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'William', 'Isabella', 'Sophia', 'Oliver', 'Mia', 'Elijah', 'Charlotte', 'Benjamin', 'Amelia', 'Lucas', 'Harper', 'Henry', 'Evelyn', 'Alexander', 'Abigail', 'Samuel', 'Emily', 'Jackson', 'Elizabeth', 'David', 'Sofia', 'Joseph', 'Avery', 'Carter', 'Ella', 'Daniel', 'Scarlett', 'Matthew', 'Grace', 'Aiden', 'Chloe', 'Wyatt', 'Victoria', 'Jayden', 'Madison', 'Jack', 'Zoey', 'Owen', 'Penelope', 'Gabriel', 'Riley', 'Anthony', 'Layla', 'Michael', 'Lillian', 'Ethan', 'Lily', 'Caleb', 'Natalie', 'Mason', 'Hannah', 'Logan', 'Stella', 'Sebastian', 'Aurora', 'Julian', 'Ellie', 'Isaiah', 'Savannah', 'Josiah', 'Addison', 'Levi', 'Brooklyn', 'Aaron', 'Nora', 'Dylan', 'Camila', 'Christopher', 'Paisley', 'Thomas', 'Maya', 'Joshua', 'Leah', 'Andrew', 'Audrey', 'Lincoln', 'Bella', 'Nathan', 'Aria', 'Ryan', 'Skylar', 'Christian', 'Claire', 'Samuel', 'Lucy', 'Jonathan', 'Paisley', 'Hunter', 'Violet', 'Eli', 'Elena', 'Connor', 'Hazel', 'Evan']

l_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins']

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego',
                  'Dallas', 'San Francisco', 'Austin', 'Seattle', 'Denver', 'Charlotte', 'Washington', 'Boston',
                  'Nashville', 'Las Vegas']
    
states = ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'TX', 'CA', 'TX', 'CA', 'TX', 'WA', 'CO', 'NC', 'DC', 'MA', 'TN', 'NV']

def generate_data(count):
    data = []
    
    for _ in range(count):
        first_name = random.choice(f_name)
        last_name = random.choice(l_names)
        email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"

        row = {
            'TITLE': random.choice(['Mr.', 'Ms.', 'Mrs.','Dr']),
            'FIRST_NAME': first_name,
            'MIDDLE_NAME': '',
            'LAST_NAME': last_name,
            'NAME_SUFFIC': '',
            'ADDRESS_1': generate_random_string(10) + ' ' + random.choice(['St.', 'Ave.', 'Blvd.']),
            'ADDRESS_2': generate_random_string(5),
            'ADDRESS_3': '',
            'ADDRESS_4': '',
            'CITY': random.choice(cities),
            'STATE': random.choice(states),
            'ZIP': ''.join(random.choice(string.digits) for _ in range(5)),
            'COUNTRY_ISO3': 'USA',
            'EMAIL': email,
            'PHONE': ''.join(random.choice(string.digits) for _ in range(10)),
        }
        data.append(row)
    
    return data

usa_data = generate_data(10)

# Write data to CSV file
filename = 'sample_data.csv'
with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=usa_data[0].keys())
    writer.writeheader()
    writer.writerows(usa_data)

print(f'CSV file "{filename}" has been generated successfully.')
