#Defects Tracking System
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as db

global cnnDTS, curDTS, mygbcolor, databaseName, databaseServer, databaseUser, databasePassword,currentSc

currentSc=0
mygbcolor = "#008080"
databaseName = "DTS"
databaseServer="localhost"
databaseUser="root"
databasePassword="root24"

class DTSUsers:
       def  __init__(self,userID,password,userTypeID):
              self.userID=userID
              self.password=password
              self.userTypeID=userTypeID

class Projects:
       def  __init__(self,ProjectID,ProjectDesc):
              self.ProjectID=ProjectID
              self.ProjectDesc=ProjectDesc

#Clear screens
def destroySc():
       
       if currentSc==1:
              destroyProjects()
       elif currentSc==2:
              destroyUsers()
       elif currentSc==3:
              destroyIssues()
       elif currentSc==4:
              destroySearchIssues()
       elif currentSc==5:
              destroySearchResults()
def destroyUsers():
       global lblUsers, cboUsers,  btnUserDisplay, lblUserID, txtUserID, lblDTSUserName, txtDTSUserName,\
       lblDTSPassword, txtDTSPassword, lblDTSCheckPassword, txtDTSCheckPassword, lblUserType, cboUserType,\
       btnUserSave, btnUserDelete,lb
       
       lblUsers.destroy()
       cboUsers.destroy()
       btnUserDisplay.destroy()
       lblUserID.destroy()
       txtUserID.destroy()
       lblDTSUserName.destroy()
       txtDTSUserName.destroy()
       lblDTSPassword.destroy()
       txtDTSPassword.destroy()
       lblDTSCheckPassword.destroy()
       txtDTSCheckPassword.destroy()
       lblUserType.destroy()
       cboUserType.destroy()
       btnUserSave.destroy()
       btnUserDelete.destroy()
       lb.destroy()

def destroyProjects():
       global cboProjects, lblProjects, lblProjectID, txtProjectID,  lblProjectName, txtProjectName, lblProjectDesc, txtProjectDesc,lb
       cboProjects.destroy()
       lblProjects.destroy()
       lblProjectID.destroy()
       txtProjectID.destroy()
       lblProjectName.destroy()
       txtProjectName.destroy()
       lblProjectDesc.destroy()
       txtProjectDesc.destroy()
       btnProjectDisplay.destroy()
       btnProjectSave.destroy()
       btnProjectDelete.destroy()
       lb.destroy()

def destroyIssues():
       global cboProjectID, lblIssueProjectID, lblIssueSeverity, cboIssueSeverity,cboIssueStatus, lblIssueStatus, lb, lblIssueAssignedToID, cboIssueAssignedToID, lblIssueDesc, txtIssueDesc, btnIssueSave,\
       cboIssueAssignedToIDH, cboIssueSeverityH, cboProjectIDH, cboIssueStatusH
       
       lblIssueProjectID.destroy()
       lblIssueSeverity.destroy()
       cboIssueSeverity.destroy()
       lblIssueStatus.destroy()
       cboIssueStatus.destroy()
       lb.destroy()
       lblIssueAssignedToID.destroy()
       cboIssueAssignedToID.destroy()
       lblIssueDesc.destroy()
       txtIssueDesc.destroy()
       btnIssueSave.destroy()
       cboIssueSeverityH.destroy()
       cboProjectIDH.destroy()
       cboIssueStatusH.destroy()
       cboIssueAssignedToIDH.destroy()

def destroySearchIssues():
       global cboProjectID, lblIssueProjectID, lblIssueSeverity, lblIssueStatus, lb, lblIssueAssignedToID, cboIssueAssignedToID, btnIssueSearch,\
       cboIssueSeverity,cboIssueStatus, currentSc, cboIssueAssignedToIDH, cboIssueSeverityH, cboProjectIDH, cboIssueStatusH

       lblIssueProjectID.destroy()
       lblIssueSeverity.destroy()
       cboIssueSeverity.destroy()
       lblIssueStatus.destroy()
       cboIssueStatus.destroy()
       lb.destroy()
       lblIssueAssignedToID.destroy()
       cboIssueAssignedToID.destroy()
       btnIssueSearch.destroy()
       cboIssueSeverityH.destroy()
       cboProjectIDH.destroy()
       cboIssueStatusH.destroy()
       cboIssueAssignedToIDH.destroy()

def destroySearchResults():
       global scroll_y, searchResultsTable
       
       scroll_y.destroy()
       searchResultsTable.destroy()

