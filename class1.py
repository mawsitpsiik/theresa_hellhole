'''
Python Dictionaries - my_cat 
Dictionaries are Key:Value pairs of objects in 
a list like structure.

Challenge #1
Run the code, fix any errors, add more cat 
characteristics to the my_cat dictionary
      
- First, fix the error - There is a string 
  concatenation error.  When you use the:
  print('some text' + 'some more text') 
  you need to make sure you are concatenatng 
  "strings"... If not, convert them to strings.
- What are you concatenating with the following:
  print('My cat is ' + my_cat['age'] + ' years old')
  HINT: the value of my_cat['age'] is an integer, 
  not a string. How do you fix that?
- Change some characteristics (values) of your cat 
  in the my_cat dictionary
- Add some additional characteristics to your cat 
  to the my_cat dictionary
'''
my_cat = {'size':'huge', 'color':'tabby', 'disposition':'quiet', 'favfood':'artichoke', 'age':7}
print(my_cat)
print('My cat is ' + my_cat['size'] + ' sized')
print('My cat has ' + my_cat['color'] + ' fur')
print('My cat is very ' + my_cat['disposition'])
print('My cat is ' + str(my_cat['age']) + ' years old')
print("my cat's favorite food is " + my_cat['favfood'])