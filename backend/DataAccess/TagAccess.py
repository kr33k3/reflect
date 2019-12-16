import DataAccess.Views.TagView as tag_view

def GetAllTags():
    tags = tag_view.GetAllTags()
    tags_toReturn = []
    for tag in tags:
        tags_toReturn.append(tag.to_dict())
    return tags_toReturn
