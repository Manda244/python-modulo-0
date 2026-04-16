#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/14 19:04:30 by marasolo            #+#    #+#            #
#   Updated: 2026/04/14 19:53:22 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_recursive(days, cnt) -> None:
    if days >= cnt:
        print(f"Day {cnt}")
        cnt += 1
        ft_recursive(days, cnt)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_recursive(days, 1)
    print("Harvest time!")
