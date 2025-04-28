# Program that determines if a student has passed or failed based on their scores. Pass marks is 50 or above. if passes check whether student has scored above 90 for a distinction
marks = float(input("Enter the marks you has obtained in exam: "))
if marks >= 50:
    """
    This condition checks whether the student has passed or failed.
    If the marks is greater or equal to 50 then s/he is passsed else failed.
    """
    if marks >= 90:
        """
        This condition checks whether the student has scored above 90 for a distinction.
        """
        name = input("Enter your name: ")
        print("Congratulations!", name, "You have passed with distinction.")
    else:
        print("You have passed.")
else:
    print("You have failed.")