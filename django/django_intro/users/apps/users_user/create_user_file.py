# Create three users
User.objects.create(first_name="peter",last_name="coding",email_address="pcoing@email.com",age=36)
User.objects.create(first_name="mike",last_name="dojo",email_address="mdojo@email.com",age=35)
User.objects.create(first_name="nike",last_name="coder",email_address="ncoder@email.com",age=27)

# Retrieve all the users
all_users = User.objects.all()
print(all_users)

# Retrieve the last user
last_user = User.objects.last()
print(last_user)

# Retrieve the first user
first_user = User.objects.first()
print(first_user)

# Change the user with id=3 so their last name is Pancakes
user_3 = User.objects.get(id=3)
print(user_3)
user_3.last_name = "pancakes"
user_3.save()
user_3 = User.objects.get(id=3)
print(user_3)

# Delete the user with id=2 from the database
all_users = User.objects.all()
print(all_users)
user_2 = User.objects.get(id=2)
user_2.delete()
all_users = User.objects.all()
print(all_users)

# Get all the users, sorted by their first name
ascending_user_list = User.objects.all().order_by("first_name")
print(ascending_user_list)

# Get all the users, sorted by their first name in descending order
descending_user_list = User.objects.all().order_by("-first_name")
print(descending_user_list)





