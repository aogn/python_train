# -*- coding: utf-8 -*-
from models.group import Group

def test_add_group(app):
    app.group.creation(Group(name="test", header="test", footer="test"))

def test_add_empty_group(app):
    app.group.creation(Group(name="", header="", footer=""))
