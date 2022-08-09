# Metro Problem by Maktab78
A metro simulation by [ahadiyanhr](https://github.com/ahadiyanhr)

The code here implements a Trip process in a Metro system.

All necessary inputs are specified in the main menu file of `main.py`. This is also the file you run to carry out the simulation.
During running the main menu (`main.py`), a copy of all logs and data, such as user objects and admin objects, is saved into `metro.log`, `users.pickle`, and `admins.pickle`.
All classes and their methods were tested by `UNITTEST` python library in `tests.py`, and all specific needed exceptions for handling errors in this projects, wrote in `exceptions.py`.
To sum up, this project has 9 different py files that are described below:
1. `main.py`: ```YOU must run this file to use the metro program```.
2. `User.py`: creates user objects with their attributes and methods;
3. `Admin.py`: creates admin objects with their attributes and methods;
4. `BankAccount.py`: manages a bank account of users/admins;
5. `MetroCard.py`: creates cards for users/admins for using in trips;
6. `Trip.py`: manages and performs trips by users/admins;
7. `tests.py`: includes all tests for classes and methods by unittest library;
8. `exceptions.py`: includes all exceptions and user-defined errors for this project;
9. `other_func.py`: other functions which are valuable for main menu well-running.

Additionally, this project is associated with three more files that they are:
1. `0-9.pdf`: Documents includes problems and project requirements;
2. `metro_by_drawSQL.png`: Picture of ERD of the metro project which is provided by [drawSQL](https://drawsql.app);
3. `README.md`: readme file that you are reading right now!!

Finally, you can see the ER Diagram of the metro project below:
![alt text](https://github.com/ahadiyanhr/Practices-M78/blob/main/HW/09-Metro/metro_by_drawSQL.png)