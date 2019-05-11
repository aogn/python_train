from models.group import Group
import random

def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.creation(Group(name="test"))
    old_groups = db.get_group_list()
    group_to_change = random.choice(old_groups)
    group = Group(name="New group")
    id = group_to_change.id
    app.group.modify_group_by_id(group, id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[id] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_modify_group_header(app):
#    if app.group.count() == 0:
#    app.group.creation(Group(header="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New group"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)