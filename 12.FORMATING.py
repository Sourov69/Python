#letter = ("Hey my name is {} and i am from {}") [have to maintain sqns]
letter = ("Hey my name is {1} and i am from {0}") #[no need to maitnsqnc]
country = "Bangladesh"
name = "Sourov"
print(letter.format(country, name))

print(f"Hey my name is {name} and i am from {country}" )

print(f"we use f-string like this:Hey my name is {{name}}  \
 and i am from{{country}}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.09999 ) )

dam = 49.099999
tzt = f"for only {dam:.2f}"
print(tzt)

print(f"{2 * 30}")