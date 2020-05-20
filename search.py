print("\n\nWelcome to Motion Picture Fusion Integrated Numerical Decision Express Rectifier")
print("Better know as Movie Finder")

def solicit_user_action():
    """Gets the User's Main Menu Choice"""
    print("\nFind that movie!")
    print("1.  Auto Movie Pick \t2.  Your Pick   \t3.  Random Choice \n4.  List Pop movies \t5.  View by Genre \t6.  Movie List \n7.  View by vote \t8.  Search by Movie \t9.  Search by Genre \n10. Buy Tickets \t11. Find Theater \t12. Stream Now \n13. Cross streams\t14. Watch Trailer\t15. Your Favorites\n16. Exit ")

    user_selection = input('What would you like to do?').lower()
    print(user_selection)

if __name__ == "__main__":
    while True:
        solicit_user_action()
