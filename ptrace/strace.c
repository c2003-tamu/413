#include <sys/ptrace.h>
#include <sys/user.h>
#include <sys/reg.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int child_func(int argc, char **argv);
int parent_func(pid_t child);
int wait_for_syscall(pid_t child);

int main(int argc, char **argv) {
    if (argc < 2){
        printf("usage: %s prog args \n", argv[0]);
        exit(1);
    }

    pid_t child_pid = fork();
    if(child_pid == 0){
        return child_func(argc-1, argv+1);
    } else {
        return parent_func(child_pid);
    }
}

int child_func(int argc, char **argv) {
    char *args [argc+1];
    memcpy(args, argv, argc * sizeof(char*));
    args[argc] = NULL;

    ptrace(PTRACE_TRACEME);
    kill(getpid(), SIGSTOP);
    return execvp(args[0], args);
}

int parent_func(pid_t child) {
    int status, syscall_number, retval;
    struct user_regs_struct registers;
    waitpid(child, &status, 0);
    ptrace(PTRACE_SETOPTIONS, child, 0, PTRACE_O_TRACESYSGOOD); 
    
    while(1) {
        ptrace(PTRACE_GETREGS, child, NULL, &registers);
        printf("\nregs before syscall:\n rbx: %llu,\n rcx: %llu,\n rdx: %llu, \n", registers.rbx, registers.rcx, registers.rdx);
        if (wait_for_syscall(child) != 0) break;

        syscall_number = ptrace(PTRACE_PEEKUSER, child, sizeof(long)*ORIG_RAX);
        printf("\nsyscall: %i\n", syscall_number);
                
        ptrace(PTRACE_GETREGS, child, NULL, &registers);
        printf("\nregs after syscall:\n rbx: %llu,\n rcx: %llu,\n rdx: %llu, \n", registers.rbx, registers.rcx, registers.rdx);
    }
    return 0;
}

int wait_for_syscall(pid_t child) {
    int status;
    while (1) {
        if (ptrace(PTRACE_SYSCALL, child, 0, 0) == -1)
            return -1;

        waitpid(child, &status, 0);

        if (WIFEXITED(status) || WIFSIGNALED(status))
            return -1;

        if (WIFSTOPPED(status)) {
            int sig = WSTOPSIG(status);

            if (sig == (SIGTRAP | 0x80))
                return 0;
        }
    }
}
