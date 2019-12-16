import os
if os.path.exists("Reflect.db"):
	os.remove("Reflect.db")

import DataAccess.UserAccess as user_access
import DataAccess.Views.Models.User as user_model
import DataAccess.MemoryAccess as memory_access
import DataAccess.Views.Models.Memory as memory_model
import DataAccess.TagAccess as tags_access
import DataAccess.Views.Models.Tag as tag_model
import pprint

user_one_dict = {
	user_model.user_username_requestKey:"user_one",
	user_model.user_password_requestKey:"password_one"
}
user_access.CreateUser(user_one_dict)

user_two_dict = {
	user_model.user_username_requestKey:"user_two",
	user_model.user_password_requestKey:"password_two"
}
user_access.CreateUser(user_two_dict)

user_three_dict = {
	user_model.user_username_requestKey:"user_three",
	user_model.user_password_requestKey:"password_three"
}
user_access.CreateUser(user_three_dict)

tag_one_dict = {
	tag_model.tag_title_requestKey:"tag_one"
}
tag_two_dict = {
	tag_model.tag_title_requestKey:"tag_two"
}
tag_three_dict = {
	tag_model.tag_title_requestKey:"tag_three"
}
memory_one_dict = {
	memory_model.memory_title_requestKey:"mem_one",
	memory_model.memory_content_requestKey:"mem_one_content",
	memory_model.memory_user_requestKey:user_one_dict,
	memory_model.memory_tags_requestKey:[
		tag_one_dict,
		tag_two_dict,
		tag_three_dict
	]
}
memory_access.CreateMemory(memory_one_dict)

tags_dicts = tags_access.GetAllTags()
tag_one_dict = tags_dicts[0]
tag_two_dict = tags_dicts[1]
tag_three_dict = tags_dicts[2]

memory_two_dict = {
	memory_model.memory_title_requestKey:"mem_two",
	memory_model.memory_content_requestKey:"mem_two_content",
	memory_model.memory_user_requestKey:user_two_dict,
	memory_model.memory_tags_requestKey:[
		tag_one_dict
	]
}
memory_access.CreateMemory(memory_two_dict)

memory_three_dict = {
	memory_model.memory_title_requestKey:"mem_three",
	memory_model.memory_content_requestKey:"mem_three_content",
	memory_model.memory_user_requestKey:user_three_dict,
	memory_model.memory_tags_requestKey:[
		tag_two_dict,
	]
}
memory_access.CreateMemory(memory_three_dict)

memory_four_dict = {
	memory_model.memory_title_requestKey:"mem_four",
	memory_model.memory_content_requestKey:"mem_four_content",
	memory_model.memory_user_requestKey:user_one_dict,
	memory_model.memory_tags_requestKey:[
		tag_three_dict
	]
}
memory_access.CreateMemory(memory_four_dict)

memory_five_dict = {
	memory_model.memory_title_requestKey:"mem_five",
	memory_model.memory_content_requestKey:"mem_five_content",
	memory_model.memory_user_requestKey:user_two_dict,
	memory_model.memory_tags_requestKey:[
		tag_one_dict,
		tag_two_dict,
	]
}
memory_access.CreateMemory(memory_five_dict)

memory_six_dict = {
	memory_model.memory_title_requestKey:"mem_six",
	memory_model.memory_content_requestKey:"mem_six_content",
	memory_model.memory_user_requestKey:user_three_dict,
	memory_model.memory_tags_requestKey:[
		tag_one_dict,
		tag_three_dict
	]
}
memory_access.CreateMemory(memory_six_dict)

memory_seven_dict = {
	memory_model.memory_title_requestKey:"mem_seven",
	memory_model.memory_content_requestKey:"mem_seven_content",
	memory_model.memory_user_requestKey:user_one_dict,
	memory_model.memory_tags_requestKey:[
		tag_two_dict,
		tag_three_dict
	]
}
memory_access.CreateMemory(memory_seven_dict)

pp = pprint.PrettyPrinter(indent=3)
print("\n/GetAllTags")
print("Response:")
pp.pprint(tags_access.GetAllTags())

print("\n/Login")
print("Request:")
print (user_one_dict)
print("Response:")
pp.pprint(user_access.Login(user_one_dict))
print("\n/Login")
print("Request:")
print (user_two_dict)
print("Response:")
pp.pprint(user_access.Login(user_two_dict))
print("\n/Login")
print("Request:")
print (user_three_dict)
print("Response:")
pp.pprint(user_access.Login(user_three_dict))

print("\n/GetUserMemories")
print("Request:")
print (user_one_dict)
print("Response:")
pp.pprint(memory_access.GetUserMemories(user_one_dict))
print("\n/GetUserMemories")
print("Request:")
print (user_two_dict)
print("Response:")
pp.pprint(memory_access.GetUserMemories(user_two_dict))
print("\n/GetUserMemories")
print("Request:")
print (user_three_dict)
print("Response:")
pp.pprint(memory_access.GetUserMemories(user_three_dict))