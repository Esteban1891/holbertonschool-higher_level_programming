# 0x0F. Python - Object-relational mapping

## Description
What you should learn from this project:

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script 
* What ORM means
* How to map a Python Class to a MySQL table

---

### [0. Get all states](./0-select_states.py)
* Write a script that lists all states from the database hbtn_0e_0_usa: 


### [1. Filter states](./1-filter_states.py)
* Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa: 


### [2. Filter states by user input](./2-my_filter_states.py)
* Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.


### [3. SQL Injection...](./3-my_safe_filter_states.py)
* Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?


### [4. Cities by states](./4-cities_by_state.py)
* Write a script that lists all cities from the database hbtn_0e_4_usa 


### [5. All cities by state](./5-filter_cities.py)
* Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa 


### [6. First state model](./model_state.py)
* Write a python file that contains the class definition of a State and an instance Base = declarative_base()


### [7. All states via SQLAlchemy](./7-model_state_fetch_all.py)
* Write a script that lists all State objects from the database hbtn_0e_6_usa 


### [8. First state](./8-model_state_fetch_first.py)
* Write a script that prints the first State object from the database hbtn_0e_6_usa 


### [9. Contains `a`](./9-model_state_filter_a.py)
* Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa 


### [10. Get a state](./10-model_state_my_get.py)
* Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa 


### [11. Add a new state](./11-model_state_insert.py)
* Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa 


### [12. Update a state](./12-model_state_update_id_2.py)
* Write a script that changes the name of a State object from the database hbtn_0e_6_usa 


### [13. Delete states](./13-model_state_delete_a.py)
* Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa 


### [14. Cities in state](./model_city.py)
* Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.

---

## Authors :black_nib:

- [Esteban De La Hoz](https://www.linkedin.com/in/esteban-de-la-hoz-romero-b6270017b/) | [Twitter](https://twitter.com/Esteban18911) | [GitHub](https://github.com/Esteban18911)
