show_menu () {
    # We show the host name right in the menu title so we know which Pi we are connected to
    OPTION=$(whiptail --title "Menu (Host:$(hostname))" --menu "Choose your option:" 12 36 5 \
    "1" "Heating Off" \
    "2" "Heating On" 3>&1 1>&2 2>&3)
 
    BUTTON=$?
    # Exit if user pressed cancel or escape
    if [[ ($BUTTON -eq 1) || ($BUTTON -eq 255) ]]; then
        exit 1
    fi
    if [ $BUTTON -eq 0 ]; then
        case $OPTION in

        1)
            # For sensitive commands, we make sure they must press extra keys
            confirmAnswer "Are you sure you want to turn the heating off?"
            if [ $? = 0 ]; then
                echo Turning Heating Off...
		aplay /home/pi/heating_off.wav
		show_menu
            else
                show_menu
            fi
            ;;
        2)
            confirmAnswer "Are you sure you want to turn the heating back on?"
            if [ $? = 0 ]; then
                echo Turning Heating On...
                aplay /home/pi/heating_on.wav
		show_menu
            else
                show_menu
            fi
            ;;
        esac
    fi  
}