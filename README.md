# Unit Testing Tutorial
### Run Flask
```
python3 app.py
```

### Running Tests
```
python3 unit_tests.py
```

#### In the repo exists testable and untestable code with corresponding unit Tests

### Bad example

```
In app.py - uncomment line 25 and 32, and comment out lines 28-29
In unit_tests.py - uncomment lines 8-16 (change either the system settings or the expected
    test output to current time for the test to pass) and comment out lines 24-52
In time_of_day.py - uncomment lines 3-16 and comment out lines 18-31
In templates/schedule - uncomment line 7 and comment out line 8 (more for reusable code example)
```
