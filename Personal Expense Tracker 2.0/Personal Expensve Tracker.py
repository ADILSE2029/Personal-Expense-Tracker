import module1 as m
user1=m.expensetracker()
while True:

    user_choice_at_start=int(input("1:Add Expense\n2:View Expense\n3:Total Expenses\n4:Exit\noption no:"))
    if user_choice_at_start==1:
        user_given_expense=int(input("Write Expense:"))
        while True:
               
               user_input=int(input("1:Add More Expense\n2:Exit\nOption No:"))
               if user_input==1:
                        user_input=input("Write Expense:")
                        user_given_expense+=int(user_input)
               elif user_input==2:
                      print("Expense Added")
                      break
        
        user_given_category=input("Write Category:")
        user_given_date=input("Write Date (Without any sign in this format:mm/dd/yy):")
        user1.add_expense(user_given_expense,user_given_category,user_given_date)
        print("Record Added")
        ## for View Expense System
    elif user_choice_at_start==2:
        user_choice=int(input("1:View By Date\n2:View By Category\n3:View By Largest Expense\nOption No:"))
        if user_choice==1:                
                    
                    user1.view_expense(1)
        elif user_choice==2:
                    user1.view_expense(2)
        elif user_choice==3:
               user1.view_expense(3)

    elif user_choice_at_start==3:
          user_input=int(input("1:Total By Most Expense\n2:Total By Category\n3:Total By Date\nOption No:"))
          if user_input==1:
                 
            user1.total(1)
          elif user_input==2:
                user1.total(2)
          elif user_input==3:
                user1.total(3)

    elif user_choice_at_start==4:
          print("Thanks For Using This Program")
          break
          
          
                    
        
        
    


        
                         
        
                


    

    elif user_choice_at_start==5:
        break


