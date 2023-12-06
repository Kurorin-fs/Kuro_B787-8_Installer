# Changelogs
##### Last Updated On :  December 06, 2023
###### v3.0.1


#
<details><summary><strong>v3.0.1</strong></summary>
  
  - [SYS] WT0.2.4 Systems(SU14)
  - [FM] Adjusted Climb Performance
  - [FM/SYS] Adjusted Fuel Consumption / ETA Fuel
  - [EXT] Adjusted Wingflex
  - [FM] Adjusted Spoilers/Flaps Performances

</details>

<details><summary><strong>v3.0.0</strong></summary>
  
  - [SYS] WT0.1.18(SU13/14beta) Systems
  - [FM] Updated Flight Model
  - [EXT] Toggleable SatCom
  - [EXT] New Wingflex
  - [INT] New PFD, CDU and MFD colours
  - [SYS] EFB Door Page
  - [EXT] New PBR Textures
  - [SYS] PFD - VBar
  - [INT] New Camera positions
  - [FX/INT] New cockpit lights
  - [UI] Initial Loading Tip
  - [FM/SYS] Fuel Scalar, ETA Fuel and TSFC
  - [SYS] Fixed OPT being higher than MAX

</details>

<details><summary><strong>v2.1.1</strong></summary>
  
  - [EXT] Duplicated Center Wheels fix (from v2.1.0)

</details>

<details><summary><strong>v2.1.0</strong></summary>
  
  - [INT] New cockpit texture fonts
  - [INT] New MCP fonts
  - [FX/INT] New interior lights
  - [FX/EXT] Beacon light improvements
  - [SYS] Set max ceiling altitude to FL430
  - [FM] Wing flex fix integration
  - [FM] Bounce fix
  - [FM] Gear Compression fix
  - [FM/EXT] Steering fix
  - [SYS] Add GSX Profile
  - [UI] Add Checklists
  - [FM] Fix Pitches from an External View
  - [FM] Fix Cruising with a negative pitch
  - [FM] Reworked flaps and slats configuration
  - [FM] Flight model dimensions & position update
  - [FM] Reworked aircraft data based on simulation software
  - [FM] Reworked default payload stations based on BAW cabin layout
  - [SYS] Adjust RA on the ground
  - [INT] New cockpit texture decals
  - [FM] Flight Director overshoot on turn fix
  - [UI] Add a tool to export Community folder lists to the Installer for easier support
  - [UI] Add changelog link to the Installer
  - [INT/EXT] minor texture & model bug fixes

</details>

