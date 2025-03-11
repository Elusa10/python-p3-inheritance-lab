#!/usr/bin/env python

from user import User

class Student(User):  # ✅ Inherits from User
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [] 

    def learn(self, str):
        self.knowledge.append(str)
        str='new_knowledge'
        # self.knowledge.append(new_knowledge)

    