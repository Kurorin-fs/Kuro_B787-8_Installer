from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
import zipfile
import shutil
import sys
import tkinter as tk
import re
import glob
import logging

version = "v1.1.2"
logging.basicConfig(level=logging.DEBUG, filename="..\installer.log", format="%(asctime)s %(levelname)s: %(funcName)s: %(message)s")

#icon
root = tk.Tk()
root.withdraw()
data = '''R0lGODlhgACAAOfJAABZnwBbnQtZlwBkoBJfnBNjmhlioCBilCdjnB5ooCtmnyRo
pzNmmippmzJplzFqpCpsqyhvpzlrnx1zqzVtpydypDJvojxtojB0rTdzpzh0qCt4
qjx2pCp7szJ6rDZ5sj14rCGCuUZ6qTh+sTCAuD59qi2CszuBtEx9pj2BrjKFtzaE
vFV+ozyGskCFuUiHrzqLvVqDqDaNuEKLuFmFsjWTxE+Muz6TvkGTx1KPviyaylCS
umWOsz+ZvlqRuj2Zy02VwjmbxVeTtmOQu0WZxS6gyVyUvTWfz0OdwmSUtT6fynGS
rS2lx0Oe0EqdyT2jxy2n1jin0D2l1nKYslifwESkz2Gdv0ujyXSYu1Kjwy2t1Uem
0TWs3EKtykCt1lqmzTyv0kes0FeoyEur1zez2z2x4UWw2n+hvE2w1Fqt0zu23y67
4nenyUq03kW22UO25XKqx3SrwkG64nGt0Fe04Em53DW/51q221u31ZKowEW95ijG
7FO72ULA4k694Gq13D3D3We31yTL6knA6FG/4j7F7Y6wy0fE5ne31DvJ6V6/5Jew
x07E7UrG6FXD5j7L7ETJ8UDM34+2ykHM5k3J60/K7FXJ5VvI3m7D3Ym+1njD3WrI
3HrF2WXL6aG8zZXA2njI6JnA1Ki8zmbP4pHE3ZTE1ojJ5X7N42rW4KPH1prK3bbC
1oDT65XP4rTH147U6sXHxJTW5r7M06DU7bbS48jQ2LrU3sHS3s3QzLDY7KPd7sjX
3s7W3rLf7MDb6rre7bze59bY1cnb59rc2bjl8s7f7L/k8sji7OHc2tne4dze293g
3N3i5ODi373r+Mfp67/r8tbl69Dn7M7o8svt9uDn8OXn5NHt6tvq8d3q69Pt+OXp
7Ofp5uro7Nfu8u/q6d/u9ers6db1+e7w7d71+uX0++j19fHz8Oz0/Of2/fL0+PP2
8uP6/+z5+vX49Pb59uj9/Pb7/vD9/fn7+P36///6 +fr8+fL/+fP///X/+v/8+/7+
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
i7RYi7ZIFAEBADs=
     ''' 
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(data=data))

#zip Path
pydir = os.getcwd()
zippath = os.path.join(os.getcwd(), 'main.zip')
patchpath = os.path.join(os.getcwd(), 'xml.zip')
HDpatchpath = os.path.join(os.getcwd(), 'newHD.zip')
cfgpath = os.path.join(os.getcwd(), "livery-cfgs")
logging.debug("path ok")
#check if lists exist
oldlistpath = os.path.join(os.getcwd(), 'old.list')
newlistpath = os.path.join(os.getcwd(), 'new.list')
logging.debug("list ok")
if not os.path.exists(oldlistpath) or not os.path.exists(newlistpath):
    logging.error("Required Installer Components(old.list or new.list) not found. Download and Extract the installer again.")
    messagebox.showerror("Kuro_B787-8 Installer - Installation Failed", "Required Installer Components(old.list or new.list) not found. \n\nDownload and Extract the installer again.")
    sys.exit()

#read list
oldlist = "old.list"
newlist = "new.list"
with open(oldlist, "r", encoding="utf-8") as oldlistT:
	oldjs = oldlistT.read().splitlines()
with open(newlist, "r", encoding="utf-8") as newlistT:
	newjs = newlistT.read ().splitlines()
