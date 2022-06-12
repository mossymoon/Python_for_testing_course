from model.contact import Contact


testdata = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="",
                      workphone="", secondaryphone="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            address=random_string("address", 10), homephone=random_string("homephone", 10),
            mobilephone=random_string("moobilephone", 10), workphone=random_string("workphone", 10),
            secondaryphone=random_string("secondaryphone", 10))
    for i in range(5)
]

