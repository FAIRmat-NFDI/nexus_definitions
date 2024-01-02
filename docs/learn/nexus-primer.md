# A primer on NeXus

!!! danger "Work in progress"

    This part of the documentation is still being written and it might be confusing or incomplete.

NeXus is is a description of a common data exchange format initially developed for neutron, X-ray, and muon experiments. Within FAIRmat we extensively extended the format to cover a range of experiments with major support for APM, ARPES, XPS, and optical spectroscpy but we also give advice and guidance for developing standards for other formats as well.

!!! info "NeXus as a tool for FAIR data"

    NeXus is supported be the research data management platform NOMAD.
    Experimental data following an NeXus application definition can easily be uploaded and is recognized by NOMAD's search system.
    If you want to learn more about uploading NeXus data to NOMAD, please refer to the [NeXus to nomad](./nexus-to-nomad.md) tutorial
    of this documentation.
    Accordingly, if you want to build data according to the FAIR principles, you can think of NeXus fulfilling the interoperability and
    reproducibility part and a research data management platform like NOMAD the findable and accessible part.

## Who is this tutorial for?

The document is for people who want to standardize their research data and want to understand the modelling principles
of NeXus definitions or who want to build their own application definition for an experiment.
We cover the basic principles and common principles of NeXus, here.
For a more detailed description we recommend reading the [official NeXus documentation](...).

## What should you should know before this tutorial?

- You should have a basic understanding what an hdf5 file is and how to write it
- You should have a basic understanding of FAIR data [wilkinson et al](...)

## What you will know at the end of this tutorial?

You will have

- a basic understanding how to write a file according to a NeXus standard
- an idea of how to start writing an NeXus application definition for your domain of research
- a basic understanding of common NeXus terminology


Concept of this tutorial:

Create an example file NXdouble_slit

NXslit_experiments --> NXdouble_slit
NXslit_experiments --> NXsingle_slit

They should learn the basic principles of how nexus works, the different path notations
- Principles of nexus
    - concepts
    - appdefs
    - base classes
- Inheritance of application definitions and base classes
- Connection of concept paths and instance paths
- Description of appdef/base class notation (upper and lower case)
- Basic tools for creation (pynxtools) and verification (pynxtools?) of nexus files

Additional information (i.e., not in this tutorial but linked to this):
- Creating a reader in pynxtools
- Reading/writing nexus data in nomad


!!! info "NeXus path notations"

    There are several methods for referencing concepts or data paths within NeXus:

    - **Concept Path Notation:** This notation describes the hierarchical structure of NeXus concepts using class names. For example, `NXexperiment:/NXentry/NXinstrument/NXdetector` indicates the creation of a new NXdetector class within the NXexperiment concept. This path typically forms automatically when an application definition extends a base class's fields.

    - **Instance Path Notation:** It represents the actual location of a field or group in a NeXus data instance (e.g., an HDF5 file). An example is `my_file.nxs:/entry/instrument/detector`.

    - **Combined Notation:** This combines concept and instance paths. For example, `NXexperiment:/NXentry[my_file.nxs:entry]/NXinstrument[instrument]/NXdetector[detector]`. Here, concept paths are outside and instance paths within square brackets. The leftmost entries may include the NeXus class or file reference.

    - **Appdef Notation:** This format is used in application definitions, where uppercase indicates a selectable name and lowercase a fixed name. Examples include `NXexperiment:ENTRY[my_experiment.nxs:entry]/INSTRUMENT[instrument]/DETECTOR[detector]` and `NXexperiment:ENTRY[my_experiment.nxs:entry]/my_INSTRUMENT[my_instrument]/DETECTOR[detector]`.
