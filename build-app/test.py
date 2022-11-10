class HelloHook:
    def msg(self):
        print("Hello Hook1")
        print("Hello Hook2")
        print("Hello Hook3")



if __name__=="__main__":

    obj = HelloHook()
    obj.msg()
