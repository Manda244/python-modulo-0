#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/14 20:09:38 by marasolo            #+#    #+#            #
#   Updated: 2026/04/15 23:58:30 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{seed_type} seeds: {quantity} {unit} avaible")
    elif (unit == "grams"):
        print(f"{seed_type} seeds: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{seed_type} seeds: covered {quantity} square meters")
    else:
        print("Unknown unit type")
