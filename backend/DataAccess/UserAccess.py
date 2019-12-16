import DataAccess.Views.UserView as user_view
import DataAccess.Views.Models.Memory as memory_model

def CreateUser(request):
    #TODO request field validation
    user_template = user_view.user_access_template(request)
    return user_view.CreateUser(user_template)

def Login(request):
    #TODO request field validation
    user_template = user_view.user_access_template(request)
    return user_view.Login(user_template).to_dict()
