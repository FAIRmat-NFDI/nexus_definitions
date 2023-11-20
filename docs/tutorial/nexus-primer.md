# A primer on NeXus

NeXus is is a description of a common data exchange format initially developed for neutron, X-ray, and muon experiments. Within FAIRmat we extensively extended the format to cover a range of experiments with major support for APM, ARPES, XPS, and optical spectroscpy but we give advince and guidance for developing standards for other formats as well.

Who is this tutorial for?

The document is for people not familiar with nexus to understand what it is doing and why it is useful.

What should people know before this tutorial?

- They should have a basic understanding what an hdf5 file is and how to write it
- They should have basic programming skills

What should people learn from this tutorial?

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

    ToDo: Clarify different path notations. We have one notation for the actual NeXus class. One for the appdef path and one in the actual instance. It still has to be clarified how we want to address when we add something like `my_INSTRUMENT` in an application definition. How would this translate to concept path?

    - **Concept path notation:** The concept path is a description of the path of a concept, e.g. `/NXentry/NXinstrument/NXdetector`
    - **Expanded concept path notation:** `NXexperiment:NXentry/NXinstrument/NXdetector`
    - **Instance path notation:** `/entry/instrument/detector`
    - **Combined notation:** `/NXentry[entry]/NXinstrument[instrument]/NXdetector[detector]`, Something like `/ENTRY[entry]/INSTRUMENT[instrument]/NXinstrument:my_DETECTOR[my_detector]` for partly variable data??
    - **Expanded combined notation:** `NXexperiment:NXentry[my_experiment.nxs:entry]/NXinstrument[instrument]/NXdetector[detector]`
