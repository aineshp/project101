import dropbox 
class TransferData: 
    def __init__(self,accesstoken): 
        self.accesstoken=accesstoken 
    def uploadFile(self,file_from,file_to): 
        dbx = dropbox.Dropbox(self.accesstoken) 
        f=open(file_from,'rb')   
        dbx.files_upload(f.read(),file_to) 
def main(): 
    accesstoken='pZgBk9L6JTwAAAAAAAAAxAS49MoVDGj8uivrBAI0RmaKAB4Z6oRurLKwhXfJyUrE9'
    transferData=TransferData(accesstoken) 
    file_from=input('Enter name of the file: ') 
    file_to='/Python1/openedfile.txt' 
    transferData.uploadFile(file_from,file_to) 
    print('File has been moved')
if __name__ == '__main__':
    main() 