#Creating Databases and Tables       
def createDatabase():
       cnnDTS = db.connect(host= databaseServer, password=databasePassword,user=databaseUser)
       curDTS= cnnDTS.cursor()
       curDTS.execute("CREATE DATABASE IF NOT EXISTS " + databaseName)
       curDTS.execute("Use "+ databaseName )

       curDTS.execute("create table if not exists dtsUserTypes (userTypeID int primary key,userTypeDesc varchar(30))")
       curDTS.execute("Insert Ignore dtsUserTypes  Set userTypeID = 1, userTypeDesc='Admin'")
       curDTS.execute("Insert Ignore dtsUserTypes  Set userTypeID = 2, userTypeDesc='User'")
       curDTS.execute("create table if not exists dtsUsers (userID int AUTO_INCREMENT primary key,userName varchar(30) UNIQUE,password varchar(30),userTypeID int)")
       curDTS.execute("Insert Ignore dtsUsers  Set userID=1, userName = 'Administrator', password='Password1', userTypeID = 1")
       curDTS.execute("create table if not exists Projects (ProjectID int AUTO_INCREMENT primary key,ProjectName varchar(30) UNIQUE, ProjectDesc varchar(30))")
       curDTS.execute("Insert Ignore Projects  Set ProjectID=1, ProjectName = 'Bookworm',ProjectDesc='Library Management system'")

       curDTS.execute("Create table if not exists Issues(IssueID int AUTO_INCREMENT primary key, CreatorID int, ProjectID int, IssueSeverity int, IssueStatus int, AssignedToID int, IssueDesc varchar(30), Logdate date)")
       curDTS.execute("create table if not exists IssueSeverity (IssueSeverityID int primary key,IssueSeverityDesc varchar(30))")
       curDTS.execute("Insert Ignore IssueSeverity  Set IssueSeverityID = 1, IssueSeverityDesc='Major'")
       curDTS.execute("Insert Ignore IssueSeverity  Set IssueSeverityID = 2, IssueSeverityDesc='Medium'")
       curDTS.execute("Insert Ignore IssueSeverity  Set IssueSeverityID = 3, IssueSeverityDesc='Minor'")
       curDTS.execute("create table if not exists IssueStatus (IssueStatusID int primary key,IssueStatusDesc varchar(30))")
       curDTS.execute("Insert Ignore IssueStatus  Set IssueStatusID = 1, IssueStatusDesc='Open'")
       curDTS.execute("Insert Ignore IssueStatus  Set IssueStatusID = 2, IssueStatusDesc='In Progress'")
       curDTS.execute("Insert Ignore IssueStatus  Set IssueStatusID = 3, IssueStatusDesc='Closed'")
       cnnDTS.commit()

def connectToDatabase():
       cnnDTS = db.connect(host= databaseServer, password=databasePassword,user=databaseUser,database=databaseName)
       return cnnDTS

def getComboBoxData(strsqlquery,defaultValue):
       cnnDTS = connectToDatabase()
       curDTS= cnnDTS.cursor()
       curDTS.execute("Use "+ databaseName )
       curDTS.execute(strsqlquery)
       data = []

       data.append(defaultValue)
       for row in curDTS.fetchall():
              data.append(row[0])

       return data

def clearUserData():
       txtUserID.delete(0,END)
       txtDTSUserName.delete(0,END)
       txtDTSPassword.delete(0,END)
       txtDTSCheckPassword.delete(0,END)
       cboUserType.current(1) 

def clearProjectData():
       txtProjectID.delete(0,END)
       txtProjectName.delete(0,END)
       txtProjectDesc.delete(0,END)

#To get information from the textboxes
def getUser(UserName):
       cnnDTS = connectToDatabase()
       curDTS= cnnDTS.cursor()
       
       strSqlQuery="Select userID,password, userTypeID from dtsUsers WHERE userName  = '" + UserName + "'"
       curDTS.execute(strSqlQuery)
       queryResults=curDTS.fetchall()
       intNumberOfResults = curDTS.rowcount
       
       if intNumberOfResults == 0:
              clearUserData()          
       else:
              txtDTSUserName.insert(0,"Test")   
              Users=DTSUsers(queryResults[0][0], queryResults[0][1], queryResults[0][2])              
              return Users

def getProject(ProjectName):
       cnnDTS = connectToDatabase()
       curDTS= cnnDTS.cursor()
       
       strSqlQuery="Select ProjectID, ProjectDesc from Projects WHERE ProjectName  = '" + ProjectName + "'"
       curDTS.execute(strSqlQuery)
       queryResults=curDTS.fetchall()
       intNumberOfResults = curDTS.rowcount
       
       if intNumberOfResults == 0:
              clearProjectData()          
       else:
              txtProjectName.insert(0,"Test")   
              Project=Projects(queryResults[0][0], queryResults[0][1])              
              return Project
       
