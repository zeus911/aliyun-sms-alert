#! /bin/sh

if ! [ -f files.txt ]; then
    >&2 echo "ERROR: Installation record file(files.txt) not found."
    >&2 echo "You may uninstall manually or do reinstall."
    exit 1
else
    service aliyun-sms-alert stop
    cat files.txt | sudo xargs rm -rf
    sudo rm -rf /var/log/aliyun-sms-alert \
        /var/lib/aliyun-sms-alert/messages
    echo "Uninstallation completed"
fi