oldjs = [item.replace('\\n', '\n') for item in oldjs]
newjs = [item.replace('\\n', '\n') for item in newjs]
logging.debug("read list")
#Intro
def intro():
    logging.debug("Intro")
    print("\nThis program is the installer/updater of Kuro_B787-8 for Microsoft Flight Simulator.    Creator:Kurorin(@kuro_x#4595)\nRequired Contents : MSFS Premium Delux Version, HeavyDivision's B78XH(any version)")
    messagebox.showinfo("Kuro_B787-8 Installer " + version, "This program is the installer/updater of Kuro_B787-8 for Microsoft Flight Simulator.\n\nRequired Contents :\nMSFS Premium Delux Version,\nHeavyDivision's B78XH(any version)\n\nCreator : Kurorin(@kuro_x#4595)\nhttps://flightsim.to/profile/Kurorin\n\nPress OK to Continue")
#lines open Usercfg.opt
def OpenOpt():
    f = open('usercfg.opt', 'r') 
    alltxt = f.readlines()
    f.close()
    MSFSpathL = len(alltxt) 
    MSFSpathF  = alltxt[MSFSpathL-1].strip()
    MSFSpathH = MSFSpathF.replace('InstalledPackagesPath ', '') 
    MSFSpath=MSFSpathH.strip('"')
    return MSFSpath
    logging.info("MSFSpath =" + MSFSpath)

def AskCom():
    #MS Store Path
    USERCFGpathM = os.path.join((os.environ['USERPROFILE']), 'AppData\Local\Packages\Microsoft.FlightSimulator_8wekyb3d8bbwe\LocalCache')
    #Steam Path
    USERCFGpathS = os.path.join((os.environ['USERPROFILE']), 'AppData\Roaming\Microsoft Flight Simulator')
    if os.path.exists(os.path.join(USERCFGpathM, 'usercfg.opt')):
        os.chdir(USERCFGpathM)
        MSFSpath = OpenOpt()
    elif os.path.exists(os.path.join(USERCFGpathS, 'usercfg.opt')):
        os.chdir(USERCFGpathS)
        MSFSpath = OpenOpt()
    else:
        MSFSpath = os.environ['USERPROFILE']
    #ask users where Community is
    Community = filedialog.askdirectory(initialdir = MSFSpath, title='Kuro_B787-8 Installer - >>>Select Community Folder<<<') 
    logging.info("Community Path = " + Community)
    print("Community Path = " + Community)
    return Community

#open config
with open(os.path.join(pydir, 'installer.cfg'), mode='r', encoding='utf-8') as config:
    configL = config.read().splitlines()
    if configL:
        Community = configL[0]
        logging.debug("read Community from cfg")
    else:
        Community = ""
        intro()

#com written in cfg or not
if Community == "" or not os.path.exists(Community): 
    #message
    print("Select your MSFS Community folder in the next pop-up")
    messagebox.showinfo("Kuro_B787-8 Installer", "Select your MSFS Community folder in the next pop-up")
    #write config
    Community = AskCom()
    with open(os.path.join(pydir, 'installer.cfg'), mode='w', encoding='utf-8') as config:
        config.write(Community)
        logging.debug("set Community (1)")


#menu
def info():
    messagebox.showinfo("Kuro_B787-8 Installer " + version, "This program is the installer/updater of Kuro_B787-8 for Microsoft Flight Simulator.\n\nRequired Contents :\nMSFS Premium Delux Version,\nHeavyDivision's B78XH(any version)\n\nCreator : Kurorin(@kuro_x#4595)\nhttps://flightsim.to/profile/Kurorin")
    logging.debug("Info")
def AskCom0(entry1, sub_set, pydir):
    sub_set.attributes("-topmost", False)
    Community = AskCom()
    if not Community =="":
        entry1.set(Community)
        logging.debug("Ask Community")
        with open(os.path.join(pydir, 'installer.cfg'), mode='w', encoding='utf-8') as config:
            config.write(Community)
            logging.info("write Community to cfg")
    sub_set.attributes("-topmost", True)
def closesettngs(entry1, sub_set):
    sub_set.destroy()
    com.set(entry1.get())
    logging.debug("override Community from entry1")
    if not com =="":
        with open(os.path.join(pydir, 'installer.cfg'), mode='w', encoding='utf-8') as config:
            config.write(com.get())
