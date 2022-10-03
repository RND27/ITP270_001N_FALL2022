#!/bin/bash

cd /home/student/ITP270_001N_FALL2022/'Week 3 (Shell Scripting)'

echo "enter a domain"
read domain

wget -o $domain\ robots.txt $domain/robots.txt

cat robots.txt | grep "Disallow" | cut -d " " -f2 | tr -d "*."  > $domain\ robocut.txt

firefox &
sleep 5

for i in $(cat $domain\ robocut.txt); do
        firefox -new-tab https://www.$domain$i &
        sleep 2
done
~                                                                               
~                                                                               
~                                                                               
~                                                                               
<2022/Week 3 (Shell Scripting)/robots.sh" 18L, 366C           13,7          All
