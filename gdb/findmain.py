import gdb

class FindMainCommand(gdb.Command):
    def __init__(self):
        super().__init__("findmain", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        # first break at _dl_start_user
        gdb.Breakpoint("_dl_start_user")
        gdb.execute("r")

        # now, find the address of where the linker returns out to user code
        dl_start_user_addr = int(gdb.parse_and_eval("$rip"))
        gdb.Breakpoint(f"*{dl_start_user_addr + 88}")
        gdb.execute("c")

        # r12 register will be near main, add 31 to get true main address in rdi register
        # 31 is added because that is where main function is called according to stack analysis
        r12 = int(gdb.parse_and_eval("$r12"))
        gdb.Breakpoint(f"*{r12+31}")
        gdb.execute("c")

        # read rdi register, will be address of endbr64 of main function, add 8 to it to get same main addr as gdb
        rdi = int(gdb.parse_and_eval("$rdi"))
        main_addr = rdi + 8
        print(f"main found at address: {(main_addr):#x}")

        # run code
        gdb.execute("c")


FindMainCommand()
