def build_person(first_name, last_name):
   person= {"first": first_name,"last": last_name}
   return person
build_person("James", "Nice")
print(build_person("James", "Nice"))

def build_person(first_name, last_name, middle_name=' ', age= None, occupation=' '):
    person= {"first": first_name,"last": last_name, 'middle': middle_name
            }
    if age:
        person['age']=age
    if occupation:
        person['occupation']='Actor'
    return person

print(build_person("James", "Nice", "Famous", 23, "Actor"))rmv