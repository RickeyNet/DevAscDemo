class Person:
    def __init__(self, first_name: str, last_name: str, age: int, gender: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.race = race
        self.standing = False
        

    def standing(self) -> None:
        if self.standing:
            print(f"{self.first_name} {self.last_name} is already standing.")
            return
        else:
            self.standing = True
            print(f"{self.first_name} {self.last_name} has stood up.")

    def sitting(self) -> None:
        if not self.standing:
            print(f"{self.first_name} {self.last_name} is already sitting.")
            return
        else:
            self.standing = False
            print(f"{self.first_name} {self.last_name} has sat down.")

   
    
    
