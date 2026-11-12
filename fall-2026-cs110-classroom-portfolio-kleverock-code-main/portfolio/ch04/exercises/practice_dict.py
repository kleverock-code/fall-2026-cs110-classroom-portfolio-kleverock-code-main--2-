my_capitals = {"USA":"Washington, D.C.", "France":"Paris", "Japan":"Tokyo"}
for i in my_capitals:
    print(i)
for country, cap in my_capitals.items():
    print(country, cap)
print(my_capitals.get("USA"))

    