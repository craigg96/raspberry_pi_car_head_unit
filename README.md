# DIY Car Head Unit
DIY raspberry pi car headunit with built in navigation and music using android auto as well as a dashcam, reverse camera and obd monitor

### Installer Script
The installer script for openauto is by humeman and patches various issues with newer GSP/touchscreen/device detection issues.

Tested using latest Raspbian Buster (2019-09-26) on 3B

### Installation Instructions
* Install git, if it's not already installed: `sudo apt install git`
* CD to user directory: `cd ~`
* Clone this repo - git clone https://github.com/craigg96/raspberry_pi_car_head_unit.git
* Mark as executable: `sudo chmod +x raspberry_pi_car_head_unit/install_openauto.sh`
* Run the installer: `raspberry_pi_car_head_unit/install_openauto.sh`
* Open OpenAuto (add to crontab or other autorun to start at boot): `sudo ~/openauto/bin/autoapp`
* Configure as necessary, plug in your phone, and you're good to go!

### Any issues?
Any issues with android-auto setup see the patched installer repo >> https://github.com/humeman/openauto-patched-installer

Any other issues let me know

### Uses:
**AASDK**: [abraha2d/aasdk](https://github.com/abraha2d/aasdk), forked from: [opencardev/aasdk](https://github.com/opencardev/aasdk), forked from: [f1xpl/aasdk](https://github.com/f1xpl/aasdk)

**OpenAuto**: [humeman/openauto](https://github.com/humeman/openauto), forked from: [Oper92/openauto](https://github.com/Oper92/openauto), forked from: [f1xpl/openauto](https://github.com/f1xpl/openauto)

*My openauto repo uses a fix to VideoService to stop compile errors, found at [abraha2d/openauto](https://github.com/abraha2d/openauto)*
