% planet(Name, Distance_from_Sun_Million_Km, Type)

planet(mercury, 58, terrestrial).
planet(venus, 108, terrestrial).
planet(earth, 150, terrestrial).
planet(mars, 228, terrestrial).
planet(jupiter, 778, gas_giant).
planet(saturn, 1433, gas_giant).
planet(uranus, 2872, ice_giant).
planet(neptune, 4495, ice_giant).

% Rule to get planet details
planet_details(Name, Distance, Type) :-
    planet(Name, Distance, Type).
