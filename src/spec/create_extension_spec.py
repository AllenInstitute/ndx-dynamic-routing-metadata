# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec

# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        name="""ndx-dynamic-routing-metadata""",
        version="""0.1.0""",
        doc="""Type for storing metadata for dynamic routing project at Allen Institute""",
        author=[
            "Arjun Sridhar", 
            "Ben Hardcastle", 
            "Corbett Bennett", 
        ],
        contact=[
            "arjun.sridhar@alleninstitute.org", 
            "ben.hardcastle@alleninstitute.org", 
        ],
    )
    ns_builder.include_type('LabMetaData', namespace='core')
    
    # TODO: if your extension builds on another extension, include the namespace
    # of the other extension below
    # ns_builder.include_namespace("ndx-other-extension")

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/stable/tutorials/general/extensions.html
    # for more information
    DynamicRoutingMetadataExtension = NWBGroupSpec(
        neurodata_type_def="DynamicRoutingMetadataExtension",
        neurodata_type_inc="LabMetaData",
        doc="Type for storing metadata for dynamic routing project at Allen Institute"
    )

    DynamicRoutingMetadataExtension.add_attribute(
        name="is_ephys",
        doc='whether session has ephys recording',
        dtype='bool'
    )

    DynamicRoutingMetadataExtension.add_attribute(
        name="is_sync",
        doc='whether session has sync',
        dtype='bool'
    )

    DynamicRoutingMetadataExtension.add_attribute(
        name="is_task",
        doc='whether session has dynamic routing task',
        dtype='bool'
    )

    # TODO: add more attributes/groups as needed
    new_data_types = [DynamicRoutingMetadataExtension]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "spec"))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