def settings(com, Commnuity, root):
    logging.debug("Settings")
    sub_set = tk.Toplevel()
    lw1 = 300
    lh1 = 100
    sub_set.geometry(str(lw1)+"x"+str(lh1)+"+"+str(int(ww/2-lw1/2))+"+"+str(int(wh/2-lh1/2)) )
    sub_set.protocol('WM_DELETE_WINDOW', lambda:closesettngs(entry1, sub_set))
    sub_set.tk.call('wm', 'iconphoto', sub_set._w, tk.PhotoImage(data=data))
    sub_set.resizable(0,0)
    sub_set.transient(root)
    sub_set.attributes("-topmost", True)
    sub_set.lift()
    sub_set.focus_force()
    sub_set.grab_set()
    entry1 = tk.StringVar()
    entry1.set(com.get())
    label_sub = tk.Label(sub_set, text="Communty Path :")
    label_sub.place(relx = 0.5, rely = 0.2, relwidth = 0.9, anchor = tk.CENTER)
    IDirEntry = ttk.Entry(sub_set, textvariable=entry1)
    IDirEntry.place(relx = 0.4, rely = 0.45, relwidth = 0.7, anchor = tk.CENTER)
    IDirButton = ttk.Button(sub_set, text="Select", command=lambda:AskCom0(entry1, sub_set, pydir))
    IDirButton.place(relx = 0.85, rely = 0.45, relwidth = 0.2, anchor = tk.CENTER)
    IDirButton1 = ttk.Button(sub_set, text="Close", command=lambda:closesettngs(entry1, sub_set))
    IDirButton1.place(relx = 0.85, rely = 0.75, relwidth = 0.2, anchor = tk.CENTER)
    '''
    #combo
    logOpt = ["DEBUG", "INFO"]
    logTex = tk.StringVar()
    label_comb = tk.Label(sub_set, text="Log Level :")
    label_comb.place(relx = 0.15, rely = 0.75, relwidth = 0.3, anchor = tk.CENTER)
    combobox = ttk.Combobox(sub_set, values = logOpt, textvariable = logTex)
    combobox.set("DEBUG")
    combobox.place(relx = 0.35, rely = 0.75, relwidth = 0.2, anchor = tk.CENTER)
    '''
def install(com):
    logging.debug("Install")
    with open(os.path.join(pydir, 'installer.cfg'), mode='r', encoding='utf-8') as config:
        configL = config.read().splitlines()
        if configL and os.path.exists(configL[0]):
            Community = configL[0]
            com.set(Community)
        else:
            Community = AskCom()
            with open(os.path.join(pydir, 'installer.cfg'), mode='w', encoding='utf-8') as config:
                config.write(Community)
            com.set(Community)
    if not Community:
        return
    ComInfo = SetCom(Community)
    if not ComInfo:
        return
    HDname = ComInfo[0]
    HDPath = ComInfo[1]
    isHDB78XHnew = ComInfo[2]
    isInstallperformed = check788exist(Community, zippath)
    if not isInstallperformed:
        logging.error("Installation canceled")
        print("Installation canceled")
        return
    PatchnewHD(isHDB78XHnew, HDpatchpath, Community)
    engAnim(Community, HDname, patchpath)
    fmcUpdate(HDPath, Community, isHDB78XHnew)
    checklivery(isHDB78XHnew, Community, cfgpath)
    endI()
def update(com):
    logging.debug("Update")
    with open(os.path.join(pydir, 'installer.cfg'), mode='r', encoding='utf-8') as config:
        configL = config.read().splitlines()
        if configL and os.path.exists(configL[0]):
            Community = configL[0]
            com.set(Community)
        else:
            Community = AskCom()
            with open(os.path.join(pydir, 'installer.cfg'), mode='w', encoding='utf-8') as config:
                config.write(Community)
            com.set(Community)
    if not Community:
        return
    ComInfo = SetCom(Community)
    if not ComInfo:
        return
    HDname = ComInfo[0]
    HDPath = ComInfo[1]
    isHDB78XHnew = ComInfo[2]
    is788installed = fmcUpdate(HDPath, Community, isHDB78XHnew)
    if not is788installed:
        logging.error("Update canceled")
        print("Update canceled")
        return
    endF()
