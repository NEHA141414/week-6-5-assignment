#!/usr/bin/env python
# coding: utf-8

# Q-1 Explain GET and POST methods.

#  Ans-1 GET Methods :
# 
#  The GET method is used to submit the HTML form data . This data is collected by the predefined $_GET variable for processing.
# The information sent from an HTML from using the GET method is visible to everyone in the browser's address bar, which means that all the variable names and thier values will be displayed in the url .Therefore , the get method is not secured to send sensitive information.
# 
# POST Methods :
# 
#      similar to the GET method , the POST mthod is also used to submit the HTML from data .But the data submitted by this method      is collected by the predefined superfined superglobal variable $_POST instead of $_GET.
#      unlike the GET method, it does not have a limit on the amount of information to be sent . The information sent from an HTML 
#      from using the  POST method is not visible to anyone.

# Q-2 Why is request used in flask ?

# Ans-2 In a flask APP ,we have our own Webpage (client) and a server. The server should process the data. The Request , in flask , is an object that contains all the data sent from the client to server. This data can be recovered using the GET/POST Methods. 

# Q-3 Why is redirect() used in flask ?

# Ans-3 A redirect is used in the flask class to send the user to a particular URL with the status code . conversely ,this status code additionally identifies the issues . When we access a website ,our browser sends a request to the server  and the server replies with what is known as the HTTP status code ,which is a three-digit number.

# Q-4 What are templates in flask ? why is the render_template() function used ?
# 

# Ans-4 Templates are files that contain static data as well as placeholders for dynamic data . A template is rendered with specific data to produce a final document . Flask uses the jinja template library to render templates. In your application , you will use templates to render HTML which will display in the use's browser.
# 
# In flask , the redirect() function is used to perform URL redirection , which means sending a client to a different URL than the one originally reguested.
# 1. After forms submission : when a user submits a form (e.g ,login form , registration form),
# you may want to process the form data and then redirect the user to a different page, such as a dashboard or a success page.
# this prevents the user form resubmitting the form accidentally by refreshing the page.
# 
# 2. changing URLs : If your application's url structure changes, or you want to create more-friendly urls,
# you can use redirect() to send users form the old urls to the new ones transparently.
