import cuhkEnv as env
# import sortTime as sortTime

run = True

def repeat(times, f):
    for i in range(times):
        f()

while run is True:
    userId = input("Your ID: ")
    userPassword = input("Your Password: ")
    user = env.personal(userId, userPassword)

    try:
        print(user)
        env.personal.login(user)
        if env.personal.check_error() is True:
            env.personal.close()
            print("error")
        else:
            while run is True:
                ask = input(
                    """
what do you want man!?
1. My academics
2. academic requirement
3. exit
"""
                )

                if ask == "1":
                    env.personal.my_academics()
                    repeat(1, env.personal.go_back)
                    env.personal.change_frame()
                elif ask == "2":
                    env.personal.academic_requirements()
                    num = int(input("how many courses would you like to search?"))
                    course= []
                    course_list = []
                    for i in range(num):
                        askCode = input("insert the code:")
                        view_all_click, course_period = env.personal.get_time(askCode.upper())
                        repeat(view_all_click+2, env.personal.go_back)
                        env.personal.change_frame()
                        course.append(course_period)

                        for i in range(len(course)):
                            print(course[i])

                        course_list.append(course)
                elif ask == "quit":
                    break
                    
                        

                        
                    

                    # for i in range(len(course_list)):
                    #     """ check the possible combination of sections one by one? or should i randomise until they get one?
                    #     """
                    #     subject_1 = sortTime.time_table()
                    #     subject_2 = sortTime.time_table()



                elif ask == "3":
                    run = False
        
    except ValueError:
        env.personal.close()
        
# env.personal.close()