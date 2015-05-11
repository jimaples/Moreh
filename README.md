# Moreh
Multiple choice question framework for learning Hebrew
Web-based GUI based on Django and Google App Engine

## Key Files
File|Description
-----|-----
djangoserver.sh|Start a local Linux Django server for testing code
djangoserver.bat|Start a local Windows Django server for testing code
templates/*|Django template files for each view
moreh/*|Django project files
hebrew_quiz/*|Define Django views, URLs, and data models
hebrew_quiz/static/*|HTML static files (background images, CSS, etc...) 
hebrew_quiz/code/*|Python application files
hebrew_quiz/code/Moreh.py|Define question/answer sets
hebrew_quiz/code/Quizzer.py|Generic quiz module
hebrew_quiz/code/Hebrew.py|Load Hebrew databases
hebrew_quiz/code/GenerateUnicode.py|Support script to generate *.csv database
hebrew_quiz/code/HebrewReference.csv|Hebrew databases to use for questions and answers

## References
The [wiki page](https://github.com/jimaples/Moreh/wiki/References) covers Hebrew, Learning Assessment and Feedback, Python, Django, User Interfaces, and Examples.

## Next Steps
A list of potential future tasks is listed in the [project wiki](https://github.com/jimaples/Moreh/wiki/Next-Steps)
