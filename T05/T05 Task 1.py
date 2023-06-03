#strings.py
"""This task has us use the strip function to make $$$Superman$$$ legible as "Superman" I've actually done this by
reassigning the legible value back into the variable, because we don't need the illegible value.
If we did, I can just store the legible value into a new variable and keep the illegible in its original variable."""

hero = "$$$Superman$$$"
hero = hero.strip("$")
print(hero)