def selectedDTSUser():
       global  cboUsers,  txtUserID, txtDTSUserName,  txtDTSPassword,  txtDTSCheckPassword, cboUserType

       strSelectedUser = cboUsers.get()
       objSelectedUser=getUser(strSelectedUser)

       txtUserID["state"] = NORMAL
       txtDTSUserName["state"] = NORMAL
       
       clearUserData()
       
       if (objSelectedUser != None):       
              txtUserID.insert(0,objSelectedUser.userID)
              txtDTSUserName.insert(0,strSelectedUser)       
              txtDTSPassword.insert(0,objSelectedUser.password)
              txtDTSCheckPassword.insert(0,objSelectedUser.password)
              cboUserType.current(objSelectedUser.userTypeID-1)
              txtDTSUserName["state"] = DISABLED

       txtUserID["state"] = DISABLED
        

def selectedProject():
       global  cboProjects,  txtProjectID, txtProjectName, txtProjectDesc

       strSelectedProject = cboProjects.get()
       objSelectedProject=getProject(strSelectedProject)

       txtProjectID["state"] = NORMAL
       txtProjectName["state"] = NORMAL
       
       clearProjectData()
       
       if (objSelectedProject != None):       
              txtProjectID.insert(0,objSelectedProject.ProjectID)
              txtProjectName.insert(0,strSelectedProject)       
              txtProjectDesc.insert(0,objSelectedProject.ProjectDesc)
              txtProjectName["state"] = DISABLED

       txtProjectID["state"] = DISABLED
                      
def modifyDTSUser():
       global  cboUsers,  txtDTSUserName,  txtDTSPassword,  cboUserType
       
       cnnDTS = connectToDatabase()
       curDTS= cnnDTS.cursor()
       
       usertype=2
       if cboUserType.get()=="Administrator":
              usertype=1
       
       if cboUsers.get()=="New User":
              strSqlQuery="Insert into dtsUsers(userName,password,userTypeID) values('"+txtDTSUserName.get() +"','" + txtDTSPassword.get()+"',"+str(usertype)+")"
       else:
              strSqlQuery="update dtsusers set password='"+txtDTSPassword.get() +"', userTypeID=" + str(usertype) + " where username='"+ txtDTSUserName.get()+"'"

       
       curDTS.execute(strSqlQuery) 
       cnnDTS.commit()
       addDtsUsers()

def modifyProject():
       global  cboProjects,  txtProjectName,  txtProjectDesc
       
       cnnDTS = connectToDatabase()
       curDTS= cnnDTS.cursor()
       
       if cboProjects.get()=="New Project":
              strSqlQuery="Insert into Projects(ProjectName,ProjectDesc) values('"+txtProjectName.get() +"','" + txtProjectDesc.get()+"')"
       else:
              strSqlQuery="update Projects set ProjectDesc='"+txtProjectDesc.get()+"'"

       
       curDTS.execute(strSqlQuery) 
       cnnDTS.commit()
       addProjects()

def modifyIssue():
       global cboIssueAssignedToIDH, cboIssueAssignedToID, cboIssueSeverityH, cboProjectIDH, cboIssueStatusH
       
       cboIssueAssignedToIDH.current(cboIssueAssignedToID.current())
       cboIssueSeverityH.current(cboIssueSeverity.current())
       cboProjectIDH.current(cboProjectID.current())
       cboIssueStatusH.current(cboIssueStatus.current())


       cnnDTS = connectToDatabase()
       curDTS= cnnDTS.cursor()

       strSqlQuery="Insert into Issues(CreatorID, ProjectID, IssueSeverity, IssueStatus, AssignedToID, IssueDesc, Logdate) values("+str(loggedInUserID) +"," + cboProjectIDH.get()+","+cboIssueSeverityH.get()+","+cboIssueStatusH.get()+","+cboIssueAssignedToIDH.get()+",'"+txtIssueDesc.get()+"',"+"curdate())"      
       
       curDTS.execute(strSqlQuery) 
       cnnDTS.commit()
       logIssues()

