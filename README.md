# login2
A second version of my login app. This version uses Django modelforms instead of defining the forms as a class in a separate file. This allows me to practically create different version of a form for specific uses using a model as a base. 

For example, to have a login form that only took an email and password and then a sign up form that took and email, password, name, and phone number I would need to define 2 separate forms on a forms.py file. Now, I don't need a forms.py file and the creation of these 2 separate forms is still necessary but much easier and cleaner to read. 

