# Tools - Pirated App

## Maya

- Install Autodesk Products for mac 2020-2024
- Install nlm11.18.0.0_ipv4_ipv6_mac64.tar
- copy from medicine folder the .dilyb and apply it on :/Library/Application Support/Autodesk/AdskLicensing/Current/AdskLicensingAgent/AdskLicensingAgent.app/Contents/PlugIns/
- Disable SIP from Recovery macOS boot

> (optional if you want only filesystem file use this command :csrutil enable --without fs would disable file protection system Only

Follow steps below for license.dat and run lmgrd:

open terminal and cd `/usr/local/flexnetserver/`

1. Execute command hostname

For me it response WhiteDeath.local

2. Execute command scutil --get LocalHostName

For me it response whitedeath1s-MacBook-Pro

3. Execute command scutil --get HostName

For me it response something like hostname is not set

4. Then I set it executed command sudo scutil --set HostName whitedeath1s-MacBook-Pro.local (if already set no need do it)

5. Then I add to /etc/hosts this line:

127.0.0.1 whitedeath1s-MacBook-Pro.local whitedeath1s-MacBook-Pro

Then execute ./lmgrd -c license.dat work correctly

more info here for make it run from boot:https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-start-license-server-on-Mac-OS-X-automatically.html

run Autodesk Product of you choice and choose network 27080@localhost!

Crack by:WhiteDeath

