
class expensetracker:
    
    def add_expense(self,expense,category,date):
        self.expense=expense
        self.category=category
        self.date=date
        datafile=open("expensetracker.txt","a")
        datafile.write(str(self.expense)+"\n")
        datafile.write(str(self.category) +"\n")
        datafile.write(str(self.date)+"\n")
        datafile.close()
    
    def view_expense(self,type):
        self.type=type
        if self.type==1:             
            Found=False     
            self.data=input("Write Date(mm/dd/yy):")
            with open("expensetracker.txt","r") as f:
                stored_data=f.readlines()
                for i in range(0,len(stored_data),3):
                    stored_Expense=stored_data[i].strip()
                    stored_Category=stored_data[i+1].strip()
                    stored_Dates=stored_data[i+2].strip()
                    if self.data==str(stored_Dates):
                        print(f"Expenses for date {stored_Dates} are : {stored_Expense}")
                        Found=True
                    if Found==False:
                        print("No Data Available for that Date")
                
                        
        elif self.type==2:
            Found=False
            self.category=input("Write Category:")
            with open("expensetracker.txt","r") as f :
                stored_data=f.readlines()
                for i in range(0,len(stored_data),3):
                    stored_category=stored_data[i+1].strip()
                    stored_expense=stored_data[i].strip()
                    if stored_category==str(self.category):
                        print(f"Expenses for Category {stored_category} are {stored_expense}")
                        Found=True
                    if Found==False:
                        print("No Data Available for that Category")
        elif self.type==3:
            self.Expenses=0
            self.date_record=None
            self.category_record=None
            with open("expensetracker.txt","r") as f :
                stored_data=f.readlines()

                for i in range(0,len(stored_data),3):
                    
                    stored_expense=int(stored_data[i].strip())
                    stored_expense+=int(self.Expenses)
                    stored_date=stored_data[i+2].strip()
                    stored_Category=stored_data[i+1].strip()
                    if int(stored_expense)>int(self.Expenses):
                        self.Expenses=stored_expense
                        self.date_record=stored_date
                        self.category_record=stored_Category

            print(f"Largest Expenses Are {self.Expenses} for Category {self.category_record} at date {self.date_record}")
                    
    def total(self):
        with open("expensetracker.txt","r") as f:
            total=0
            stored_data=f.readlines()
            for i in range(0,len(stored_data),3):
                stored_expenses=stored_data[i].strip()
                
                total+=int(stored_expenses)
            print(f"Total Expenses Are :{total}$")
                
                
                
            
                

        
        

