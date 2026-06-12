% diet(Disease, Diet)

diet(diabetes, low_sugar_food).
diet(bp, low_salt_food).
diet(obesity, low_fat_food).
diet(anemia, iron_rich_food).

% Rule
suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).
