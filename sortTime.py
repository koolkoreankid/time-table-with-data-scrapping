import random, math


def sort_time(course_list):
    course_classified = []
    for i in range(len(course_list)):
        # course_list[i] =   



class time_table:
    def __init__(self, course, lec_or_tut, day, start, end):
        self.course = course
        self.lec_or_tut = lec_or_tut
        self.day = day
        self.start = start
        self.end = end

    @staticmethod
    def check_cross(subject1, subject2):
        """
        check sub1's day, start and end with sub2's
        """
        pass
