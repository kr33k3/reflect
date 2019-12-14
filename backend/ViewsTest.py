import os
if os.path.exists("Reflect.db"):
	os.remove("Reflect.db")

import DataAccess.Views.UserView as user_view
from DataAccess.Views.Models.User import User, \
	user_username_requestKey, \
	user_password_requestKey

import DataAccess.Views.MemoryView as memory_view
from DataAccess.Views.Models.Memory import Memory, \
    memory_id_requestKey, \
    memory_title_requestKey, \
    memory_content_requestKey, \
    memory_user_id_requestKey, \
    memory_user_requestKey, \
    memory_tags_requestKey


import DataAccess.Views.TagView as tag_view
from DataAccess.Views.Models.Tag import Tag, \
	tag_id_requestKey, \
	tag_title_requestKey, \
	tag_memories_requestKey

print("VIEWS TESTS")

#*****************************************************************
#****************** USER TESTS ***********************************
#*****************************************************************

print("\n\nUSER TESTS")

print("\nSuccessfully Create User Test")
user_one_dict = {
	user_username_requestKey:"user_one", 
	user_password_requestKey:"password_one"}
user_one_template = user_view.user_access_template(user_one_dict)
print(user_one_template.username)
user_one = user_view.CreateUser(user_one_template)
print(type(user_one) is User)

print("\nCreate User Fail Test - Username already taken")
user_two_dict = {
	user_username_requestKey:"user_one", 
	user_password_requestKey:"password_two"}
user_two_template = user_view.user_access_template(user_two_dict)
user_two = user_view.CreateUser(user_two_template)
print(type(user_two) is dict and "Error" in user_two)

print("\nGet user by ID test")
user_one = user_view.GetUser(user_one.id)
print(user_one is not None and type(user_one) is User)

print("\nLogin Test - successful login")
print(user_one_template.password)
validation = user_view.Login(user_one_template)
print(type(validation) is User)

print("\nLogin Test - unsuccessful login")
user_one_template.password = "badpassword"
validation = user_view.Login(user_one_template)
print(type(validation) is dict and "Error" in validation)
user_one_template.password = "password_one"

print("\nUpdate Password Test")
user_one = user_view.UpdatePassword(user_one_template, "new_password")
user_one_dict[user_password_requestKey] = "new_password"
user_one_template = user_view.user_access_template(user_one_dict)
print(type(user_one) is User and type(user_view.Login(user_one_template)) is User)

#*****************************************************************
#****************** MEMORY TESTS *********************************
#*****************************************************************

print("\n\nMEMORY TESTS")

print("\nSuccessfully Create Memory test")
memory_one_dict = {
	memory_title_requestKey:"mem_one",
	memory_content_requestKey:"mem_one_content",
	memory_user_requestKey:user_one_dict
}
memory_one_template = memory_view.memory_template(memory_one_dict)
memory_one = memory_view.CreateMemory(memory_one_template)
print(type(memory_one) is Memory)

print("\nCreate Memory Fail Test - incorrect user")
user_fail_dict = {
	user_username_requestKey:"user_one",
	user_password_requestKey:"badpassword"
}
memory_fail_dict = {
	memory_title_requestKey:"mem_fail",
	memory_content_requestKey:"mem_fail_content",
	memory_user_requestKey:user_fail_dict
}
memory_fail_template = memory_view.memory_template(memory_fail_dict)
memory_fail = memory_view.CreateMemory(memory_fail_template)
print(type(memory_fail) is dict and "Error" in memory_fail)

print("\nGet Memories By User Test")
memory_two_dict = {
	memory_title_requestKey:"mem_two",
	memory_content_requestKey:"mem_two_content",
	memory_user_requestKey:user_one_dict
}
memory_two_template = memory_view.memory_template(memory_two_dict)
memory_two = memory_view.CreateMemory(memory_two_template)
user_one_memories = memory_view.GetMemoriesByUser(user_one_template)
print(len(user_one_memories) is 2)

