print("TagView Start")
from DataAccess.Views.Models.DB_Engine import session, SafeCommit, New_UUID, Error

from DataAccess.Views.Models.Tag import Tag, \
    tag_id_requestKey, \
    tag_title_requestKey, \
    tag_memories_requestKey

class tag_access_template:
    id = None
    title = None

    def __init__(self, template_dict):
        self.id = template_dict[tag_id_requestKey] if tag_id_requestKey in template_dict else None
        self.title = template_dict[tag_title_requestKey] if tag_title_requestKey in template_dict else None

def CreateTag(template):
    template.title = template.title.strip()
    old_tag = session.query(Tag).filter(Tag.title==template.title).first()
    if old_tag is not None:
        return old_tag
    new_tag = Tag(id=New_UUID(), title=template.title)
    session.add(new_tag)
    return SafeCommit(new_tag)

def GetTag_CreateTag(template):
    if template.id is None:
        return CreateTag(template)
    else:
        return GetTag(template)

def GetAllTags():
    return session.query(Tag).all()

def GetTag(template):
    tag = session.query(Tag).filter(Tag.id==template.id).first()
    if tag is None:
        return Error("Tag not found! ID: " + template.id)
    return tag

print("TagView End")
