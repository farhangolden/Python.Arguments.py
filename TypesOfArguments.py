def greeting(username,class_name,class_timing):
    print(f"Hi! {username} welcome to {class_name} and its time is {class_timing}")

greeting("Farhan","Python Class","9:00PM TO 10:00PM")
greeting("Ali","Python Class","9:00PM TO 10:00PM")

def display_student_data(*para):
    print(f="the student details are follows{para}")

display_student_data(1,"Sufiyan",[67,90,87],"Mumbai","B.tech")