def searchIssue():
       global cboIssueAssignedToIDH, cboIssueAssignedToID, cboIssueSeverityH, cboProjectIDH, cboIssueStatusH
       
       cboIssueAssignedToIDH.current(cboIssueAssignedToID.current())
       cboIssueSeverityH.current(cboIssueSeverity.current())
       cboProjectIDH.current(cboProjectID.current())
       cboIssueStatusH.current(cboIssueStatus.current())
       
       strSqlQuery="Select issues.IssueID, issues.IssueDesc, issues.Logdate from issues Inner Join projects on issues.ProjectID = projects.ProjectID Inner Join issueseverity on issues.IssueSeverity = issueseverity.IssueSeverityID Inner Join issuestatus on issues.IssueStatus = issuestatus.IssueStatusID Inner Join dtsusers on issues.AssignedToID = dtsusers.userID Where issues.ProjectID = " + cboProjectIDH.get() + " and issues.IssueSeverity = "+cboIssueSeverityH.get() + " and issues.IssueStatus = " +cboIssueStatusH.get() + " and issues.AssignedToID = "+ cboIssueAssignedToIDH.get()
       searchResults(strSqlQuery)
def deleteDTSUser():
       global  txtDTSUserName
       cnnDTS = connectToDatabase()
       curDTS= cnnDTS.cursor()
       strSqlQuery="delete from dtsusers where username='"+ txtDTSUserName.get()+"'"
       curDTS.execute(strSqlQuery)
       cnnDTS.commit()
       addDtsUsers()

def deleteProject():
       global  txtProjectName
       cnnDTS = connectToDatabase()
       curDTS= cnnDTS.cursor()
       strSqlQuery="delete from Projects where ProjectName='"+ txtProjectName.get()+"'"
       curDTS.execute(strSqlQuery)
       cnnDTS.commit()
       addProjects()
    
def gettingLoginDetails():       
       global txtUserName,txtPassword,strQuery,loggedInUserID

       cnnDTS = connectToDatabase()
       curDTS= cnnDTS.cursor()
       
       strUserName = txtUserName.get()
       strPassword = txtPassword.get()       
       strQuery = "select userTypeID,userID from dtsUsers where userName='" + strUserName + "' and password = '"+ strPassword + "'"
       
       curDTS.execute(strQuery)
       queryResults=curDTS.fetchall()
       intNumberOfResults = curDTS.rowcount

       intUserTypeID = -1
       if intNumberOfResults == 0:
              messagebox.showinfo("Failure","Invalid Login")
       else:
               intUserTypeID =  queryResults[0][0]
               loggedInUserID=queryResults[0][1]
               loginsc.destroy()
               Menu(intUserTypeID)       

#Login Screen
def login():
       global lblUserfName,txtUserName,lblPassword,txtPassword, loginsc
       loginsc = Tk()
       loginsc.title("Defect tracking system")
       loginsc.state("zoomed")
       loginsc.configure(bg='LightSalmon1')

       lbname=Label(loginsc,text='Defect Tracking System',font=('Avenir Next LT Pro Light', 50,'bold'),bg='LightSalmon1')
       lbname.place(relx=0.25, rely=0.2)

       lblUserfName = Label(loginsc,text='User Name:',font=('arial', 20,'bold'),bg='LightSalmon1')
       lblUserfName.place(relx=0.35, rely=0.4)

       txtUserName=Entry(loginsc, font=('arial', 20,'bold'))
       txtUserName.place(relx=0.48, rely=0.4, relwidth=0.15)

       lblPassword=Label(loginsc,text='Password:',font=('arial', 20,'bold'),bg='LightSalmon1')
       lblPassword.place(relx=0.35, rely=0.50)

       txtPassword=Entry(loginsc, font=('arial', 20,'bold'),show="\u2023")
       txtPassword.place(relx=0.48, rely=0.50, relwidth=0.15)

       btnLogin = Button(loginsc,text="LOGIN",  font=("arial",20,'bold'),command=gettingLoginDetails,bg='black',fg='white')
       btnLogin.place(relx=0.38,rely=0.65, relwidth=0.1)

       #Credits
       strDeveloper = "Done by:Mridula Prasad"
       lblDeveloper = Label(loginsc,text=strDeveloper,font=('Bahnschrift', 12,'bold'),bg='LightSalmon1')
       lblDeveloper.place(relx=0.80, rely=0.97)

