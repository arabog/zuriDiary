class Student:
        # [assignment] Skeleton class. Add your code here
        def __init__(self, name, age, tracks, score):
            pass
            self.name = name;
            self.age = age;
            self.tracks = tracks;
            self.score = score;

            print(self.name, self.age,self.tracks, self.score)

        def change_name(self, value):
            return (f'{value}');

        def change_age(self, value):
            return (f'{value}');

        def add_track(self, value):
            return (f'{value}');

        def get_score(self):
            return (f'{self.score}');

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
name = Bob.change_name("Peter")
age = Bob.change_age(34)
track = Bob.add_track("UI/UX")
score = Bob.get_score()

Bob = Student(name= name, age= age, tracks= [track], score = score)
