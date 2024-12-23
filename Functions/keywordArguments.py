# For Keyword Arguments.
def keyword_argument(**kwargs):
    print("Print Keyword Arguments")
    for key,value in kwargs.items():
        print("{} is: {}".format(key,value))
    print("\n")

#Function Call
keyword_argument(Firstname="Hasan", Lastname="Rony", Age=25, Phone=1234567890)
keyword_argument(Firstname="M", Lastname="Rashid", Email="noname@example.com",
Country="Bangladesh", Age=26, Phone=9876543210)