#Menu Screen
def Menu(intUserTypeID):
    global btnProjects,btnDtsUsers,btnLogIssues ,btnSearchIssues,btnReports,menuSC,headingFrame,moduleFrame,headingLabel,heading,dFrame,displayFrame
    menuSC = Tk()
    menuSC.title("Defects tracking system")
    menuSC.state("zoomed")
    menuSC.configure(bg=mygbcolor)
    
    headingFrame = Frame(menuSC,bd=40, relief=RIDGE,bg=mygbcolor)
    headingFrame.place(relx=0,rely=0,relwidth=1,relheight=0.2)
    heading=Label(headingFrame,font=('Calibri', 40, 'italic'), text="Welcome to Defects Tracking System",bg=mygbcolor)
    heading.place(relx=0, rely=0.2)
    moduleFrame = Frame(menuSC,bd=20, relief=RIDGE,bg=mygbcolor)
    moduleFrame.place(relx=0,rely=0.2,relwidth=0.2,relheight=0.8)
    headingLabel = Label(moduleFrame, text="MENU",font=("Calibri",26,'bold'),bg=mygbcolor)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=0.15)
    dFrame= Frame(menuSC,bd=20, relief=RIDGE,bg=mygbcolor)
    dFrame.place(relx=0.2,rely=0.2,relwidth=0.8,relheight=0.8)
    displayFrame=Frame(dFrame, bd=10, relief=RIDGE,bg='white')
    displayFrame.place(relx=0.2,rely=0.05, relwidth=0.6, relheight=0.9)
    
    btnLogIssues = Button(moduleFrame,text="Log Issues",font=("Calibri",12,'bold'), compound= LEFT, command=logIssues,bg='black',fg='white')
    btnLogIssues .place(relx=0, rely=0.17, relwidth=1,relheight=0.12)
    
    btnSearchIssues = Button(moduleFrame,text="Search Issues",font=("Calibri",12,'bold'), compound= LEFT, command=searchIssues,bg='black',fg='white')
    btnSearchIssues.place(relx=0,rely=0.31, relwidth=1,relheight=0.12)

    if (intUserTypeID == 1):
           btnProjects = Button(moduleFrame,text="Projects",font=("Calibri",12,'bold'),compound = LEFT, command=addProjects,bg='black',fg='white')
           btnProjects.place(relx=0,rely=0.44, relwidth=1,relheight=0.12)
           
           btnDtsUsers = Button(moduleFrame,text="DTS Users",font=("Calibri",12,'bold'), compound= LEFT, command=addDtsUsers,bg='black',fg='white')
           btnDtsUsers.place(relx=0,rely=0.58, relwidth=1,relheight=0.12)

    logoutBtn=Button(headingFrame, text="LOGOUT", font=('Calibri',10,'bold'), command=menuSC.destroy,bg='black',fg='white')
    logoutBtn.place(relx=0.87, rely=0.7, relwidth=0.1)

#Projects Function
def addProjects():

    global cboProjects, lblProjects, lblProjectID, txtProjectID, lblProjectName, txtProjectName, lblProjectDesc,\
    txtProjectDesc, currentSc,btnProjectDisplay,btnProjectSave, btnProjectDelete,lb
    destroySc()
    currentSc=1
    
    lb=Label(displayFrame,text='Projects',font=("Times New Roman",26,'bold'),bg='white')
    lb.place(relx=0.34,rely=0)

   #Combo-box
    lblProjects = Label(displayFrame,text="Projects : ",font=("arial",12,'bold'),bg='white')
    lblProjects.place(relx=0.05,rely=0.2)

    cboProjects=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboProjects['value']=getComboBoxData("Select ProjectName from Projects","New Project")
    cboProjects.current(0)
    cboProjects.place(relx=0.3,rely=0.2,relwidth=0.30)

    # Project ID
    lblProjectID = Label(displayFrame,text="Project ID : ",font=("arial",12,'bold'),bg='white')
    lblProjectID.place(relx=0.05,rely=0.3)
    txtProjectID = Entry(displayFrame,font=("arial",12,'bold'),bg='White')
    txtProjectID .place(relx=0.3,rely=0.3, relwidth=0.62)

    # Project Name
    lblProjectName = Label(displayFrame,text="Project Name : ",font=("arial",12,'bold'),bg='white')
    lblProjectName.place(relx=0.05,rely=0.4)
    txtProjectName = Entry(displayFrame,font=("arial",12,'bold'),bg='White')
    txtProjectName.place(relx=0.3,rely=0.4, relwidth=0.62)

    # Project Description
    lblProjectDesc = Label(displayFrame,text="Project Desc : ",font=("arial",12,'bold'),bg='white')
    lblProjectDesc.place(relx=0.05,rely=0.5)
    txtProjectDesc = Entry(displayFrame,font=("arial",12,'bold'),bg='White')
    txtProjectDesc.place(relx=0.3,rely=0.5, relwidth=0.62)

    btnProjectDisplay=Button(displayFrame, text="Display", font=('Calibri',10,'bold'), command=selectedProject,bg='black',fg='white')
    btnProjectDisplay.place(relx=0.7, rely=0.2, relwidth=0.15)

    btnProjectSave=Button(displayFrame, text="Save", font=('Calibri',10,'bold'), command=modifyProject,bg='black',fg='white')
    btnProjectSave.place(relx=0.3, rely=0.7, relwidth=0.15)

    btnProjectDelete=Button(displayFrame, text="Delete", font=('Calibri',10,'bold'), command=deleteProject,bg='black',fg='white')
    btnProjectDelete.place(relx=0.6, rely=0.7, relwidth=0.15)

