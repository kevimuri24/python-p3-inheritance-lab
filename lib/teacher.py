#!/usr/bin/env python

from user import User
import random

class Teacher(User):
    knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = Teacher.knowledge  # Using the class-level knowledge

    def teach(self):
        """Randomly select a piece of knowledge to teach."""
        return random.choice(self.knowledge)  # Randomly return a piece of knowledge

    def add_knowledge(self, new_knowledge):
        """Add a new piece of knowledge to the teacher's knowledge list."""
        if isinstance(new_knowledge, str):
            self.knowledge.append(new_knowledge)  # Append new knowledge to the list
        else:
            raise ValueError("Knowledge must be a string.")
