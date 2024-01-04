# Converting research data to NeXus

!!! danger "Work in progress"

    This part of the documentation is still being written and it might be confusing or incomplete.

## Who is this tutorial for?

The document is for people who want to standardize their research data by converting their research data into 
a NeXus standardized format.
We cover the basic principles and common principles of NeXus, here.
For a more detailed description on the general principles of NeXus we recommend reading our 
[learning page for NeXus](../learn/nexus-primer.md) or the [official NeXus user manual](https://manual.nexusformat.org/user_manual.html).

## What should you should know before this tutorial?

- You should have a basic understanding what an hdf5 file is and how to write it
- You should have a basic understanding of FAIR data [wilkinson et al](...)

## What you will know at the end of this tutorial?

You will have

- a basic understanding how to write a file according to a NeXus standard
- a basic understanding of common NeXus terminology

!!! info "NeXus path notations"

    There are several methods for referencing concepts or data paths within NeXus:

    - **Concept Path Notation:** This notation describes the hierarchical structure of NeXus concepts using class names. For example, `NXexperiment:/NXentry/NXinstrument/NXdetector` indicates the creation of a new NXdetector class within the NXexperiment concept. This path typically forms automatically when an application definition extends a base class's fields.

    - **Instance Path Notation:** It represents the actual location of a field or group in a NeXus data instance (e.g., an HDF5 file). An example is `my_file.nxs:/entry/instrument/detector`.

    - **Combined Notation:** This combines concept and instance paths. For example, `NXexperiment:/NXentry[my_file.nxs:entry]/NXinstrument[instrument]/NXdetector[detector]`. Here, concept paths are outside and instance paths within square brackets. The leftmost entries may include the NeXus class or file reference.

    - **Appdef Notation:** This format is used in application definitions, where uppercase indicates a selectable name and lowercase a fixed name. Examples include `NXexperiment:ENTRY[my_experiment.nxs:entry]/INSTRUMENT[instrument]/DETECTOR[detector]` and `NXexperiment:ENTRY[my_experiment.nxs:entry]/my_INSTRUMENT[my_instrument]/DETECTOR[detector]`.

