class Animal():
    def __init__(self, weight, mood):
      self.weight = weight
      self.mood = mood
    def feed(self, weight, mood):
        pass
    def walk(self, weight, mood):
        pass
    def bath(self, n_bath):
        self.mood = self.mood -2*n_bath
    
class Dogs(Animal):
    def __init__(self, weight, mood):
        super().__init__(weight, mood) 
    def feed(self, n_feed):
        self.weight = self.weight + 0.2*n_feed
        self.mood = self.mood + n_feed
    def walk(self, n_walk):
        self.weight = self.weight - n_walk*0.2
        self.mood = self.mood + 2*n_walk
    def bath(self, n_bath):
        super().bath(n_bath)
    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed)
        self.walk(n_walk)
        self.bath(n_bath)
        print("狗狗現在的體重=", self.weight, "kg, 心情= ", self.mood)
              
class Shiba(Dogs):
  def __init__(self, weight, mood):
    super().__init__(weight, mood) 
  def feed(self, n_feed):
    self.weight = self.weight + 0.3*n_feed
    self.mood = self.mood + n_feed*5
  def printf(self, n_feed, n_walk, n_bath):
      self.feed(n_feed)
      self.walk(n_walk)
      self.bath(n_bath)
      print("柴犬現在的體重=", self.weight, "kg, 心情= ", self.mood)#請接續完成...
  def mood_constraint(self, constraint):
      shiba.printf(0, 0, 0) 
      if (self.mood>=constraint):#請接續完成...):
          print("所以，柴犬現在的心情 ", constraint)
      print("mood最高只能為=" ,constraint )

print("Q1:")
shiba = Shiba(5, 70) 
shiba.printf(20, 10, 3) 

print("Q2:")
shiba.mood_constraint(90)

print("Q3:")
shiba.mood_constraint(300)