def livery(com, cfgpath):
    logging.debug("livery")
    with open(os.path.join(pydir, 'installer.cfg'), mode='r', encoding='utf-8') as config:
        configL = config.read().splitlines()
        if configL and os.path.exists(configL[0]):
            Community = configL[0]
            com.set(Community)
        else:
            Community = AskCom()
            with open(os.path.join(pydir, 'installer.cfg'), mode='w', encoding='utf-8') as config:
                config.write(Community)
            com.set(Community)
    if not Community:
        return
    ComInfo = SetCom(Community)
    if not ComInfo:
        return
    HDname = ComInfo[0]
    HDPath = ComInfo[1]
    isHDB78XHnew = ComInfo[2]
    if not isHDB78XHnew:
        logging.warning("Installed B78XH is not separeted one.")
        print("Installed B78XH is not separeted one. No need to convert liveries.")
        messagebox.showwarning("Kuro_B787-8 Installer ", "The installed B78XH is not the one separeted from the Default B787-10.  No need to convert liveries.")
        return
    else:
        isLivConverted = liveryconv(Community, cfgpath)
        if not isLivConverted:
            return
        else:
            endL()
        
def close():
    logging.debug("close")
    sys.exit()

logging.debug("root")
root.title("Kuro_B787-8 Installer " + version)
root.update_idletasks()
ww = root.winfo_screenwidth()
wh = root.winfo_screenheight()
lw = 320
lh = 150
root.geometry(str(lw)+"x"+str(lh)+"+"+str(int(ww/2-lw/2))+"+"+str(int(wh/2-lh/2)) )
root.resizable(0,0)
com = tk.StringVar()
com.set(Community)
men = tk.Menu(root) 
root.config(menu=men)
root.deiconify()
menu_file1 = tk.Menu(root, tearoff=0)
menu_file2 = tk.Menu(root, tearoff=0)
men.add_cascade(label='Settings', menu=menu_file1) 
menu_file1.add_command(label='Settings', command=lambda:settings(com, Community, root)) 
menu_file1.add_separator() 
menu_file1.add_command(label='Close', command=close)
men.add_cascade(label='Info', menu=menu_file2) 
menu_file2.add_command(label='Info', command=info)
button1 = ttk.Button(root, text="Install/Update B787-8", command=lambda:install(com))
button1.place(relx = 0.5, rely = 0.2, relwidth = 0.8, anchor = tk.CENTER)
button2 = ttk.Button(root, text="Update Only FMC files", command=lambda:update(com))
button2.place(relx = 0.5, rely = 0.4, relwidth = 0.8, anchor = tk.CENTER)
button3 = ttk.Button(root, text="Convert Livery", command=lambda:livery(com, cfgpath))
button3.place(relx = 0.5, rely = 0.6, relwidth = 0.8, anchor = tk.CENTER)
label1 = ttk.Label(root, text="Kurorin(@kuro_x#4595)")
label1.place(relx = 0.5, rely = 0.8, anchor = tk.CENTER)