<details><summary><strong>v2.0.0</strong></summary>
  
  - [SYS/FM] Accurate -8 FMC Calculation/Trim Settings/Flight models based on FCOM and Real References  
  - [FX/EXT] NewLight Effects  
  - [EXT] New GE Engine Textures/Anims  
  - [FM] Some FM Improvements  
  - [UI] Added Tips  
  
  - [SYS/FM] Systems/Flight models are completely overhauled based on AAU2  
  - [SYS/FM/LIV/SND] Split GEnx-1B64/Trent1000-H Variants  
  - [EXT] Added model.v2  
  - (High Res mesh, Unmirrored UV mapping for Tail/Engines/Wings/Bottom-Gear-Door/Cargo-Hinge)  
  
  - [SYS] Corrected GE Engine MFD Gauges  
  - [SYS] Corrected GE Engine FMC Values  
  - [SYS/FM] Adjusted Engines Power/Fuel Flow to match FCOM, Real Reference and SimBrief  
  - [EXT] Corrected Airplane Height  
  - [EXT] Corrected Gear Hinge Animations as irl  
  - [UI] The Installer has a function to patch/use Third-Party SoundPacks easily  
  - [UI] The Installer has a function to convert Older Liveries (For ~v1.1.6) with User Selected Engine Variants  
  - (For real B788 operators, GE/RR is selected by default. For virtual, GE is selected.)  
  - [FM] Adjusted Steering Sensitivity  
  - [FM] Adjusted Pitch/Roll/Yaw Stability  
  
  - [EXT] Adjusted GPU/Fuel Pipes to the correct position  
  - [EXT] Adjusted GPU/Fuel Truck position to the correct one  
  - [LIV] Liveries no longer need to include its own panel.cfg  
  - [EXT] New Engines Animation  
  - [EXT] New Engine textures  
  - [LIV] Added ANA Saba Special Livery (JA801A)  
  - [LIV] Added TUI Livery (T-GUIH)  
  - [FX] Added APU Blur effect  
  
  - [UI] Added Custom Loading Screen Images  
  - (Currently not working due to Asobo's bug)  
  - [LIV] ANA/JAL Custom Wing textures  
  - [FX] More brighter Beacon/Strobo Light  
  - [FM] Weight fix
</details>

<details><summary><strong>v1.1.6</strong></summary>

  - Fixed problem with ANA and JAL engine animations when using with B78XH(dev) since v1.1.1
</details>

<details><summary><strong>v1.1.5</strong></summary>

  - Fixed problem with rudder not being enabled.  
  - Fixed a problem with the livery converter.
  - The problem with the loss of Animation for Engine in third party liveries is due to a change in the latest B78XH.
  - The flight model is now based on the one used until v1.0.5 (basic Flight Model). v1.0.6-v1.1.4 flight models are named "exp Flight Model" and you can specify which one to use from the Settings tab before installation/update.
  - control issues could be improved.
</details>

<details><summary><strong>v1.1.4</strong></summary>

  - Fix Livery Converter issue  
  - Add revert function to Livery Converter
</details>

<details><summary><strong>v1.1.3</strong></summary>

  - Fixed problems with exp installation  
  - Updated livery conversion function  
  - Updated menu  
  - Updated FAQ page
</details>

<details><summary><strong>v1.1.2</strong></summary>

  - New installer  
  - Created FAQ Page
  - Remove texts/decals showed in front of the cockpit.  
  - Fix Strobe lights direction
  - The engine thrust has been reduced to 0.92  
  - Added code to phase out the CLB 1/2 limit at FL100 and above as irl, (so low climb rate has been solved.)  
  - Added code to show optimum, maximum and recommended altitude based on current weight in FMC page.  
  - Improved Control stability
</details>

<details><summary><strong>v1.1.1</strong></summary>

  - Fixed liveries bug  
  - Increased engine thrust power
</details>

<details><summary><strong>v1.1.0</strong></summary>

  - Realistic flight model based on documentation  
  - Engine parameters from GEnx-1B67  
  - More realistic strobe and beacon lights  
  - More realistic fuel consumption  
  - FMC payload manager adjusted for -8  
  - Front wheels can now turn up to 70° left/right  
  - Fuel pump bug fixed  
  - The sound is now using the B78X(or B78XH) one.  
  - Support for B78XH (latest exp) separated from default 78X  
  - (recommended B78XH is latest Dev)  
</details>

<details><summary><strong>v1.0.6</strong></summary>

  - Fixed APU issues.  
  - Top beacon light in correct position.  
  - Some of the models have been reworked, the definition has been increased, and some bugs in the models have been fixed.  
  - Fixed American livery's engine painting.  
  - The installer detects the latest B78XH(dev) and adapts configs to the new engine animations.
</details>

<details><summary><strong>v1.0.5</strong></summary>

  - Even if the folder name of HD78XH (downloaded by Community-Downlaoder) is B78XH-dev, it will be detected (as dev version).  
  - Parameters such as engine thrust, fuel consumption, etc. will be the same as the (installed) B78XH after runned v1.0.5-installer.  
  - (-1B76 instead of GEnx-1B70, but more realistic to fly than before).
</details>

<details><summary><strong>v1.0.4</strong></summary>

  - The installer has changed from .exe to .bat+.py. This eliminates false positives of substitution-type-malware by McAfee.  
  - Liveries/models Updated.  
</details>

<details><summary><strong>v1.0.3</strong></summary>

  - Fix for some users cannot run installer.
</details>

<details><summary><strong>v1.0.2</strong></summary>

  - The installer no longer checking for Asobo B78X, as there was still a problem with Steam users not being able to use the installer.
</details>

<details><summary><strong>v1.0.1</strong></summary>

  - Fixed an issue Steam users were getting an error when running the installer.
</details>

<details><summary><strong>v1.0.0</strong></summary>

  - Corrected Cockpit Position  
  - Corrected Aerodynamics configs  
  - Corrected Camera configs  
  - Corrected AFT Cargo Position  
  - Systems compatibility with HD  
  - Fixed broken instruments  
  - FMC now shows correct engines name  
  - Corrected flaps settings in FMC  
  - Fixed Strobe Lights  
  - Fixed Interior Lights (e.g. Dome Lights)  
  - Fixed Logo Lights missing  
  - Fixed Wipers missing  
  - Corrected Flaps config / EICAS Instruments / FMC Settings (deleted flaps 10, 17, 18)  
  - Changed Flap lever decals  
  - Changed Flaps Speed Limit decals.  
  - Fixed ailerons inverted  
  - Fixed Qatar livery  
  - Added Liveries : Air Canada, United Airlines (New - 2019, not irl)
</details>

<details><summary><strong>v0.0.1</strong></summary>

  - Initial release
</details>
