


from sprite import Sprite


class Friendbook:
    # This is the class that will hold the graph of all the people in the friendbook
    # It will also hold the list of all the people in the friendbook

    def __init__(self):
        self.people = []
        self.graph = {}

    def add_person(self, person):
        self.people.append(person)
        self.graph[person] = person.friends

    def add_friendship(self, person1, person2):
        self.graph[person1].append(person2)
        self.graph[person2].append(person1)

    def get_friends(self, person):
        return self.graph[person]

    def get_friends_of_friends(self, person):
        friends = self.get_friends(person)
        friends_of_friends = []
        for friend in friends:
            friends_of_friends.extend(self.get_friends(friend))
        return friends_of_friends

    def data_for_new_profile(self):
        ## this could be done on website
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        person = Person(name, age)
        person.get_personality_traits()
        friend_names = input("Enter the names of your friends, separated by commas: ")
        friend_names = friend_names.split(", ")

        if (input("Would you like to make a new profile? (y/n): ")) == "y":
            self.make_new_profile(person)
            self.add_friends(person, friend_names)

    def make_new_profile(self, person):
        self.add_person(person)
        person.update_profile()

    def add_friends(self, person, friend_names):
        for friend_name in friend_names:
            for friend in self.people:
                if friend.name == friend_name:
                    self.add_friendship(person, friend)
        



class Person:
    # This is the class that will hold the information about each person in the friendbook
    # It will hold the name, age, and friends of each person

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def get_personality_traits(self):
        self.personality_traits = []
        self.personality_traits.append(input("Enter your favorite color: "))
        self.personality_traits.append(input("Enter your favorite food: "))
        # self.personality_traits.append(input("Enter your favorite animal: "))
        # self.personality_traits.append(input("Enter your favorite sport: "))
        # self.personality_traits.append(input("Enter your favorite movie: "))
        # self.personality_traits.append(input("Enter your favorite book: "))
        # self.personality_traits.append(input("Enter your favorite song: "))
        # self.personality_traits.append(input("Enter your favorite game: "))
        # self.personality_traits.append(input("Enter your favorite TV show: "))
        # self.personality_traits.append(input("Enter your favorite holiday: "))
        # self.personality_traits.append(input("Enter your favorite season: "))
        # self.personality_traits.append(input("Enter your favorite hobby: "))
        # self.personality_traits.append(input("Enter your favorite sport team: "))
        # self.personality_traits.append(input("Enter your favorite video game: "))
        
    def update_profile(self):
        self.update_profile_repsn()
        self.update_profile_picture()

    def update_profile_repsn(self):
        # This function will return from pfp representation from quantum state based on personality traits and friends
        self.pfp_repsn = []
        pass

    def update_profile_picture(self):
        self.sprite = Sprite(self.pfp_repsn)
        self.pfp = self.sprite.render()

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name


