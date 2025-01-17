CREATE INDEX "enrollments_student_id_index" ON "enrollments" ("student_id");

CREATE INDEX "enrollments_course_id_index" ON "enrollments" ("course_id");

CREATE INDEX "semester_index" ON "courses" ("semester");

CREATE INDEX "courses_department_index" ON "courses" ("department");

CREATE INDEX "satisfies_course_id_index" ON "satisfies" ("course_id");

CREATE INDEX "satisfies_requeriment_id_index" ON "satisfies" ("requeriment_id");






