# spam comment
text = input("enter the text\n")
if("make money online" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
    
elif("subscribe now" in text):
    spam = True
    
if(spam):
    print("this text is spam")
else:
    print("not spamming text")
