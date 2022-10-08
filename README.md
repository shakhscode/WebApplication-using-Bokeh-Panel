# Python Web App Prototype
**Is it possible to design a fully operational web application using Python ? The answer is yes. But is it possible to build a web application in python without using web development framework like Flask and Django. The answer is still yes. We can create web applications without using any web framework just using Bokeh and Panel which require only few lines of python codes.**

I have created the prototype of a web application using python libraries- bokeh and panel and pushed the files into this repository.

## The product
Video

## Used tools
#### Python, Matplotlib, Bokeh, Panel.

## Description 
- Basically I created 5 files for 5 different pages in the application.

- The file [startApp.py](startApp.py) starts the application on the local host.
- Inside the first file I created a function that opens another specified file and executes it
```
def visit():
        with open(other_file_location) as infile:
            exec(infile.read())  #execute the opened file.
```
Then created a Bokeh button which when clicked will exceute the defined function visit()
```
b1 = Button(label= 'REGISTER', button_type = 'primary')
b1.on_click(visit)
```
- Using this technique one page is connected to another.
- Each page is desinged using panel dashboard functions and tools.

#### Note:
- This is just a protoytpe of a web application.
- The pages and the dashboards are not designed well. This was my first web application using python libraries. So I was more focused on functions and methods to know how it works rather than how to design a beautiful dashboard or web pages.

***
There is an interesting story behind this project. If you wish you can read it.

## Story behind this project
One day, one of my friend came to me for some help regarding python. He is a Biomedical student and needed some help in python to complete his project. He came to me and asked -

My friend: Bro! do you know python ?

Me: Yes.

My friend: I need pyhton for my project, can you help me ?

Me: Yah, ofcourse. ( I thought he have written some python code and its not running and I can fix it easily)

Me again: When do you need to submit the project ? 

My friend: Next week. 

Me: Okay, so come to me next week.

He was so confident that I can do it and he did not ask anyone else. Then, two days before the project submission deadline he came to me -

My friend: Bro, here is the block diagram of the project. Everything is done just you need to design the website. 

Me: Wait, what ..website ? what kind of website?

My friend: My project is about to connect biomedical devices like oxieter, spirometer from mobile or computer via bluetooth using a web application. The application should coonect to the oximeter, take input from the oximeter, analyze the input data by a machine learning model and visualize the final results in a specific manner. 

Me: Okay, so what I need to do ?

My friend: Everyhting is done, just need to design a website for the application. 

Me: Bro, are you serious ?...desinging a website just in one day.....I am not a web developer.

My friend: But you know python, so you can.

(He is a biomedical student and dont have any idea about web developement. He thought anyone who knows python can develop a website.)

Me: Bro, web development is a different field. I know python, but I use python for data analytics. Data analytics and web developement are different. I don't know how to design a website. Sorry bro! You can ask someone else.

My friend: But, I was expecting that you can do it and thats why I did not approach anyone else. Now tomorrow is the final submission date, anyhow you have to do it, otherwise I will fail the assessment.

Me: ....lets see. What I can do!

He put me under pressure.Since I said 'yes' to him without actually knowing what to do, I was feeling guilty and he did not even have enough time to approach someone else. 

Being into data analytics I knew that it is possible to design interactive dashboard using python libraries like plotly, bokeh, panel etc. Then I started to think, is it possible to design multiple dashboards and link them together? I kept thinking and exploring what can be done using 'Bokeh' and Panel'.
 
After lot of  googling and reading the official documentation of [Bokeh](https://docs.bokeh.org/en/latest/docs/reference.html) and [Panel](https://panel.holoviz.org/) I came up with this prototype.

Finally he submitted the prototype and past his semester. He was happy, but I was much more happier as I learnt something new, explored something new which will also help me in future. 

This project boosted my confidence and interest for web developement using python libraries and frameworks. So I decided to present this in a public repository.