#! /bin/bash

PYMAIL="$HOME/.pymail_profile.sh"
profile="$HOME/.bash_profile"

function update_bash(){
    echo "# pymail setup" >> $profile
    echo "if [ -f ~/.pymail_profile.sh ]; then" >> $profile
    echo "    source ~/.pymail_profile.sh" >> $profile
    echo "fi" >> $profile
    echo "alias pymail=\"pymail.py\"" >> $profile
}

function create_profile(){
    echo "#! /bin/bash" > $PYMAIL
    echo "export PYMAIL_SRV=$1" >> $PYMAIL
    echo "export PYMAIL_PRT=$2" >> $PYMAIL
    echo "export PYMAIL_ADR=$3" >> $PYMAIL
    echo "export PYMAIL_PSW=$(md5 -q -s $4)" >> $PYMAIL
}

touch $PYMAIL
echo "---- PyMail Config ----"
echo "Smtp server : "
read server
echo "Port : "
read port
echo "Mail addr : "
read acc
echo "Mail pass :"
read psw
create_profile $server $port $acc $psw
chmod +x $PYMAIL
update_bash
echo "Done, restart the shell to make changes effective"
echo "---- PyMail Config ----"