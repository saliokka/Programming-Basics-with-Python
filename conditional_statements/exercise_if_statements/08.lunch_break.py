from math import ceil
movie_name = input()
movie_duration = int(input())
break_duration = int(input())
lunch_break_time = break_duration*0.125
cigarette_break_otdih = break_duration*0.25
remaining_time = abs(break_duration-lunch_break_time-cigarette_break_otdih)

if remaining_time >= movie_duration:
    print(f"You have enough time to watch {movie_name} and left with {ceil(abs(movie_duration-remaining_time))} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(abs(movie_duration-remaining_time))} more minutes.")
