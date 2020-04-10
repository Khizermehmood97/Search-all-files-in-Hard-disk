import mmap, sys, time, win32api, os, multiprocessing, win32api


def search_func(path, files):
    global toSearch
    global result
    for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(path, file)) as f:
                    if toSearch in f.read():
                     #   count+=1
                        result.append(os.path.join(path, file))
                        #print(os.path.join(path, file))
                        f.close()
                        sys.stdout.flush()




if __name__ == '__main__':
    #count = 0
    toSearch = raw_input("Enter the String you want to search in Hard Disk: ")
    
    result = []
    drives = win32api.GetLogicalDriveStrings()
    paths = drives.split('\000')[:-1]
    start_time = time.time()
    for path in paths:
        print("SEARCHING IN DRIVE: "+path)
        try:
            for(path, dirs ,files) in os.walk(path):
                search_func(path, files)
            
            
        except Exception as e:
            print e
            print sys.exc_type

    end_time = time.time()

    print ("\nTotal "+str(len(result))+" Files matched in all Drives: \n")
    for r in result:
            print(r)
    print("\nTotal time spent --- %s seconds ---" % (end_time - start_time))     
    
