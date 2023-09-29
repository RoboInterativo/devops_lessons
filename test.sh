#!/usr/bin/env bash


RESPONSE=$(/bin/python3 /etc/zabbix/scripts/external_system/get_data.charges.py);
echo "emp.prod.host charges.response $RESPONSE" | /usr/bin/zabbix_sender -c /etc/zabbix/zabbix_agentd.conf -i - &>/dev/null
exit 0
