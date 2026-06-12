% Facts: person(Name, DOB)

person('Ravi', date(15, 5, 2000)).
person('Sita', date(20, 8, 1999)).
person('Rahul', date(10, 1, 2001)).
person('Priya', date(25, 12, 2002)).

% Rule to display DOB of a person
dob(Name, DOB) :-
    person(Name, DOB).
