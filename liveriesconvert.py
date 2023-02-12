from tkinter import filedialog
from tkinter import messagebox
import os
import zipfile
import shutil
import sys
import tkinter as tk
import re
import glob

#livery convert
def convert(Community, cfgpath):
    os.chdir(Community)
    for filename1 in glob.glob('**/aircraft.cfg', recursive=True):
        with open(filename1) as f1:
            s1 = f1.read()
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



if __name__ == "__main__": 
    cfgpath = os.path.join(os.getcwd(), "livery-cfgs")
    sample_func() 
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
    if Community == "":
        messagebox.showerror("Kuro_B787-8 Installer - Installation Canceled", "Installation Canceled")
        sys.exit()
    print("Community Path = " + Community)
    convert(Community, cfgpath)


'''
oldM = "..\..\Asobo_B787_10\model\B787_10_interior.xml"
newM = "..\..\Heavy-Division-B78XH-mod\model\B787_10_interior.xml"
oldT = r"fallback.6=..\..\Kuro_B787_8\texture\nfallback.7=..\..\Asobo_B787_10\texture\nfallback.8=..\..\..\..\texture\Planes_Generic\nfallback.9=..\..\..\..\texture\Extinguisher"
newT = r"fallback.6=..\..\Kuro_B787_8\texture\nfallback.7=..\..\Heavy-Division-B78XH-mod\texture\nfallback.8=..\..\Asobo_B787_10\texture\nfallback.9=..\..\..\..\texture\Planes_Generic\nfallback.10=..\..\..\..\texture\Extinguisher"
oldP = "Airliners/B787_10/FMC/B787_8_FMC.html"
newP = "Airliners/Heavy-Division-B78XH-mod/FMC/B787_8_FMC.html"
os.chdir(Community)
for filename1 in glob.glob('**/aircraft.cfg', recursive=True):
    with open(filename1) as f1:
        s1 = f1.read()
        if 'Kuro_B787_8' in s1:
            dirname1 = os.path.dirname(filename1)
            #model.cfg
            for model1 in glob.glob(os.path.join(dirname1, 'model.*/model.cfg')):
                with open(model1) as m0:
                    m1 = m0.read()
                    m2 = m1.replace(oldM, newM)
                    print("Converted : " + model1)
                    with open(model1, 'w') as m3:
                        m3.write(m2)
            #texture.cfg
            for tex1 in glob.glob(os.path.join(dirname1, 'texture.*/texture.cfg')):
                with open(tex1) as t0:
                    t1 = t0.read()
                    t2 = t1.replace(oldT, newT)
                    print("Converted : " + tex1)
                    with open(tex1, 'w') as t3:
                        t3.write(t2)
            #panel.cfg
            for panel1 in glob.glob(os.path.join(dirname1, 'panel.*/panel.cfg')):
                with open(panel1) as p0:
                    p1 = p0.read()
                    p2 = p1.replace(oldP, newP)
                    print("Converted : " + panel1)
                    with open(panel1, 'w') as p3:
                        p3.write(p2)
'''

