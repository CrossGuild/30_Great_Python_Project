def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}:")
    return user_input

noun1 = get_input("noun")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""
Once upon a time, there was a{noun1} who loved to {verb1} all day.

One day, {noun2} walked into the room and caught the {noun1} in the act.
{noun2} : "What are you doing?"
{noun1} : "I'm just {verb1}ing, what's the big deal?"
{noun2} : "It's not everyday that you see a {noun1} {verb1}ing in the middle of the day."
{noun1} : "That's right. Would you join {verb1}ing?"

And so, {noun2} and {noun1} had great time.
The end.
"""
print(story)