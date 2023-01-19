from tkinter import filedialog
from tkinter import messagebox
import os
import zipfile
import shutil
import sys
import tkinter as tk

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
8uP6/+z5+vX49Pb59uj9/Pb7/vD9/fn7+P36///6+fr8+fL/+fP///X/+v/8+/7+
9f/9//r///z/+/3//CwAAAAAgACAAAAI/gDdCRxIsKDBgwgTKlzIsKHDhxAjSpxI
saLFixgzatzIsaPHjyBDihxJsqTJkyhTqlzJsqXLlzBjypxJs6bNmzhz6tzJs6fP
n0CDCh1KtKjRo0iTKl3KtKnTp1CjSp1KtarVq1izat3KtavXr2DDih1LtqzZs2jT
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
i7RYi7ZIFAEBADs=
     ''' 
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(data=data))


#Intro
print("\nThis program is the installer/updater of Kuro_B787-8 for Microsoft Flight Simulator.    Creator:Kurorin(@kuro_x#4595)\nRequired Contents : MSFS Premium Delux Version, HeavyDivision's B78XH(any version)")
if not messagebox.askokcancel("Kuro_B787-8 Installer v1.0.2", "This program is the installer/updater of Kuro_B787-8 for Microsoft Flight Simulator.\n\nRequired Contents :\nMSFS Premium Delux Version,\nHeavyDivision's B78XH(any version)\n\nCreator : Kurorin(@kuro_x#4595)\nhttps://flightsim.to/profile/Kurorin\n\nPress OK to Continue"):
    messagebox.showerror("Kuro_B787-8 Installer - Installation Canceled", "Installation Canceled")
    sys.exit()

#zip Path
zippath = os.path.join(os.getcwd(), 'Kuro_B787-8.zip')

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

#MS Store Path
USERCFGpathM = os.path.join((os.environ['USERPROFILE']), 'AppData\Local\Packages\Microsoft.FlightSimulator_8wekyb3d8bbwe\LocalCache')
#Steam Path
USERCFGpathS = os.path.join((os.environ['USERPROFILE']), 'AppData\Roaming\Microsoft Flight Simulator')

if os.path.exists(USERCFGpathM):
    os.chdir(USERCFGpathM)
    MSFSpath = OpenOpt()
elif os.path.exists(USERCFGpathS):
    os.chdir(USERCFGpathS)
    MSFSpath = OpenOpt()
else:
    MSFSpath = os.environ['USERPROFILE']

#ask users where Community is
Community = filedialog.askdirectory(initialdir = MSFSpath, title='Kuro_B787-8 Installer - Select Community Folder') 
if Community == "":
    messagebox.showerror("Kuro_B787-8 Installer - Installation Canceled", "Installation Canceled")
    sys.exit()
print("Community Path = " + Community)

#Find HD78XH
os.chdir(Community)
HDpathS = os.path.join(Community, 'B78XH\html_ui\Pages\VCockpit\Instruments\Airliners\B787_10\FMC')
HDpathD = os.path.join(Community, 'B78XH-main\html_ui\Pages\VCockpit\Instruments\Airliners\B787_10\FMC')
HDpathE = os.path.join(Community, 'B78XH-experimental\html_ui\Pages\VCockpit\Instruments\Airliners\B787_10\FMC')

#check if HD78XH exists
if os.path.exists(HDpathS):
    HDPath = HDpathS
    print("HD78XH(Stable) found")
elif os.path.exists(HDpathD):
    HDPath = HDpathD
    print("HD78XH(Development) found")
elif os.path.exists(HDpathE):
    HDPath = HDpathE
    print("HD78XH(Experimental) found")
else:
    print("HeavyDivision's B78XH not found. Install it and try again.")
    messagebox.showerror("Kuro_B787-8 Installer - Installation Failed", "HeavyDivision's B78XH not found. Install it and try again.")
    sys.exit()

'''#check if Asbo_B78X exists
AS78XPath = os.path.join(os.path.dirname(Community), r'Official\OneStore\asobo-aircraft-b787-10')
AS78XPathS = os.path.join(os.path.dirname(Community), r'Official\Steam\asobo-aircraft-b787-10')
print(AS78XPath)
if not os.path.exists(AS78XPath) and not os.path.exists(AS78XPathS):
    print("Asobo B78X not found. You have to install Premium Delux Version of MSFS and the B787-10. After that, try again.")
    messagebox.showerror("Kuro_B787-8 Installer - Installation Failed", "Asobo B78X not found\nYou have to install Premium Delux Version of MSFS and the B787-10.\nAfter that, try again.")
    sys.exit()
