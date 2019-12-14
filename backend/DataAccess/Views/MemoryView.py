print("MemoryView Start")
import DataAccess
from DataAccess.Views.Models.DB_Engine import session, SafeCommit, New_UUID, Error, Success

from DataAccess.Views.Models.Memory import Memory, \
    memory_id_requestKey, \
    memory_title_requestKey, \
    memory_content_requestKey, \
    memory_user_id_requestKey, \
    memory_user_requestKey, \
    memory_tags_requestKey

from DataAccess.Views.Models.User import User
from DataAccess.Views.Models.Tag import Tag

import DataAccess.Views.UserView as user_view
import DataAccess.Views.TagView as tag_view

class memory_template:
    id = None
    title = None
    content = None
    #user_id = None
    user = None
    tags = None

    def __init__(self, template_dict):
        self.id = template_dict[memory_id_requestKey] if memory_id_requestKey in template_dict else None
        self.title = template_dict[memory_title_requestKey] if memory_title_requestKey in template_dict else None
        self.content = template_dict[memory_content_requestKey] if memory_content_requestKey in template_dict else None
        #self.user_id = template_dict[memory_user_id_requestKey] if memory_user_id_requestKey in template_dict else None
        self.user = user_view.user_access_template(template_dict[memory_user_requestKey]) if memory_user_requestKey in template_dict else None
        if memory_tags_requestKey in template_dict:
            self.tags = []
            for memory_tag in template_dict[memory_tags_requestKey]:
                self.tags.append(tag_view.tag_access_template(memory_tag)) 


#Create User
#Creates a user
#_username, password - strings
def CreateMemory(template):
    memory_user = user_view.Login(template.user)
    if type(memory_user) is not User:
        return memory_user 
    new_memory = Memory(id = New_UUID(), \
        title = template.title, \
        content = template.content, \
        user = memory_user)
    if template.tags is not None:
        new_memory.tags = []
        for tag_template in template.tags:
            new_memory.tags.append(tag_view.GetTag_CreateTag(tag_template))
    session.add(new_memory)
    return SafeCommit(new_memory)

def GetMemoriesByUser(user_template):
    user = user_view.Login(user_template)
    if type(user) is not User:
        return user
    return user.memories

def GetMemory(template):
    user = user_view.Login(template.user)
    if type(user) is not User:
        return user
    memory = session.query(Memory).filter(Memory.id==template.id).first()
    if memory is None:
        return Error("Memory not found!")
    return memory

def GetMemoriesByTag(tag_template):
    tag = tag_view.GetTag(tag_template)
    if type(tag) is not Tag:
        return tag
    return tag.memories

def GetMemoriesByTags(tag_templates):
    memories = []
    first = True
    #TODO this is messed up - I dont think you can compare objects by reference? or does sqlalchemy not maintain reference between the same rows if gotten from different queries?
    for tag_template in tag_templates:
        tag = tag_view.GetTag(tag_template)
        print(tag.title)
        if type(tag) is not Tag:
            return tag
        tag_memories = tag.memories
        print("tag memories")
        print(tag_memories)
        if first:
            memories = tag_memories
            print("first")
            print(memories)
            first = False
        else:
            print("not first")
            print(memories)
            to_remove = []
            for memory in memories:
                print(memory)
                if memory not in tag_memories:
                    print('remove')
                    to_remove.append(memory)
            for mem_to_remove in to_remove:
                memories.remove(mem_to_remove)
            print(memories)
    return memories

def GetMemoriesBySource(source_uuid):
    #TODO
    return

def UpdateMemory(template):
    memory = GetMemory(template)
    if type(memory) is dict:
        return memory
    if template.title is not None:
        memory.title = template.title
    if template.content is not None:
        memory.content = template.content
    if template.tags is not None:
        memory.tags = []
        for tag_template in template.tags:
            memory.tags.append(tag_view.GetTag_CreateTag(tag_template))
    return SafeCommit(memory)

def DeleteMemory(template):
    memory = GetMemory(template)
    if type(memory) is not Memory:
        return memory
    session.delete(memory)
    return SafeCommit(Success("Memory successfully deleted"))

print("MemoryView End")