#!/bin/bash

File=servers


while read line;do
    args=( $line )
    if [ ${#args[@]} -eq 5 ];then
        version1=$(ssh -i private.key -l ${args[0]} ${args[1]} lsof -i:${args[3]} | grep ${args[2]})
        version2=$(ssh -i private.key -l ${args[0]} ${args[1]} lsof -i:${args[4]} | grep ${args[2]})
        if [ ! -z "$version1" ] && [ ! -z "$version2" ];then
            echo "Service on ${args[0]}@${args[1]} running both version."
        elif [ ! -z "$version1" ];then
            echo "Service on ${args[0]}@${args[1]} running old version."
        elif [ ! -z "$version2" ];then
            echo "Service on ${args[0]}@${args[1]} running new version."
        else
            echo "Service on ${args[0]}@${args[1]} is not running."
        fi
    else
        echo "Illegal input"
    fi
done < $File



