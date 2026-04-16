#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/14 17:38:22 by marasolo            #+#    #+#            #
#   Updated: 2026/04/14 19:03:39 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for jour in range(1, days + 1):
        print(f"Day {jour}")
    print("Harvest time!")
