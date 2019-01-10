# Intro
This is a CLI application. To run it, you'll need Python 3.6 (should also work with 3.X but I don't guarantee it).  
To invoke the application:   
```python dispencer_cli.py <number>```   
`number` is the amount you'd like to be dispensed in 100, 50, 20, and 10 notes.   

## Warning
Don't try this app with numbers larger than 8 or 9 digits. See `solution-discussion.pdf`.   

# Running Tests
You'd need `pytest` to run the tests. If you're using `pipenv` then just do `pipenv install` in project directory and then run `pytest` in the activated virtualenv (`pipenv shell`).

