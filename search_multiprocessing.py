import mmap, sys, time, win32api, os, multiprocessing

#path = 'C:\\Users\\Khizer Mehmood\\Desktop\\test'
#path = 'E:\\'
#path = 'C:\Users'


def search_func_process(path, files):
    #global count
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(path, file)) as f:
                if 'khizer' in f.read():               # Replace 'khizer' with your string you want to search
                   # count.value = count.value+1
                    print(os.path.join(path, file))
                    f.close()
                    sys.stdout.flush()



if __name__ == '__main__':

    #result = []
    drives = win32api.GetLogicalDriveStrings()
    paths = drives.split('\000')[:-1]
    #paths = ["C:\\Users\\Khizer Mehmood\\Desktop\\test", "E:\\"]
    
    for path in paths:
        processes = []
        #count = multiprocessing.Value('i',0) #shared variable 
        start_time = time.time()
        try:
            for(path, dirs ,files) in os.walk(path):
                p = multiprocessing.Process(target=search_func_process, args=(path,files))
                processes.append(p)
                p.start()
            
            for process in processes:
                process.join()
            
        except Exception as e:
            print e
            print sys.exc_type

        end_time = time.time()

        print("--- %s seconds ---" % (end_time - start_time))    
        #print(count.value)      