#Find HD78XH
def setB78XH(Community):
    logging.debug("setB78XH")
    os.chdir(Community)
    HDpathS = os.path.join(Community, 'B78XH\html_ui\Pages\VCockpit\Instruments\Airliners')
    HDpathD = os.path.join(Community, 'B78XH-main\html_ui\Pages\VCockpit\Instruments\Airliners')
    HDpathD2 = os.path.join(Community, 'B78XH-dev\html_ui\Pages\VCockpit\Instruments\Airliners')
    HDpathE = os.path.join(Community, 'B78XH-experimental\html_ui\Pages\VCockpit\Instruments\Airliners')
    #check if HD78XH exists and HD78XH is separated new one -v1.1.0
    if os.path.exists(HDpathS):
        if os.path.exists(os.path.join(HDpathS, 'Heavy-Division-B78XH-mod\FMC')):
            isHDB78XHnew = True
            HDPath = os.path.join(HDpathS, 'Heavy-Division-B78XH-mod\FMC')
        else:
            HDPath = os.path.join(HDpathS, 'B787_10\FMC')
            isHDB78XHnew = False
        HDname = "B78XH"
        logging.info("HD78XH(Stable) found")
        print("HD78XH(Stable) found")
    elif os.path.exists(HDpathD):
        if os.path.exists(os.path.join(HDpathD, 'Heavy-Division-B78XH-mod\FMC')):
            HDPath = os.path.join(HDpathD, 'Heavy-Division-B78XH-mod\FMC')
            isHDB78XHnew = True
        else:
            HDPath = os.path.join(HDpathD, 'B787_10\FMC')
            isHDB78XHnew = False
        HDname = "B78XH-main"
        logging.info("HD78XH(Development) found")
        print("HD78XH(Development) found")
    elif os.path.exists(HDpathD2):
        if os.path.exists(os.path.join(HDpathD2, 'Heavy-Division-B78XH-mod\FMC')):
            HDPath = os.path.join(HDpathD2, 'Heavy-Division-B78XH-mod\FMC')
            isHDB78XHnew = True
        else:
            HDPath = os.path.join(HDpathD2, 'B787_10\FMC')
            isHDB78XHnew = False
        HDname = "B78XH-dev"
        logging.info("HD78XH(Development) found")
        print("HD78XH(Development) found")
    elif os.path.exists(HDpathE):
        if os.path.exists(os.path.join(HDpathE, 'Heavy-Division-B78XH-mod\FMC')):
            HDPath = os.path.join(HDpathE, 'Heavy-Division-B78XH-mod\FMC')
            isHDB78XHnew = True
        else:
            HDPath = os.path.join(HDpathE, 'B787_10\FMC')
            isHDB78XHnew = False
        HDname = "B78XH-experimental"
        logging.info("HD78XH(Experimental) found")
        print("HD78XH(Experimental) found")
    else:
        logging.error("HeavyDivision's B78XH not found.")
        print("HeavyDivision's B78XH not found. Install it and try again.")
        messagebox.showerror("Kuro_B787-8 Installer - Installation Failed", "HeavyDivision's B78XH not found. Install it and try again.")
        return
    return HDname, HDPath, isHDB78XHnew
def SetCom(Community):
    logging.debug("SetCom")
    cB78XH = setB78XH(Community)
    if not cB78XH:
        return
    HDname = cB78XH[0]
    HDPath = cB78XH[1]
    isHDB78XHnew = cB78XH[2]
    return(HDname, HDPath, isHDB78XHnew)



#def - extract and copy 787-8
def Copy788():
    logging.info("Copying Kuro_B787-8 to Community")
    print("Copying Kuro_B787-8 to Community")
    zip_f = zipfile.ZipFile(zippath, "r")
    zip_f.extractall(Community)
    zip_f.close()
    logging.info("Copied Kuro_B787-8 to Community")
    print("Copied Kuro_B787-8 to Community")

#check if 787-8 exists and install
def check788exist(Community, zippath):
    KuroPath = os.path.join(Community, 'Kuro_B787-8')
    if os.path.exists(KuroPath):
        logging.info("Kuro_B787-8 found in Community folder")
        print("Kuro_B787-8 found in Community folder")
        if messagebox.askyesno("Kuro_B787-8 Installer", "Kuro_B787-8 found in Community folder.\nDo you want to replace the current one?\n\nSelect Yes to continue.\nSelect No to abort reinstall"):
            #check if zip exist
            if not os.path.exists(zippath):
                logging.error("Required Installer Component(main.zip) not found.")
                print("Required Installer Component(main.zip) not found. Download and Extract the installer again.")
                messagebox.showerror("Kuro_B787-8 Installer - Installation Failed", "Required Installer Component(main.zip) not found.\n(The file is required to install)\n\nDownload and Extract the installer again.")
                isInstallperformed = 0
            else:
                #delete 787-8
                logging.info("Deleting Kuro_B787-8 in Community")
                print("Deleting Kuro_B787-8 in Community")
                shutil.rmtree(KuroPath)
                logging.info("Deleted Kuro_B787-8 in Community")
                print("Deleted Kuro_B787-8 in Community")
                #copy 787-8
                Copy788()
                isInstallperformed = 1
        else:
            isInstallperformed = 0
    #check if zip exists
    elif not os.path.exists(zippath):
        logging.error("Required Installer Component(main.zip) not found.")
        print("Required Installer Component(main.zip) not found. Download and Extract the installer again.")
        messagebox.showerror("Kuro_B787-8 Installer - Installation Failed", "Required Installer Component(main.zip) not found. \n\nDownload and Extract the installer again.")
        isInstallperformed = 0
    else:
        #copy 787-8
        Copy788()
        isInstallperformed = 1
    return isInstallperformed






