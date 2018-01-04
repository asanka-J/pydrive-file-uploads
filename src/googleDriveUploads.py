from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive



def googleUpload(creditialpath="credentialst.txt",fileToUpload="test.txt"):

    gauth = GoogleAuth()# Try to load saved client credentials
    gauth.LoadCredentialsFile(creditialpath)
    if gauth.credentials is None: # Authenticate if they're not there
        gauth.LocalWebserverAuth()

    elif gauth.access_token_expired: # Refresh them if expired
        gauth.Refresh()
    else:  # Initialize the saved creds
        gauth.Authorize()
    
    gauth.SaveCredentialsFile("credentialst.txt")

    drive = GoogleDrive(gauth)


    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    folderExistStatus=False
    for file2 in file_list:
       # print('title: %s, id: %s' % (file1['title'], file1['id']))

        if file2['title'] == 'cryptoInfo':
           folderExistStatus=True
           folderid=file2['id']
           print("file exists")


    if folderExistStatus==False:
        folder_metadata = {'title' : 'cryptoInfo', 'mimeType' : 'application/vnd.google-apps.folder'}
        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
        folderid = folder['id']


    
    # foldertitle = folder['title']
    # folderid = folder['id']
    # print('title: %s, id: %s' % (foldertitle, folderid))

    #Upload file to folder
    file = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folderid}]})
    file.SetContentFile(fileToUpload)
    file.Upload()
    print("Sucessfully uploaded")

   

googleUpload()