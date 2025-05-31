#!/bin/bash

source /opt/pihole/basic-install.sh

setupVars=/etc/pihole/setupVars.conf

# official pihole basic-install.sh code here
find_IPv4_information() {
    # Detects IPv4 address used for communication to WAN addresses.
    # Accepts no arguments, returns no values.

    # Named, local variables
    local route
    local IPv4bare

    # Find IP used to route to outside world by checking the route to Google's public DNS server
    route=$(ip route get 8.8.8.8)

    # Get just the interface IPv4 address
    # shellcheck disable=SC2059,SC2086
    # disabled as we intentionally want to split on whitespace and have printf populate
    # the variable with just the first field.
    printf -v IPv4bare "$(printf ${route#*src })"

    if ! valid_ip "${IPv4bare}"; then
        IPv4bare="127.0.0.1"
    fi

    # Append the CIDR notation to the IP address, if valid_ip fails this should return 127.0.0.1/8
    IPV4_ADDRESS=$(ip -oneline -family inet address show | grep "${IPv4bare}/" | awk '{print $4}' | awk 'END {print}')

    IPV4DEV=$(ip route get 8.8.8.8 | awk '{for(i=1;i<=NF;i++)if($i~/dev/)print $(i+1)}')
}

# official pihole basic-install.sh code here
# This lets us prefer ULA addresses over GUA
# This caused problems for some users when their ISP changed their IPv6 addresses
# See https://github.com/pi-hole/pi-hole/issues/1473#issuecomment-301745953
testIPv6() {
    # first will contain fda2 (ULA)
    printf -v first "%s" "${1%%:*}"
    # value1 will contain 253 which is the decimal value corresponding to 0xFD
    value1=$(((0x$first) / 256))
    # value2 will contain 162 which is the decimal value corresponding to 0xA2
    value2=$(((0x$first) % 256))
    # the ULA test is testing for fc00::/7 according to RFC 4193
    if (((value1 & 254) == 252)); then
        # echoing result to calling function as return value
        echo "ULA"
    fi
    # the GUA test is testing for 2000::/3 according to RFC 4291
    if (((value1 & 112) == 32)); then
        # echoing result to calling function as return value
        echo "GUA"
    fi
    # the LL test is testing for fe80::/10 according to RFC 4193
    if (((value1) == 254)) && (((value2 & 192) == 128)); then
        # echoing result to calling function as return value
        echo "Link-local"
    fi
}

# official pihole basic-install.sh code here
find_IPv6_information() {
    # Detects IPv6 address used for communication to WAN addresses.
    mapfile -t IPV6_ADDRESSES <<<"$(ip -6 address | grep 'scope global' | awk '{print $2}')"

    # For each address in the array above, determine the type of IPv6 address it is
    for i in "${IPV6_ADDRESSES[@]}"; do
        # Check if it's ULA, GUA, or LL by using the function created earlier
        result=$(testIPv6 "$i")
        # If it's a ULA address, use it and store it as a global variable
        [[ "${result}" == "ULA" ]] && ULA_ADDRESS="${i%/*}"
        # If it's a GUA address, use it and store it as a global variable
        [[ "${result}" == "GUA" ]] && GUA_ADDRESS="${i%/*}"
        # Else if it's a Link-local address, we cannot use it, so just continue
    done

    # Determine which address to be used: Prefer ULA over GUA or don't use any if none found
    # If the ULA_ADDRESS contains a value,
    if [[ -n "${ULA_ADDRESS}" ]]; then
        # set the IPv6 address to the ULA address
        IPV6_ADDRESS="${ULA_ADDRESS}"
        # Show this info to the user
        printf "  %b Found IPv6 ULA address\\n" "${INFO}"
    # Otherwise, if the GUA_ADDRESS has a value,
    elif [[ -n "${GUA_ADDRESS}" ]]; then
        # Let the user know
        printf "  %b Found IPv6 GUA address\\n" "${INFO}"
        # And assign it to the global variable
        IPV6_ADDRESS="${GUA_ADDRESS}"
    # If none of those work,
    else
        printf "  %b Unable to find IPv6 ULA/GUA address\\n" "${INFO}"
        # So set the variable to be empty
        IPV6_ADDRESS=""
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
    echo "QUERY_LOGGING=true"
	echo "PIHOLE_DNS_1=1.1.1.1"
	echo "PIHOLE_DNS_2=8.8.8.8"
    }>> "${setupVars}"
}

find_IPv4_information
find_IPv6_information
finalExports
