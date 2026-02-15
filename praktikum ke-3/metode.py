class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Halo semuanya, nama aku " + self.name)

p1 = Person("salsa")
p1.greet()

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

class Person:
  def __init__(self, name, age, bulan):
    self.name = name
    self.age = age
    self.bulan = bulan

  def get_info(self):
    return f"{self.name} berusia {self.age} tahun dan lahir bulan {self.bulan} "

p1 = Person("Meiling", 15, "november")
print(p1.get_info())

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

class Kue:
  def __init__(self, name, jenis):
    self.name = name
    self.jenis = jenis

p1 = Kue("kemojo", "basah")

print(p1)

class Kue:
  def __init__(self, name, jenis):
    self.name = name
    self.jenis = jenis

  def __str__(self):
    return f"{self.name} ({self.jenis})"    

p1 = Kue("cookies", "kering")

print(p1)

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("firasat")
my_playlist.add_song("cincin")
my_playlist.show_songs()

