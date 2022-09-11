# 0x0F-python-object_relational_mapping

## Mandatory

1. 0-select_states.py - A script that lists all `states` from the database `hbtn_0e_0_usa` under some conditions
2. 1-filter_states.py - A script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`
3. 2-my_filter_states.py - A script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument
4. 3-my_safe_filter_states.py - A script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!
5. 4-cities_by_state.py - A script that lists all `cities` from the database `hbtn_0e_4_usa`
6. 5-filter_cities.py - A script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`
7. 7-model_state_fetch_all.py - A script that lists all `State` objects from the database `hbtn_0e_6_usa`
8. 8-model_state_fetch_first.py -  A script that prints the first `State` object from the database `hbtn_0e_6_usa`
9. 9-model_state_filter_a.py - A script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`
10. 10-model_state_my_get.py - A script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`
11. 11-model_state_insert.py - A script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`
12. 12-model_state_update_id_2.py - A script that changes the name of a `State` object from the database `hbtn_0e_6_usa`
13. 13-model_state_delete_a.py - A script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`
14. 14-model_city_fetch_by_state.py - A script that prints all `City` objects from the database `hbtn_0e_14_usa`
15. 15-roman_to_int.py - A function `def roman_to_int(roman_string):` that converts a Roman numeral to an integer

## Advanced

100-relationship_states_cities.py
101-relationship_states_cities_list.py
102-relationship_cities_states_list.py
model_city.py
model_state.py
relationship_city.py
relationship_state.py
