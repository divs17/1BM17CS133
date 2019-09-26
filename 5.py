class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.__phoneno=phoneno
        self.__called_no=called_no
        self.__duration=duration
        self.__call_type=call_type

    def print1(self):
        print(self.__phoneno,' ',self.__called_no,' ',self.__duration,' ',self.__call_type)



class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        self.list_of_call_objects=[]
        for i in list_of_call_string:
            phoneno,called_no,duration,call_type=map(str,i.split(","))
            self.list_of_call_objects.append(CallDetail(phoneno,called_no,duration,call_type))
            c1=CallDetail(phoneno,called_no,duration,call_type)
            c1.print1()


call1='9148530090,9851005518,12,ISD'
call2='9954367877,9854367432,24,LOCAL'
call3='9805421445,9765125878,32,ISD'
call4='9852347654,9876123456,28,LOCAL'

list_of_call_string=[call1,call2,call3,call4]
Util().parse_customer(list_of_call_string)
        
