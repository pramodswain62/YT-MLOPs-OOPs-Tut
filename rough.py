# lst = [1,2,3]
# my_str = "ml ops"

# print(type(lst))

from oops_proj import chatbook
user = chatbook()
print(user.id)

chatbook.set_id(5)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)


# print(user.id)
# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)

# print(user._chatbook__name)
# print(user.get_name())
# user.set_name("atc")
# print(user.get_name())