#!/bin/bash

setupVars=/etc/pihole/setupVars.conf

# official pihole basic-install.sh code here
getIPv4stuff()
{
	IPV4DEV=$(ip route get 8.8.8.8 | awk '{for(i=1;i<=NF;i++)if($i~/dev/)print $(i+1)}')
	# change local ip to unusable 0.0.0.0 (ref. http://dlaa.me/blog/post/skyhole), and :: for ipv6
	IPV4_ADDRESS="0.0.0.0"
}

# official pihole basic-install.sh code here
getIPv6stuff()
{
	if [ -e /proc/net/if_inet6 ]; then
		# change local ip to unusable 0.0.0.0 (ref. http://dlaa.me/blog/post/skyhole), and :: for ipv6
		IPV6_ADDRESS="::"
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
    echo "INSTALL_WEB_INTERFACE=false"
    echo "QUERY_LOGGING=true"
    }>> "${setupVars}"
}

getIPv4stuff
getIPv6stuff
finalExports
