import addUser
import showUser
import deleteUser
import addImage
import assignImage
import sendEmail

def runShowContactsFile(self):
        self.withdraw()
        showUser.ShowUser()

def runAddContactFile(self):
        self.withdraw()
        addUser.AddContact()

def runDeleteContactFile(self):
        self.withdraw()
        deleteUser.deleteUser()

def runAddImageFile(self):
        self.withdraw()
        addImage.AddImage()

def runAssignImageFile(self):
        self.withdraw()
        assignImage.AssignImage()

def runSendEmailFile(self):
        self.withdraw()
        sendEmail.SendEmail()
    