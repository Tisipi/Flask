# Flask Web Development

I used this repository while reading the book *Flask Web Development*, 2nd Edition, by *Miguel Grinberg*. Published by O'Reilly Media, Inc., 2018.

Book is accompanied by github repository https://github.com/miguelgrinberg/flasky.git.


# Installation

Install Flask package:  
> pip install flask  

Check installed packages:  
```
pip list  
pip freeze
```


# Flask Development Web Server

Run Flask Web Server:
```
export | grep FLASK  
export FLASK_APP=hello.py  

flask run  
```

Web server is running on http://127.0.0.1:5000


Enable debugging:  
> export FLASK_DEBUG=1  

Help info:  
> flask --help  
> flask run --help  


Show the routes for the Flask app:  
> flask routes

