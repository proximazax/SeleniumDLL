

def getToday():
    import datetime
    today = datetime.datetime.today().strftime('%Y%m%d')
    return str(today)

def getOldFile(folderPath, fileNameStartWith):
    import os
    oldFile = None

    listOfFiles = os.listdir(folderPath)

    for file in listOfFiles:
        if file.startswith(fileNameStartWith):
            oldFile = folderPath + '/' + file
            break

    return oldFile




def replaceFiles():
    import shutil
    import os

    downloadFolderPath = 'C:/Users/616096/Downloads'
    targetFolderPath = 'C:/Users/616096/Downloads/TaseFiles'
    fileNameInDownloadFolder = 'listedCapital'

    newFileInDownloadPath = downloadFolderPath + '/' + fileNameInDownloadFolder + '.csv'
    if not os.path.exists(newFileInDownloadPath):
        print("Can't find the new file...")
        return

    oldFilePath = getOldFile(targetFolderPath, fileNameStartWith=fileNameInDownloadFolder)
    if not oldFilePath is None:
        os.remove(oldFilePath)
        print('Old file was removed:    ', oldFilePath)

    today = getToday()
    newName = fileNameInDownloadFolder + '_' + today + '.csv'
    shutil.move(newFileInDownloadPath, targetFolderPath + '/' + newName)

    print('New file moved successfully:     ',newName)
    print('\n*** Done! ***')


replaceFiles()

