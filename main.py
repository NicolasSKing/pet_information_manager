from pet_class import Pet

my_pet = Pet()

name = input("Enter your pet's name: ")
animal_type = input("Enter your pet's type: ")
age = int(input("Enter your pet's age: "))

my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)

print("\nPet Information")
print(f"Name: {my_pet.get_name()}")
print(f"Type: {my_pet.get_animal_type()}")
print(f"Age: {my_pet.get_age()}")