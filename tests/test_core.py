import ndx_dynamic_routing_metadata

import os
import unittest
from datetime import datetime
from pynwb import NWBHDF5IO, NWBFile
from ndx_dynamic_routing_metadata import DynamicRoutingMetadataExtension


def test_import_package():
    pass

"""Unit and integration tests for the DynamicRoutingMetadata extension neurodata type.

TODO: Modify these tests to test your extension neurodata type.
"""

class DynamicRoutingMetaDataExtensionTest(unittest.TestCase):
    def setUp(self):
        self.nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

    def test_add_lab_metadata(self):
        # Creates LabMetaData container
        self.setUp()

        lab_metadata_dict = dict(
            name='DynamicRoutingMetadata', # name of key in nwb 
            is_sync=True,
            is_ephys=True,
            is_task=True,
        )

        lab_metadata = DynamicRoutingMetadataExtension(**lab_metadata_dict)

        # Add to file
        self.nwbfile.add_lab_meta_data(lab_metadata)

        filename = 'test_labmetadata.nwb'

        with NWBHDF5IO(filename, 'w') as io:
            io.write(self.nwbfile)

        with NWBHDF5IO(filename, mode='r', load_namespaces=True) as io:
            nwbfile = io.read()

            for metadata_key, metadata_value in lab_metadata_dict.items():
                self.assertEqual(metadata_value, getattr(nwbfile.lab_meta_data['DynamicRoutingMetadata'], metadata_key))

        os.remove(filename)

