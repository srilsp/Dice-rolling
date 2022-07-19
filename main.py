import random
def main():
  num_times = int(input("How many times do you want to roll the dice? "))
  print(f"Rolling the dice {num_times} times...the values are:")
  roll_dice(num_times)
  roll_again = input("Do you want to roll the dice again? (y/n)")
  if roll_again != 'y':
    exit
  else:
    main()
    
def roll_dice(num_times):
  rolls = 0
  for i in range(num_times):
    rolls += 1
    random_number = random.randint(1, 6)
    print(f'Roll {rolls}: {random_number}')

main()