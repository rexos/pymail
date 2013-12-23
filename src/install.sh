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

touch $PYMAIL
echo "---- PyMail Config ----"
echo "Mail addr : "
read acc
echo "#! /bin/bash" > $PYMAIL
echo "export PYMAIL_ADR=$acc" >> $PYMAIL
echo "Mail pass :"
read psw
echo "export PYMAIL_PSW=$(md5 -q -s $psw)" >> $PYMAIL
chmod +x $PYMAIL
update_bash
echo "Done, restart the shell to make changes effective"
echo "---- PyMail Config ----"