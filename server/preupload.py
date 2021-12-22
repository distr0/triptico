import os
import time
import glob
import shutil
from subprocess import check_output
import datetime

in_folder="/var/sftp/triptico/"
out_folder="/home/<user>/triptico/tripticoEdge/"
log_file="/home/<user>/triptico/log.csv"

f_size=[]
files = glob.glob(in_folder+"**/*.*",recursive=True)
print("Encontré {} archivos".format(len(files)))

if files:
    print("Comprobando cambios en tamaño")
    for f in files:
       f_size.append(os.path.getsize(f))

    time.sleep(5)

    i=0
    for f in files:
        s=os.path.getsize(f)
        if s != f_size[i]:
            files.remove(f)
        i+=1

    print("\n{} archivos están listos para subir".format(len(files)))

    if files:
        tipo={"RPiFotos":0,"RPiREC":0,"RPiIMU":0,"RPiIMU2":0}
        print("\nMoviendo a "+out_folder+":")
        for f in files:
            print(f)
            f_path=f.split("/")
            shutil.move(f,out_folder+f_path[-2]+"/"+f_path[-1])
            tipo[f_path[-2]]=tipo[f_path[-2]]+1

        print("")
        try:
            uploadScript=check_output(["/usr/bin/bash","/home/<user>/triptico/upload.sh"])
            print(uploadScript)
            error=0
        except Exception as e:
            error=e.returncode

        t=datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        log="{},{},{},{}".format(t,len(files),tipo,error)
        print("\n"+log)

        logger=open(log_file,"a")
        logger.write(log+"\n")
        logger.close()
