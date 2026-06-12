% Disease and Symptoms

disease(flu, fever).
disease(flu, cough).

disease(malaria, fever).
disease(malaria, headache).

disease(cold, cough).
disease(cold, sneezing).

% Rule to diagnose disease
diagnose(Disease, Symptom) :-
    disease(Disease, Symptom).
