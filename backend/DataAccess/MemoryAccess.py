import DataAccess.Views.MemoryView as memory_view
import DataAccess.Views.UserView as user_view
import DataAccess.Views.Models.Memory as memory_model

def CreateMemory(request):
    #TODO request field validation
    memory_template = memory_view.memory_template(request)
    return memory_view.CreateMemory(memory_template)

def GetUserMemories(request):
    #TODO request field validation
    user_template = user_view.user_access_template(request)
    memories = memory_view.GetMemoriesByUser(user_template)
    memories_toReturn = []
    for memory in memories:
        memories_toReturn.append(memory.to_dict())
    return memories_toReturn