## script to generate fake information
import random, os
from faker import Faker
from datetime import datetime

SITES = ['Portmore', 'Trinidad', 'Jamaica']
LOCATION = ['Cabinet 1', 'Cabinet 2', 'Cabinet 3', 'Tape Library']
COMPARTMENT = ['Drawer 1', 'Drawer 2', 'Drawer 3', 'Module 1', 'Module 2']

def create_db_queries_file(data):
    INSERT_SMT = 'INSERT INTO media(media_id, created_date, modified_date, site, location, compartment) VALUES("%s", "%s", "%s", "%s", "%s", "%s");\r'
    try:
        with open('./query.sql', 'w') as ptr:
            newline = '\r'

            ptr.write("USE tape_manager;\r")

            ptr.write(newline)

            ptr.write("/*======================================INSERTING DATA INTO TABLE======================================*/\r")
            
            for item in data:
                currentDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ptr.write(INSERT_SMT % (item['id'], currentDate, currentDate, item['site'], item['location'], item['compartment']))
    except:
        pass

def pick_random_compartment(location):
    if location == LOCATION[-1].upper():
        return random.choice(COMPARTMENT[4:]).upper()
    return random.choice(COMPARTMENT[0:4]).upper()

def pick_random_location():
    return random.choice(LOCATION).upper()

def pick_random_site():
    return random.choice(SITES).upper()

def main():
    fake_generator = Faker()
    media = []

    for i in range(random.randint(0, 100)):
        item = {}
        item['id'] = fake_generator.bothify(text='???###L6').upper()
        item['site'] = pick_random_site()
        item['location'] = pick_random_location()
        item['compartment'] = pick_random_compartment(item['location'])
        media.append(item)
    
    create_db_queries_file(media)



if __name__ == '__main__':
    main()