#check if not HD78XH is newer (separated) one - v1.1.0
#def - extract and copy new HD patch - v1.1.0
def PatchnewHD(isHDB78XHnew, HDpatchpath, Community):
    logging.debug("patch newHD")
    if isHDB78XHnew:
        if not os.path.exists(HDpatchpath):
            logging.info("non-separated HD78XH")
            print("non-separated HD78XH")
            logging.error("Required Installer Component(newHD.zip) not found.")
            print("Required Installer Component(newHD.zip) not found. Download and Extract the installer again.")
            messagebox.showerror("Kuro_B787-8 Installer - Installation Failed", "newHD.zip not found.\n\nDownload and Extract the installer again.")
            sys.exit()
        else:
            logging.info("separated HD78XH")
            print("separated HD78XH")
            logging.info("Patching files for newer (separated) B78XH")
            print("Patching files for newer (separated) B78XH")
            patch_f1 = zipfile.ZipFile(HDpatchpath, "r")
            patch_f1.extractall(Community)
            patch_f1.close()
            logging.info("Patched files for newer (separated) B78XH")
            print("Patched files for newer (separated) B78XH")

def fmcUpdate(HDPath, Community, isHDB78XHnew):
    #copy HD78XH's FMC files -v1.1.0
    logging.debug("fmcUpdate")
    os.chdir(HDPath)
    if isHDB78XHnew:
        fmcpath7878 = os.path.join(Community, 'Kuro_B787-8\html_ui\Pages\VCockpit\Instruments\Airliners\Heavy-Division-B78XH-mod\FMC')
    else:
        fmcpath7878 = os.path.join(Community, 'Kuro_B787-8\html_ui\Pages\VCockpit\Instruments\Airliners\B787_10\FMC')
    if not os.path.exists(fmcpath7878):
        is788installed = 0
        logging.error("Kuro_B787-8 not found.")
        print("Kuro_B787-8 not found. Install it and try again.")
        messagebox.showerror("Kuro_B787-8 Installer - Installation Failed", "Kuro_B787-8 not found. Install it and try again.")
        return is788installed
    shutil.copyfile('B787_10_FMC.html', fmcpath7878 + '\B787_8_FMC.html')
    shutil.copyfile('hdfmc.js', fmcpath7878 + '\hdfmc8.js')
    logging.info("Copied HDfiles to Kuro_B787-8")
    print("Copied HDfiles to Kuro_B787-8")
    #rewrite HD78XH's FMC files(html) -v1.1.0
    os.chdir(fmcpath7878)
    FMC788html = 'B787_8_FMC.html'
    with open(FMC788html, encoding="UTF-8") as html:
        htmlcontent = html.read()
        if isHDB78XHnew:
            htmlafter = htmlcontent.replace('/Pages/VCockpit/Instruments/Airliners/Heavy-Division-B78XH-mod/FMC/hdfmc.js', '/Pages/VCockpit/Instruments/Airliners/Heavy-Division-B78XH-mod/FMC/hdfmc8.js')
        else:
            htmlafter = htmlcontent.replace('/Pages/VCockpit/Instruments/Airliners/B787_10/FMC/hdfmc.js', '/Pages/VCockpit/Instruments/Airliners/B787_10/FMC/hdfmc8.js')
    with open(FMC788html, mode="w", encoding="UTF-8") as html2:
        html2.write(htmlafter)
    #rewrite HD78XH's FMC files(js)
    os.chdir(fmcpath7878)
    FMC788js = 'hdfmc8.js'
    with open(FMC788js, encoding="UTF-8") as js:
        jscontent = js.read()
        for O, N in zip(oldjs, newjs):
            jscontent= jscontent.replace(O, N)
    with open(FMC788js, mode="w", encoding="UTF-8") as js2:
        js2.write(jscontent)
    is788installed = 1
    return is788installed

