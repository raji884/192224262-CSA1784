% student_teacher_subject_code(Student, Teacher, Subject, Code)

student_teacher_subject_code(ravi, kumar, ai, cs301).
student_teacher_subject_code(sita, ramesh, dbms, cs302).
student_teacher_subject_code(rahul, kumar, ai, cs301).
student_teacher_subject_code(priya, lakshmi, cn, cs303).

% Rule to find subject details
subject_details(Student, Teacher, Subject, Code) :-
    student_teacher_subject_code(Student, Teacher, Subject, Code).
