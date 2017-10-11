#!/bin/bash
##
## saveMyDay.bash
## Script de sauvegarde maison d'après linuxmag 203
##

readonly DIR_LIST='data/backup.list'
readonly EXCLUDE_LIST='data/backup_exclude.list'
readonly HDD=('admin@192.168.1.17:/data/macbook/')
readonly ERROR_LOG='data/error.log'
readonly ERROR_SAVE='data/error.log.bak'
readonly ALARM_SOUND='data/alarm.wav'
readonly MAIL='thomas.etcheverria@mailfence.com'

usage() {
    if [ "${1}" == "help" ]; then
        local hdd_number=0
        echo 'Usage: backupSys <action> [hdd_number] [init]'
        echo '       <action> :'
        echo '           - save   : Sauvegarde les répertoires DIR_LIST dans HDD[hdd_number]'
        echo '           - notify : pour envoyer les fichiers'
        echo '           - state  : état de la sauvegarde (contenu de error.log)'
        echo '           - mail   : envoi d un rapport par mail'
        echo '       [hdd_number] : numéro du disque à utiliser'
        echo '       [init]       : si spécifié, initialisation du fichier error.log'
        for hdd in ${HDD[@]}; do
            echo "           - ${hdd_number} : ${hdd}"
            hdd_number=$((${hdd_number}+1))
        done
        exit 0
    fi
}

# Sauvegarde des répertoires de DIR_LIST sur le disque passé en paramètre
# ${1} : numéro du disque à utiliser dans HDD
# ${2} : initialisation du fichier error.log (optionnel)
save() {
    # Exclusion des fichiers de EXCLUDE_LIST
    local exclude=""
    while read -r directory || [[ -n "${directory}" ]]; do
        exclude="--exclude ${directory} ${exclude}"
    done < ${EXCLUDE_LIST}
    # Lancement des sauvegardes
    while read -r directory || [[ -n "${directory}" ]]; do
#        notify-send -t 1500 "backupSys" "Lancement de la sauvegarde sur :\n${HDD[${1}]}"
        rsync -aH --delete --force --stats ${exclude} ${directory} ${HDD[${1}]} 2>> ${ERROR_LOG} | logger -p local0.notice
#        notify-send -i /usr/share/icons/mate/32x32/emblems/emblem-default.png -t 1500 "backupSys" "Sauvegarde terminée sur :\n${HDD[${1}]}"
    done < ${DIR_LIST}
}

# Notification d'erreur lors de la sauvegarde
notify() {
    if [ -s ${ERROR_LOG} ]; then
        notify-send -i /usr/share/icons/mate/32x32/status/dialog-warning.png -u CRITICAL -t 15000 "backupSys" "Erreur de sauvegarde\nConsultez les fichiers :\n- error.log\n- /var/log/backup.log"
        amixer -D pulse sset Master 100%
        aplay ${ALARM_SOUND}
    else
        notify-send -i /usr/share/icons/mate/32x32/emblems/emblem-default.png -t 1500 "backupSys" "Sauvegarde OK"
    fi
}

# État de la sauvegarde
state() {
    more ${ERROR_LOG}
}

# Vérification des sauvegardes et rapport par mail
mail() {
    local content=""
    for hdd in ${HDD[@]}; do
        content=${content}"Sauvegarde sur ${hdd}\n"
        content=${content}$(find ${hdd} -mtime -1)
        content=${content}"\n\n"
    done
    printf "To:${MAIL}\nSubject:Rapport de sauvegarde du $(date)\n\n${content}" > /tmp/mail.txt
    msmtp -t < /tmp/mail.txt
    rm /tmp/mail.txt
}

if [ "${1}" == 'save' ]; then
    save ${2}
elif [ "${1}" == 'notify' ]; then
    notify
elif [ "${1}" == 'state' ]; then
    state
elif [ "${1}" == 'mail' ]; then
    mail
else
    usage 'help'
fi