#DTS Users Function
def addDtsUsers():
    
    global lblUsers, cboUsers,  btnUserDisplay, lblUserID, txtUserID, lblDTSUserName, txtDTSUserName,\
    lblDTSPassword, txtDTSPassword, lblDTSCheckPassword, txtDTSCheckPassword, lblUserType, cboUserType,\
    currentSc,btnUserSave, btnUserDelete,lb

    destroySc()
    currentSc=2
    
    lb=Label(displayFrame,text='DTS User',font=("Times New Roman",26,'bold'),bg='white')
    lb.place(relx=0.34,rely=0)

   #Combo-box
    lblUsers = Label(displayFrame,text="DTS Users : ",font=("arial",12,'bold'),bg='white')
    lblUsers.place(relx=0.05,rely=0.1)

    cboUsers=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboUsers['value']=getComboBoxData("Select userName from dtsUsers","New User")
    cboUsers.current(0)
    cboUsers.place(relx=0.3,rely=0.1,relwidth=0.30)

    btnUserDisplay=Button(displayFrame, text="Display", font=('Calibri',10,'bold'), command=selectedDTSUser,bg='black',fg='white')
    btnUserDisplay.place(relx=0.7, rely=0.1, relwidth=0.15)

    btnUserSave=Button(displayFrame, text="Save", font=('Calibri',10,'bold'), command=modifyDTSUser,bg='black',fg='white')
    btnUserSave.place(relx=0.3, rely=0.7, relwidth=0.15)

    btnUserDelete=Button(displayFrame, text="Delete", font=('Calibri',10,'bold'), command=deleteDTSUser,bg='black',fg='white')
    btnUserDelete.place(relx=0.6, rely=0.7, relwidth=0.15)


    # User ID
    lblUserID = Label(displayFrame,text="User ID : ",font=("arial",12,'bold'),bg='white')
    lblUserID.place(relx=0.05,rely=0.2)
    txtUserID = Entry(displayFrame,font=("arial",12,'bold'),bg='White')
    txtUserID .place(relx=0.3,rely=0.2, relwidth=0.62)

    # User Name
    lblDTSUserName = Label(displayFrame,text="User Name : ",font=("arial",12,'bold'),bg='white')
    lblDTSUserName.place(relx=0.05,rely=0.3)
    txtDTSUserName = Entry(displayFrame,font=("arial",12,'bold'),bg='White')
    txtDTSUserName.place(relx=0.3,rely=0.3, relwidth=0.62)

     # Password
    lblDTSPassword = Label(displayFrame,text="Password : ",font=("arial",12,'bold'),bg='white')
    lblDTSPassword.place(relx=0.05,rely=0.4)
    txtDTSPassword = Entry(displayFrame,font=("arial",12,'bold'),bg='White',show="\u2023")
    txtDTSPassword.place(relx=0.3,rely=0.4, relwidth=0.62)

   # Check Password
    lblDTSCheckPassword = Label(displayFrame,text="Check Password : ",font=("arial",12,'bold'),bg='white')
    lblDTSCheckPassword.place(relx=0.05,rely=0.5)
    txtDTSCheckPassword = Entry(displayFrame,font=("arial",12,'bold'),bg='White',show="\u2023")
    txtDTSCheckPassword.place(relx=0.3,rely=0.5, relwidth=0.62)

    #UserType ID
    lblUserType = Label(displayFrame,text="UserType ID : ",font=("arial",12,'bold'),bg='white')
    lblUserType.place(relx=0.05,rely=0.6)

    cboUserType=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=23)
    cboUserType['value']=('Administrator' ,'User')
    cboUserType.current(1)
    cboUserType.place(relx=0.3,rely=0.6,relwidth=0.62)

