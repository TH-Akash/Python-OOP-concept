print("Decorator")


def dec1(function):
    def nowexec():
        print("Execution now ")
        function()
        print("Execution end")
    return nowexec


@dec1
def Who_is_Akash():
    print("Akash is good boy")


Who_is_Akash()
