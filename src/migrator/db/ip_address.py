#
# Migrator tool for phpIPAM-NetBox
# migrator/db/ip/address.py - Internet Protocol (IP) addresses
#
# Copyright (c) 2017 Catalyst.net Ltd
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


'''
Internet Protocol (IP) addresses.
'''


import ipaddress

from migrator.db.object import Object


class Address(Object):
    '''
    Database type for Internet Protocol (IP) subnet prefixes.
    '''


    def __init__(self,
                 address_id,
                 address,
                 description=None,
                 custom_fields=None,
                 status_id=None, nat_inside_id=None, nat_outside_id=None,
                 interface_id=None, vrf_id=None, tenant_id=None):
        '''
        VLAN object constructor.
        '''

        # Initialise database object with ID.
        super.__init__(address_id, None, description)

        # Internal fields.
        self.address = ipaddress.ip_address(address)
        self.family = 6 if isinstance(self.prefix, ipaddress.IPv6Address) else 4
        self.custom_fields = tuple(custom_fields)

        # External fields.
        self.status_id = status_id
        self.nat_inside_id = nat_inside_id
        self.nat_outside_id = nat_outside_id

        # Grouping fields, in ascending order of scale.
        self.interface_id = interface_id
        self.vrf_id = vrf_id
        self.tenant_id = tenant_id