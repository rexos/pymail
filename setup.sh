#! /bin/bash

echo "mail addr : "
read acc
echo "export PYMAIL_ADR=$acc" >> ~/.bashrc
echo "mail pass :"
read psw
echo "export PYMAIL_PSW=$(md5 -q -s $psw)" >> ~/.bashrc
echo "Done, restart the shell to make changes effective"