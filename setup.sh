#! /bin/bash

echo "mail addr : "
read acc
echo "export MAIL_ADR=$acc" >> ~/.bashrc
echo "mail pass :"
read psw
echo "export MAIL_PSW=$(md5 -q -s $psw)" >> ~/.bashrc