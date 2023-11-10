grade = float(input())


def grade_in_words(grd):
    if 2.00 <= grd <= 2.99:
        print("Fail")
    elif 3.00 <= grd <= 3.49:
        print("Poor")
    elif 3.50 <= grd <= 4.49:
        print("Good")
    elif 4.50 <= grd <= 5.49:
        print("Very Good")
    elif 5.50 <= grd <= 6.00:
        print("Excellent")


grade_in_words(grade)