#Log issues function
def logIssues():
    global cboProjectID, lblIssueProjectID, lblIssueSeverity, lblIssueStatus, lb, lblIssueAssignedToID, cboIssueAssignedToID, lblIssueDesc, txtIssueDesc, btnIssueSave,\
           cboIssueSeverity,cboIssueStatus, currentSc, cboIssueAssignedToIDH, cboIssueSeverityH, cboProjectIDH, cboIssueStatusH
    destroySc()
    currentSc=3
    
    lb=Label(displayFrame,text='Issues',font=("Times New Roman",26,'bold'),bg='white')
    lb.place(relx=0.34,rely=0)

   #Project ID Combo-box
    lblIssueProjectID = Label(displayFrame,text="Project ID : ",font=("arial",12,'bold'),bg='white')
    lblIssueProjectID.place(relx=0.05,rely=0.2)

    cboProjectIDH=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboProjectIDH['value']=getComboBoxData("Select ProjectID from projects order by ProjectName","")
    cboProjectIDH.current(0)
    cboProjectIDH.place(relx=0.3,rely=0.2,relwidth=0.30)

    cboProjectID=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboProjectID['value']=getComboBoxData("Select ProjectName from projects order by ProjectName","")
    cboProjectID.current(0)
    cboProjectID.place(relx=0.3,rely=0.2,relwidth=0.30)

    # Issue Severity
    lblIssueSeverity = Label(displayFrame,text="Issue Severity : ",font=("arial",12,'bold'),bg='white')
    lblIssueSeverity.place(relx=0.05,rely=0.3)

    cboIssueSeverityH=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboIssueSeverityH['value']=getComboBoxData("Select IssueSeverityID from IssueSeverity","")
    cboIssueSeverityH.current(0)
    cboIssueSeverityH.place(relx=0.3,rely=0.5,relwidth=0.30)

    cboIssueSeverity=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboIssueSeverity['value']=getComboBoxData("Select IssueSeverityDesc from IssueSeverity","")
    cboIssueSeverity.current(0)
    cboIssueSeverity.place(relx=0.3,rely=0.3,relwidth=0.30)

    # Issue Status
    lblIssueStatus = Label(displayFrame,text="Issue Status : ",font=("arial",12,'bold'),bg='white')
    lblIssueStatus.place(relx=0.05,rely=0.4)

    cboIssueStatusH=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboIssueStatusH['value']=getComboBoxData("Select IssueStatusID from IssueStatus","")
    cboIssueStatusH.current(0)
    cboIssueStatusH.place(relx=0.3,rely=0.4,relwidth=0.30)
    
    cboIssueStatus=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboIssueStatus['value']=getComboBoxData("Select IssueStatusDesc from IssueStatus","")
    cboIssueStatus.current(0)
    cboIssueStatus.place(relx=0.3,rely=0.4,relwidth=0.30)

    # Issue Assigned to ID
    lblIssueAssignedToID = Label(displayFrame,text="Assigned To : ",font=("arial",12,'bold'),bg='white')
    lblIssueAssignedToID.place(relx=0.05,rely=0.5)
    
    cboIssueAssignedToIDH=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboIssueAssignedToIDH['value']=getComboBoxData("Select UserID from dtsusers  order by UserName","")
    cboIssueAssignedToIDH.current(0)
    cboIssueAssignedToIDH.place(relx=0.3,rely=0.5,relwidth=0.30)

    cboIssueAssignedToID=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboIssueAssignedToID['value']=getComboBoxData("Select UserName from dtsusers order by UserName","")
    cboIssueAssignedToID.current(0)
    cboIssueAssignedToID.place(relx=0.3,rely=0.5,relwidth=0.30)

    # Issue Description
    lblIssueDesc = Label(displayFrame,text="Issue Desc : ",font=("arial",12,'bold'),bg='white')
    lblIssueDesc.place(relx=0.05,rely=0.6)
    txtIssueDesc = Entry(displayFrame,font=("arial",12,'bold'),bg='White')
    txtIssueDesc.place(relx=0.3,rely=0.6, relwidth=0.62)

    btnIssueSave=Button(displayFrame, text="Save", font=('Calibri',10,'bold'), command=modifyIssue,bg='black',fg='white')
    btnIssueSave.place(relx=0.3, rely=0.7, relwidth=0.15)


def searchResults(sqlQuery):
       global scroll_y, searchResultsTable,num,headingLabel, currentSc
       destroySc()
       currentSc=5

       scroll_y=Scrollbar(displayFrame,orient=VERTICAL)
       searchResultsTable=ttk.Treeview(displayFrame,columns=("IssueID","IssueDesc","Logdate"),yscrollcommand=scroll_y.set)
       scroll_y.pack(side=RIGHT, fill=Y)

       scroll_y.config(command=searchResultsTable.yview)
       searchResultsTable.heading("IssueID",text="Issue ID")
       searchResultsTable.heading("IssueDesc",text="Issue Description")
       searchResultsTable.heading("Logdate",text="Log Date")
       searchResultsTable["show"]="headings"
       searchResultsTable.column("IssueID",width=50)
       searchResultsTable.column("IssueDesc",width=50)
       searchResultsTable.column("Logdate",width=50)
       searchResultsTable.pack(fill=BOTH,expand=1)
       
       cnnDTS = connectToDatabase()
       curDTS= cnnDTS.cursor()
       curDTS.execute(sqlQuery)
       rows=curDTS.fetchall()
       
       for row in rows:
              searchResultsTable.insert('',END,values=row)


