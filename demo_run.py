from entities import Student, Course
from registration import student_registration, drop_course

students = {                                    # students and courses are stored in dictionaries, so we can find them by id
    "S1": Student("S1", 1, set()),
    "S2": Student("S2", 2, {"MSCS532"}),
    "S3": Student("S3", 3, {"MSCS532"}),
    "S4": Student("S4", 4, {"MSCS532"}),
}
courses = {
    "MSCS532": Course("MSCS532", 100, 1, [("Mon", 9, 10)], set()),
    "ITSI336": Course("ITSI336", 200, 1, [("Tue", 9, 10)], {"MSCS532"}),
}


def register(student_id, course_id):            # register a student and print the result
    print(f"{student_id} -> {course_id}:", student_registration(students[student_id], courses[course_id]))


if __name__ == "__main__":

    register("S1", "MSCS532")                     # gets the only seat
    register("S1", "MSCS532")                     # already registered
    register("S1", "ITSI336")                     # missing prerequisite
    register("S2", "ITSI336")                     # gets the only seat
    register("S3", "ITSI336")                     # course is full, goes to the waitlist
    register("S4", "ITSI336")                     # senior, goes ahead of S3

    print(drop_course(students["S2"], courses["ITSI336"], students))      # S4 gets the seat