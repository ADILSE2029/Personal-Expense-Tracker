
class expensetracker:
    ## addition system
    def add_expense(self,expense,category,date):
        self.expense=expense
        self.category=category
        self.date=date
        datafile=open("expensetracker.txt","a")
        datafile.write(str(self.expense)+"\n")
        datafile.write(str(self.category) +"\n")
        datafile.write(str(self.date)+"\n")
        datafile.close()
    ## view system
    def view_expense(self,type):
        self.type=type
        if self.type==1:  ## for view by date           
            Found=False     
            self.data=input("Write Date(mm/dd/yy):")
            with open("expensetracker.txt","r") as f:
                stored_data=f.readlines()
                for i in range(0,len(stored_data),3):
                    stored_Expense=stored_data[i].strip()
                    stored_Category=stored_data[i+1].strip()
                    stored_Dates=stored_data[i+2].strip()
                    if self.data==stored_Dates:
                        print(f"Expenses for date {stored_Dates} are : {stored_Expense}")
                        Found=True
                if Found==False:
                        print("No Data Available for that Date")
                
                        
        elif self.type==2: ##for view by Category
            Found=False
            self.category=input("Write Category:")
            with open("expensetracker.txt","r") as f :
                stored_data=f.readlines()
                for i in range(0,len(stored_data),3):
                    stored_category=stored_data[i+1].strip()
                    stored_expense=stored_data[i].strip()
                    if stored_category==self.category:
                        print(f"Expenses for Category {stored_category} are {stored_expense}$")
                        Found=True
                if Found==False:
                        print("No Data Available for that Category")
        elif self.type==3:  ##view by Largest Expense
            self.Expenses=0
            self.date_record=None
            self.category_record=None
            with open("expensetracker.txt","r") as f :
                stored_data=f.readlines()

                for i in range(0,len(stored_data),3):
                    
                    stored_expense=int(stored_data[i].strip())
                    self.Expenses+=stored_expense
                    stored_date=stored_data[i+2].strip()
                    stored_Category=stored_data[i+1].strip()
                    if int(stored_expense)>int(self.Expenses):
                        self.Expenses=stored_expense
                        self.date_record=stored_date
                        self.category_record=stored_Category

            print(f"Largest Expenses Are {self.Expenses}$ for Category {self.category_record} at date {self.date_record}")
                    
    def total(self,type):
        self.type=type
        if self.type==1:       ## for largest expense overall

            with open("expensetracker.txt","r") as f:
                total=0
                stored_data=f.readlines()
                for i in range(0,len(stored_data),3):
                    stored_expenses=stored_data[i].strip()
                
                    total+=int(stored_expenses)
                print(f"Total Expenses Are :{total}$")
        elif self.type==2:       ## for total of specific Category
                user_input=input("Write Category:")
                total_value=0
                with open("expensetracker.txt","r") as f:
                    stored_data=f.readlines()
                    for i in range(0,len(stored_data),3):
                        stored_category=stored_data[i+1].strip()
                        stored_expense=stored_data[i].strip()
                        if user_input==stored_category:
                            total_value+=int(stored_expense)
                print(f"Total Expenses for Category {stored_category} is {total_value}$")
        elif self.type==3:
            user_input=input("Write Date(mm/dd/yy):")
            
            with open("expensetracker.txt","r") as f:
                    stored_data=f.readlines()
                    for i in range(0,len(stored_data),3):
                        stored_category=stored_data[i+1].strip()
                        stored_expense=stored_data[i].strip()
                        stored_date=stored_data[i+2].strip()
                        if user_input==stored_date:          
                            print(f"Total Expenses for Date {stored_date} is {stored_expense}$")



        
                
                
            
                

        
        

