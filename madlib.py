# this is a basic madlib problem, you enter the value and they get printed.
# created by hardik thapar
day=input("enter the day: ")
location=input("enter the location: ")
person1=input("enyter the name of the person: ")
weather=input("enter the weather: ")
mood=input("enter how was your mood: ")
person2=input("enter the name of the second person: ")
trip=input("enter where you were going on trip: ")
reason=input("enter the reason your trip got cancelled: ")

madlib=f"""This was last {day}, i was at a  {location} with my {person1}.
the weather was very {weather} and it was sunrise.
I was very {mood} beacause of {person2}. Our trip to {trip} was 
cancelled due to {reason}."""
print(madlib)