#Search Issues Function    
def searchIssues():
    global cboProjectID, lblIssueProjectID, lblIssueSeverity, lblIssueStatus, lb, lblIssueAssignedToID, cboIssueAssignedToID, btnIssueSearch,\
           cboIssueSeverity,cboIssueStatus, currentSc, cboIssueAssignedToIDH, cboIssueSeverityH, cboProjectIDH, cboIssueStatusH,scroll_y, searchResultsTable
    destroySc()
    currentSc=4
    
    lb=Label(displayFrame,text='Search Issues',font=("Times New Roman",26,'bold'),bg='white')
    lb.place(relx=0.34,rely=0)

   #Project ID Combo-box
    lblIssueProjectID = Label(displayFrame,text="Project ID : ",font=("arial",12,'bold'),bg='white')
    lblIssueProjectID.place(relx=0.05,rely=0.2)

    cboProjectIDH=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboProjectIDH['value']=getComboBoxData("Select ProjectID from projects order by ProjectName","")
    cboProjectIDH.current(0)
    cboProjectIDH.place(relx=0.3,rely=0.2,relwidth=0.30)

    cboProjectID=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboProjectID['value']=getComboBoxData("Select ProjectName from projects order by ProjectName","")
    cboProjectID.current(0)
    cboProjectID.place(relx=0.3,rely=0.2,relwidth=0.30)

    # Issue Severity
    lblIssueSeverity = Label(displayFrame,text="Issue Severity : ",font=("arial",12,'bold'),bg='white')
    lblIssueSeverity.place(relx=0.05,rely=0.3)

    cboIssueSeverityH=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboIssueSeverityH['value']=getComboBoxData("Select IssueSeverityID from IssueSeverity","")
    cboIssueSeverityH.current(0)
    cboIssueSeverityH.place(relx=0.3,rely=0.5,relwidth=0.30)

    cboIssueSeverity=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboIssueSeverity['value']=getComboBoxData("Select IssueSeverityDesc from IssueSeverity","")
    cboIssueSeverity.current(0)
    cboIssueSeverity.place(relx=0.3,rely=0.3,relwidth=0.30)

    # Issue Status
    lblIssueStatus = Label(displayFrame,text="Issue Status : ",font=("arial",12,'bold'),bg='white')
    lblIssueStatus.place(relx=0.05,rely=0.4)

    cboIssueStatusH=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboIssueStatusH['value']=getComboBoxData("Select IssueStatusID from IssueStatus","")
    cboIssueStatusH.current(0)
    cboIssueStatusH.place(relx=0.3,rely=0.4,relwidth=0.30)
    
    cboIssueStatus=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboIssueStatus['value']=getComboBoxData("Select IssueStatusDesc from IssueStatus","")
    cboIssueStatus.current(0)
    cboIssueStatus.place(relx=0.3,rely=0.4,relwidth=0.30)

    # Issue Assigned to ID
    lblIssueAssignedToID = Label(displayFrame,text="Assigned To : ",font=("arial",12,'bold'),bg='white')
    lblIssueAssignedToID.place(relx=0.05,rely=0.5)
    
    cboIssueAssignedToIDH=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboIssueAssignedToIDH['value']=getComboBoxData("Select UserID from dtsusers  order by UserName","")
    cboIssueAssignedToIDH.current(0)
    cboIssueAssignedToIDH.place(relx=0.3,rely=0.5,relwidth=0.30)

    cboIssueAssignedToID=ttk.Combobox(displayFrame, font=('arial', 12, 'bold'), state='readonly', width=15)
    cboIssueAssignedToID['value']=getComboBoxData("Select UserName from dtsusers order by UserName","")
    cboIssueAssignedToID.current(0)
    cboIssueAssignedToID.place(relx=0.3,rely=0.5,relwidth=0.30)


    btnIssueSearch=Button(displayFrame, text="Search", font=('Calibri',10,'bold'), command=searchIssue,bg='black',fg='white')
    btnIssueSearch.place(relx=0.3, rely=0.7, relwidth=0.15)

createDatabase()
login()
