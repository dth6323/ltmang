import ftplib
import os
def menu():
    print("\nMenu")
    print("1.List directory")
    print("2.Change directory")
    print("3.Create directory")
    print("4.Delete file")
    print("5.Delete directory")
    print("6.Rename file and directory")
    print("7.Get file size")
    print("8.Download file")
    print("9.Upload file")
    print("10. Send custom command")
    print("11.Exit")

def list_directory(ftp):
    print("\nList Directory\n")
    try:
        files = []
        ftp.dir(files.append)
        return files
    except ftplib.all_errors as e:
        print(f"Error list directory:{e}")
        return []

def change_directory(ftp, directory):
    print("\nChange Directory\n")
    try:
        ftp.cwd(directory)
        print(f"changed to directory:{directory}")
        
    except ftplib.all_errors as e:
        print(f"Error change directory:{e}")

def create_directory(ftp, directory):
    print("\nCreate Directory\n")
    try:
        ftp.mkd(directory)
        print(f"New directory:{directory}")
    except ftplib.all_errors as e:
        print(f"Error create directory:{e}")

def delete_file(ftp, directory):
    print("\nDelete File\n")
    try:
        ftp.delete(directory)
        print(f"delete file:{directory}")
    except ftplib.all_errors as e:
        print(f"Error delete file:{e}")
def delete_directory(ftp, directory):
    print("\nDelete Directory\n")
    try:
        ftp.rmd(directory)
        print(f"delete directory:{directory}")
    except ftplib.all_errors as e:
        print(f"Error delete directory:{e}")
        
def rename_file_directory(ftp, oldname, newname):
    print("\nRename File and Directory\n")
    try:
        ftp.rename(oldname, newname)
        print(f"Rename file or directory:{oldname} to {newname}")
    except ftplib.all_errors as e:
        print(f"Error rename file or directory:{e}")
 
def get_file_size(ftp, file):
    print("\nGet file size\n")
    try:
        size = ftp.size(file)
        print(f"file {file} have size {size}")
    except ftplib.all_errors as e:
        print(f"Error get file size :{e}")   
        return None    

def download_file(ftp, file_origin, file_copy):
    print("\nDowload File and Directory\n")
    try:
        with open(file_copy,"wb") as fp:
            ftp.retrbinary("RETR"+ file_origin, fp.write(file_copy))
        print(f"file {file_origin} copy successfull")
    except ftplib.all_errors as e:
        print(f"Error download file :{e}")   
        if(os.path.isfile(file_copy)):
            os.remove(file_copy)    

def upload_file(ftp, file_origin):
    print("\nUpload File and Directory\n")
    try:
        with open(file_origin,"rb") as fp:
            response =ftp.storbinary("STOR"+ file_origin, fp)
            print(f"Server response:{response}")
            if not response.startwith("226"):
                print("upload file failed!")
            else:
                print(f"file {file_origin} upload successfull")
    except ftplib.all_errors as e:
        print(f"Error upload file :{e}")  

def send_custom_command(ftp, command):
    print("\nSend Custom Command\n")
    try:
        response = ftp.sendcmd(command)
        return response
    except ftplib.all_errors as e:
        print(f"Error send_custom_command :{e}")  
     
if __name__ == '__main__':
    #dang nhap vao zilla
    with ftplib.FTP("127.0.0.1") as ftp:
        try:
            ftp.login("User02","123")
            ftp.set_pasv(True)
            print(ftp.getwelcome())
        
            while True:
                menu()
                choice = input("Enter your select:")
                if choice == "1":
                    entries = list_directory(ftp)
                    print(len(entries), "entries:")
                    for entry in entries:
                        print(entry)
                elif choice=="2":
                    directory= input("Enter directory name to change:")
                    change_directory(ftp, directory)
                elif choice=="3":
                    directory= input("Enter directory name to create:")
                    create_directory(ftp, directory)
                elif choice=="4":
                    directory= input("Enter file name to delete:")
                    delete_file(ftp, directory)
                elif choice=="5":
                    directory= input("Enter directory name to delete:")
                    delete_directory(ftp, directory)
                elif choice=="6":
                    oldname= input("Enter directory name to rename:")
                    newname= input("Enter new name:")
                    rename_file_directory(ftp, oldname, newname)
                elif choice=="7":
                    file = input("Enter file name to get size:")
                    get_file_size(ftp, file)
                elif choice=="8":
                    file = input("Enter file name to download:")
                    file_copy = input("Enter file name to copy:")
                    download_file(ftp, file, file_copy)
                elif choice=="9":
                    file = input("Enter file name to upload:")
                    upload_file(ftp, file)
                elif choice=="10":
                    cmd = input("Command:")
                    response = send_custom_command(ftp, cmd)
                    if response:
                        print(response)
                else:
                    exit()
        except ftplib.all_errors as e:
            print(f"FTP errors:{e}")
    