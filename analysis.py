import mysql.connector,datetime
user_acc =mysql.connector.connect(
            host="localhost",
            user="root",
            password="vijaykavi",
            database="covid"
           
           )
def data_insert(state,distic,village,positive,death,recovery):
           
            mycursor=user_acc.cursor()
            current_time = datetime.datetime.now()
            print (current_time)
            data_insert="insert into data(state,distic,village,positive_case,death_case,recovered_case) value(%s,%s,%s,%s,%s,%s)"
            data=(state,distic,village,positive,death,recovery)
            mycursor.execute(data_insert,data)
            user_acc.commit()
            print("data added Successful!")
def village(v):
    mycursor=user_acc.cursor()
    mycursor.execute(f"select positive_case,death_case,recovered_case from data where village='{v}'")
    result=mycursor.fetchall()
    if result!=[]:
        vk=result[0]
        print(f"{v} positive cases='{vk[0]}'")
        print(f"{v} death_cases='{vk[1]}'")
        print(f"{v} recovered_cases='{vk[2]}'")
    else:
        print("Enter valdi village name")
def district(distic):
    
    mycursor=user_acc.cursor()
    mycursor.execute(f"select village from data where distic='{distic}' ")
    result=mycursor.fetchall()
    if result!=[]:
        for i in range(len(result)):
          vk=result[i]
          print(f"'{i}'",vk[0])
        v=input("enter your village: ")
        village(v)
    else:
        print("Please enter valid distict")

def search(state):
    
            mycursor=user_acc.cursor()
            mycursor.execute(f"select distic from data where state='{state}' ")
            result=mycursor.fetchall()
            if result!=[]:
              for i in range(len(result)):
                 vk=result[i]
                 print(f"'{i}'",vk[0])
              distic=input("Enter your district: ")
              district(distic)
            else:
               print("Please enter valid state")

user=int(input("\nenter 1 to add data\n enter 2 to search you data\n"))
if user==1:
    state=input("Enter Your State: ")
    distic=input("Enter Your distic: ")
    village=input("Enter Your village: ")
    positive=input("Enter Your positive: ")
    death=input("Enter Your death: ")
    recovery=input("Enter Your recovery: ")
    data_insert(state,distic,village,positive,death,recovery)
elif user==2:
    state=input("enter your state: ")
    search(state)
else:
    print("thanks for visit")


