#! /bin/sh

is_command_existed ()
{
    if command -v $1 >/dev/null 2>&1;
    then return 0
    else return 1
    fi
}

check_requirements ()
{
    have_requirements_met=0

    if ! is_command_existed python; then
        have_requirements_met=1
        >&2 echo "ERROR: python not found"
    fi

    if ! is_command_existed pip; then
        have_requirements_met=1
        >&2 echo "ERROR: pip not found"
    fi

    return $have_requirements_met
}

do_install ()
{
    if sudo pip install -r requirements.txt; then
        if sudo python setup.py install --record files.txt;
        then return 0
        else return 1
        fi
    else return 1
    fi
}


if check_requirements; then
    if do_install; then
        service aliyun-sms-alert start
        echo "Installation succeeded"
    else >&2 echo "Installation failed"
    fi
else
    >&2 echo "Installation failed"
    exit 1
fi
