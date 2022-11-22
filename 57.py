#create a dictionary which converts english words to hindi
mydict = {
    "fan":"pankha",
    "box":"dabba",
    "kite":"patang",
    "breakfast":"nashta"
}
print("the options are:",mydict.keys())
a = input("enter the english word\n")
print("the meaning of the word in hindi is :",mydict[a])