#def - extract and copy older xml - v1.0.6
def PatchXML():
    logging.info("Patching xml files for older B78XH engine")
    print("Patching xml files for older B78XH engine")
    patch_f = zipfile.ZipFile(patchpath, "r")
    patch_f.extractall(Community)
    patch_f.close()
    logging.info("Patched xml files for older B78XH engine")
    print("Patched xml files for older B78XH engine")

#check if not HD78XH is compatible with the new engine anim - v1.0.6
def engAnim(Community, HDname, patchpath):
    logging.debug("engAnim")
    EngPath = os.path.join(Community, os.path.join(HDname, 'ModelBehaviorDefs\Heavy\Engines'))
    if not os.path.exists(EngPath):
        if not os.path.exists(patchpath):
            logging.error("Required Installer Component(xml.zip) not found. Download and Extract the installer again.")
            print("Required Installer Component(xml.zip) not found.")
            messagebox.showerror("Kuro_B787-8 Installer - Installation Failed", "xml.zip not found.\n\nDownload and Extract the installer again.")
            sys.exit()
        else:
            logging.info("Use old engines animation")
            print("Use old engines animation")
            PatchXML()

#livery updater v1.1.0
def liveryconv(Community, cfgpath):
    logging.debug("liveryconv")
    if messagebox.askyesno("Kuro_B787-8 Installer", "The installer has detected that you are using the recently released B78XH, which is separated from the Default B787-10.\nThe previous B787-8 liveries are not compatible and cause fmc not to show up or CTD.\nDo you want to convert all liveries for B787-8 installed in your Community folder?\n(This operation cannot be undone.  Also, this feature is experimental.)"):
        convert(Community, cfgpath)
        isLivConverted = 1
    else:
        isLivConverted = 0
    return isLivConverted
    os.chdir(pydir)

def checklivery(isHDB78XHnew, Community, cfgpath):
    logging.debug("checklivery")
    if isHDB78XHnew:
        logging.info("separated B78XH")
        print("separated B78XH")
        liveryconv(Community, cfgpath)
    os.chdir(pydir)

#livery converter v1.1.2
def convert(Community, cfgpath):
    os.chdir(Community)
    for filename1 in glob.glob('**/aircraft.cfg', recursive=True):
        f1 = open(filename1, mode="r", encoding="UTF-8")
        s1 = f1.read()
        f1.close()
        if 'Kuro_B787_8' in s1:
            dirname1 = os.path.dirname(filename1)
            print("Scanned : " + dirname1)
            #model.cfg
            for model1 in glob.glob(os.path.join(dirname1, 'model.*/model.cfg')):
                shutil.copyfile(cfgpath + r'\model.cfg', model1)
            #texture.cfg
            for tex1 in glob.glob(os.path.join(dirname1, 'texture.*/texture.cfg')):
                shutil.copyfile(cfgpath + r'\texture.cfg', tex1)
            #panel.cfg
            for panel1 in glob.glob(os.path.join(dirname1, 'panel.*/panel.cfg')):
                shutil.copyfile(cfgpath + r'\panel.cfg', panel1)

def endI():
    print('Re-run the batch file each time after updating B78XH. If not, the instruments will not work properly.')
    messagebox.showwarning("Kuro_B787-8 Installer", "Re-run the batch file each time after updating B78XH to update FMC files.\nIf not, the instruments will not work properly.")
    logging.info('Installation/Update has completed')
    print('Installation/Update has completed')
    messagebox.showinfo("Kuro_B787-8 Installer", "Installation/Update has completed.")
    os.chdir(pydir)
def endF():
    logging.info('FMC files have been updated.')
    print('FMC files have been updated.')
    messagebox.showinfo("Kuro_B787-8 Installer", "FMC files have been updated.")
    os.chdir(pydir)
def endL():
    logging.info('Livery configs have been updated.')
    print('Livery configs have been updated.')
    messagebox.showinfo("Kuro_B787-8 Installer", "Livery configs have been updated.")
    os.chdir(pydir)


root.mainloop()