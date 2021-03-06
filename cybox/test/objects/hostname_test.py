# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.hostname_object import Hostname
from cybox.test.objects import ObjectTestCase


class TestHostname(ObjectTestCase, unittest.TestCase):
    object_type = "HostnameObjectType"
    klass = Hostname

    _full_dict = {
        'is_domain_name': True,
        'hostname_value': "www.example.com",
        'naming_system': ["DNS", "NETBIOS"],
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
