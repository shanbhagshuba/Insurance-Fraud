from datetime import datetime

class activity_logger:
    
    def author(self):
        return 'Shuba Shanbhag'
    
    def log(self,file_object,message):
        now = datetime.now()
        date = now.date()
        current_time = now.strftime("%H:%M:%S")
        file_object.write(str(date) + "/" + str(current_time) + "\t\t" + message +"\n")

