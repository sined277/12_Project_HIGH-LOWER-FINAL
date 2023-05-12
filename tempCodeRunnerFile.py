import random
from game_data import data
from replit import clear

def person_vs_person():
  person = data[random.randint(0, len(data))]
  return person



def more_followers(first_person, second_person, count_now):
  who = input("Who has more followers? Type 'A' or 'B': ").upper()

  if first_person['follower_count'] > second_person['follower_count'] and who == 'A':
      count_now = count_now + 1
      print(f"You're right! Current score: {count_now}")
  
  elif first_person['follower_count'] < second_person['follower_count'] and who == 'B':
      count_now = count_now + 1
      print(f"You're right! Current score: {count_now}")
  
  else:
    end_game = True
    print(f"Sorry, that's wrong. Final score: {count_now}")
    count_now = -1
    return count_now

  # Очистка поля ввода
  clear()
  
  return count_now

  





def game():
  end_game = False
  count = 0
  while count != -1:
    #logo main
    first = person_vs_person()
    second = person_vs_person()

    print(f"first {first['follower_count']}, second {second['follower_count']}")
    print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}.")

    #logo vs

    print(f"Compare B: {second['name']}, a {second['description']}, from {second['country']}.")
    count = more_followers(first_person=first, second_person=second, count_now=count)
    if count > 0:
      print(f"You're right! Current score: {count}")

game()



