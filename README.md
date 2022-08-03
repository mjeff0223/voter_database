Voter Application
This application is an initial attempt to create Election software. Currently I am working on the backend functionality but eventually I intend to create a frontend as well.
The app will allow users to register as voters, create an account and cast ballots electronically. The database will keep track of election results and user information.
Current APIs:
baseURL = http://localhost:5000"
/voters : GET request displays list of registered voters
/voters/<id> : GET request shows single voter corresponding with the id input by the user
/accounts : GET request shows list of accounts currently in database
/accounts/<id> GET request shows list of voter with matching ID input by user, 
/ballots : shows current ballot information 
APIs called on voters have GET, POST, and DELETE requests
APIs called on accounts have GET, POST, PUT and DELETE requests
APIs called on ballots have GET requests only. 

In the future authorization will be required to get information from APIs on anything other than election results. 
In the future I also will explore how blockchain technology can help with transparency and accountability of all results. 
