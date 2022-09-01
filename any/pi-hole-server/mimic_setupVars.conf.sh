#!/bin/bash

setupVars=/etc/pihole/setupVars.conf

# official pihole basic-install.sh code here
getIPv4stuff()
{
	IPV4DEV=$(ip route get 8.8.8.8 | awk '{for(i=1;i<=NF;i++)if($i~/dev/)print $(i+1)}')
	IPV4_ADDRESS=$(ip -o -f inet addr show dev "$IPV4DEV" | awk '{print $4}' | awk 'END {print}')
}

# official pihole basic-install.sh code here
testIPv6() {
	first="$(cut -f1 -d":" <<< "$1")"
	value1=$(((0x$first)/256))
	value2=$(((0x$first)%256))
	((($value1&254)==252)) && echo "ULA" || true
	((($value1&112)==32)) && echo "GUA" || true
	((($value1==254) && (($value2&192)==128))) && echo "Link-local" || true
}

# official pihole basic-install.sh code here
getIPv6stuff()
{
	if [ -e /proc/net/if_inet6 ]; then
		IPV6_ADDRESSES=($(ip -6 address | grep 'scope global' | awk '{print $2}'))

		# Determine type of found IPv6 addresses
		for i in "${IPV6_ADDRESSES[@]}"; do
			result=$(testIPv6 "$i")
			[[ "${result}" == "ULA" ]] && ULA_ADDRESS="${i%/*}"
			[[ "${result}" == "GUA" ]] && GUA_ADDRESS="${i%/*}"
		done

		# Determine which address to be used: Prefer ULA over GUA or don't use any if none found
		if [[ ! -z "${ULA_ADDRESS}" ]]; then
			IPV6_ADDRESS="${ULA_ADDRESS}"
		elif [[ ! -z "${GUA_ADDRESS}" ]]; then
			IPV6_ADDRESS="${GUA_ADDRESS}"
		else
			IPV6_ADDRESS=""
		fi
	fi
}

# from official pihole basic-install.sh, almost
finalExports() {
    #If it already exists, lets overwrite it with the new values.
    if [[ -f ${setupVars} ]];then
        rm ${setupVars}
    fi
    {
    echo "PIHOLE_INTERFACE=${IPV4DEV}"
    echo "IPV4_ADDRESS=${IPV4_ADDRESS}"
    echo "IPV6_ADDRESS=${IPV6_ADDRESS}"
    echo "INSTALL_WEB_INTERFACE=true"
    echo "QUERY_LOGGING=true"
    }>> "${setupVars}"
}

getIPv4stuff
getIPv6stuff
finalExports