print("\nDelete Memory Test")
memory_two_template.id = memory_two.id
delete_validation = memory_view.DeleteMemory(memory_two_template)
memory_two = memory_view.GetMemory(memory_two_template)
print(type(memory_two) is not Memory)

print("\nUpdate Memory Tests")
memory_one_update_dict = {
	memory_id_requestKey:memory_one.id, 
	memory_title_requestKey:"updated_title", 
	memory_user_requestKey:user_one_dict
}
memory_one_update_template = memory_view.memory_template(memory_one_update_dict)
memory_one = memory_view.UpdateMemory(memory_one_update_template)
print(type(memory_one) is Memory and memory_one.title==memory_one_update_template.title and memory_one.content==memory_one_template.content)

memory_one_update_dict = {
	memory_id_requestKey:memory_one.id, 
	memory_content_requestKey:"updated_content", 
	memory_user_requestKey:user_one_dict
}
memory_one_update_template = memory_view.memory_template(memory_one_update_dict)
memory_one = memory_view.UpdateMemory(memory_one_update_template)
print(type(memory_one) is Memory and memory_one.title=="updated_title" and memory_one.content==memory_one_update_template.content)

#*****************************************************************
#****************** TAG TESTS ************************************
#*****************************************************************

print("\n\nTAG TESTS")

print("\nSuccessfully Create Tag test")
tag_one_dict = {
	tag_title_requestKey:"tag_test"
}
tag_one_template = tag_view.tag_access_template(tag_one_dict)
tag_one = tag_view.CreateTag(tag_one_template)
print(type(tag_one) is Tag and len(tag_view.GetAllTags()) is 1)


print("\nCreate Tag Fail test: tag already exists")
tag_fail_dict = {
	tag_title_requestKey:" tag_test "
}
tag_fail_template = tag_view.tag_access_template(tag_fail_dict)
tag_fail = tag_view.CreateTag(tag_fail_template)
print(type(tag_fail) is Tag and len(tag_view.GetAllTags()) is 1)

print("\nGet Memories by Tag test")
tag_one_dict[tag_id_requestKey] = tag_one.id
tag_one_template.id = tag_one.id
tag_two_dict = {
	tag_title_requestKey:"tag_two"
}
memory_withtags_one_dict = {
	memory_title_requestKey:"memwt_one",
	memory_content_requestKey:"content",
	memory_user_requestKey:user_one_dict,
	memory_tags_requestKey:[tag_one_dict]
}
memory_withtags_one_template = memory_view.memory_template(memory_withtags_one_dict)
memory_withtags_one = memory_view.CreateMemory(memory_withtags_one_template)
memory_withtags_two_dict = {
	memory_title_requestKey:"memwt_two",
	memory_content_requestKey:"content",
	memory_user_requestKey:user_one_dict,
	memory_tags_requestKey:[tag_one_dict, tag_two_dict]
}
memory_withtags_two_template = memory_view.memory_template(memory_withtags_two_dict)
memory_withtags_two = memory_view.CreateMemory(memory_withtags_two_template)
memory_withtags_three_dict = {
	memory_title_requestKey:"memwt_three",
	memory_content_requestKey:"content",
	memory_user_requestKey:user_one_dict,
	memory_tags_requestKey:[tag_two_dict]
}
memory_withtags_three_template = memory_view.memory_template(memory_withtags_three_dict)
memory_withtags_three = memory_view.CreateMemory(memory_withtags_three_template)
print(len(memory_view.GetMemoriesByTag(tag_one_template)) is 2)


print("\nGet Memories by Tags test")
tag_templates = []
for tag in tag_view.GetAllTags():
	print(tag.id)
	tag_dict = {tag_id_requestKey:tag.id}
	tag_templates.append(tag_view.tag_access_template(tag_dict))
print(len(memory_view.GetMemoriesByTags(tag_templates)) is 1)
