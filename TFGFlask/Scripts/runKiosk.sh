#!/usr/bin/bash

xset s noblank
xset s off
xset -dpms
unclutter -idle 0.1 -root &
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/'/home/kioskpi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"crashed"/"exit_type":"Normal"/'/home/kioskpi/.config/chromium/Default/Preferences
/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk http://127.0.0.1:5000

#END
