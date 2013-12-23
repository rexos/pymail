#! /bin/bash
profile="$HOME/.bash_profile"

function unset_all(){
    unset "PYMAIL_SRV"
    unset "PYMAIL_PRT"
    unset "PYMAIL_ADR"
    unset "PYMAIL_PSW"
}

unset_all
rm $HOME/.pymail_profile.sh
sudo sed '/pymail/d' $profile > tmp
chmod 644 tmp
mv tmp $profile