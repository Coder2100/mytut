def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind,"?")
    print("-- I'm sorry, we're all out", kind)
    for arg in arguments:
        print(arg)
        #creating a crossing line
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
#calling the function

cheeseshop("Limbuger", "Its very nice sir",
"It's really very, VERY runny, sir",
shopkeeper="mAKR lIMBAD", 
client="Jonh Reece",
sketch = "Bed room kitchen")

#4.7.6. Documentation Strings
def my_function():
    """Do nothing but document it
    
    No, really, it does not do anything.
    """
    pass
print(my_function.__doc__)