else:
    print("Asobo B78X found in Official folder")
'''

#extract and copy 787-8
def Copy788():
    print("Copying Kuro_B787-8 to Community")
    zip_f = zipfile.ZipFile(zippath, "r")
    zip_f.extractall(Community)
    zip_f.close()
    print("Copied Kuro_B787-8 to Community")

#check if 787-8 exists
KuroPath = os.path.join(Community, 'Kuro_B787-8')
if os.path.exists(KuroPath):
    print("Kuro_B787-8 found in Community folder")
    if messagebox.askyesno("Kuro_B787-8 Installer", "Kuro_B787-8 found in Community folder.\nDo you want to replace the current one?\n\nSelect Yes to re-install.\nSelect No to only update the instrument files from B78XH."):
        #check if zip exist
        if not os.path.exists(zippath):
            print("Kuro_B787-8.zip not found. Download and Extract the installer again.")
            messagebox.showerror("Kuro_B787-8 Installer - Installation Failed", "Kuro_B787-8.zip not found.\n\nDownload and Extract the installer again.")
            sys.exit()
        else:
            #delete 787-8
            print("Deleting Kuro_B787-8 in Community")
            shutil.rmtree(KuroPath)
            print("Deleted Kuro_B787-8 in Community")
            #copy 787-8
            Copy788()
#check if zip exists
elif not os.path.exists(zippath):
    print("Kuro_B787-8.zip not found. Download and Extract the installer again.")
    messagebox.showerror("Kuro_B787-8 Installer - Installation Failed", "Kuro_B787-8.zip not found.\n\nDownload and Extract the installer again.")
    sys.exit()
else:
    #copy 787-8
    Copy788()


#copy HD78XH's FMC file
os.chdir(HDPath)
fmcpath7878 = os.path.join(Community, 'Kuro_B787-8\html_ui\Pages\VCockpit\Instruments\Airliners\B787_10\FMC')
shutil.copyfile('B787_10_FMC.html', fmcpath7878 + '\B787_8_FMC.html')
shutil.copyfile('hdfmc.js', fmcpath7878 + '\hdfmc8.js')
print("Copied HDfiles to Kuro_B787-8")


#rewrite HD78XH's FMC files(html)
os.chdir(fmcpath7878)
FMC788html = 'B787_8_FMC.html'
with open(FMC788html, encoding="UTF-8") as html:
    htmlcontent = html.read()
    htmlafter = htmlcontent.replace('/Pages/VCockpit/Instruments/Airliners/B787_10/FMC/hdfmc.js', '/Pages/VCockpit/Instruments/Airliners/B787_10/FMC/hdfmc8.js')
with open(FMC788html, mode="w", encoding="UTF-8") as html2:
    html2.write(htmlafter)


#rewrite HD78XH's FMC files(js)
oldjs = ["['787-10', 'GEnx-1B76']", "Only flaps 5, 10, 15, 17, 18, 20 can be set for takeoff", "[5, 10, 15, 17, 18, 20]", "let flapAngles = [0, 1, 5, 10, 15, 17, 18, 20, 25, 30];"]
newjs = ["['787-8', 'GEnx-1B70']", "Only flaps 5, 15, 20 can be set for takeoff", "[5, 15, 20]", "let flapAngles = [0, 1, 5, 15, 20, 25, 30];"]

FMC788js = 'hdfmc8.js'
with open(FMC788js, encoding="UTF-8") as js:
    jscontent = js.read()
    for O, N in zip(oldjs, newjs):
        jscontent= jscontent.replace(O, N)
with open(FMC788js, mode="w", encoding="UTF-8") as js2:
    js2.write(jscontent)


print('Be sure to re-run this exe every time after updating B78XH. If not, the instruments will not work properly.')
messagebox.showwarning("Kuro_B787-8 Installer", "Be sure to re-run this exe every time after updating B78XH.\nIf not, the instruments will not work properly.")
print('Installation/Update has completed')
messagebox.showinfo("Kuro_B787-8 Installer", "Installation/Update has completed.")
sys.exit()
