.. _FairmatCover:

=======================
FAIRmat-NeXus Proposal
=======================

.. index::
   Achievements
   Outreach
   WhichData
   VersionAlignment

Aim
#########################

Organizing (meta)data for materials characterization calls for a mastering of formatting varieties and data volume handling while assuring semantic interpretability, validity, and keeping inaccuracies documented and controlled. Data schemas and file formats are the tools that enable a structured and semantically annotated storage and processing of research data. Frequently, these tools organize entities effectively as graph of materials data. Experimentalists face the challenge that these schemas and graph-based representations often use different levels of (meta)data and information granularity, different formatting, and different semantic concepts. This causes limited interoperability.

`NeXus <https://www.nexusformat.org/>`_ is a (meta)data schema and formatting standardization that is rooted in the condensed matter physics. The development of NeXus is coordinated by the NeXus International Advisory Committee (NIAC).

The NeXus-FAIRmat proposal is an interdisciplinary data-science- and semantic-technology-driven standardization project that extends NeXus beyond its original scope (neutron, x-ray, and muon experiments). These extensions cover the materials-science-branch of electron microscopy (EM), photo-emission spectroscopy (PES), optical spectroscopy, and standards for the field of atom probe tomography and related field-ion microscopy (atom probe microscopy). The FAIRmat proposal to NeXus is an effort by the community of scientists of the `FAIRmat consortium <https://www.fairmat-nfdi.eu/fairmat/about-fairmat/consortium-fairmat>`_. As a project which aims at creating an infrastructure for experimental data to be findable, accessible, interoperable, and reusable (FAIR) in the fields of condensed-matter physics and the chemical physics of solids, FAIRmat has adopted NeXus as the common format.

NeXus defines a set of data schemas. These define terms (concepts) with a controlled vocabulary and defined relations between the concepts including definitions for specifying details how (meta)data instances should be recorded for file based storage. NeXus definitions are version-controlled. Software tools are provided by members of the NIAC and FAIRmat for checking and verifying if specific instances of NeXus files comply with the intended
schema definitions. The file format most commonly used with NeXus is the Hierarchical Data Format (`HDF5 <https://www.hdfgroup.org/solutions/hdf5/>`_) but using other file formats is also possible.

Base classes (:ref:`base.class.definitions`) and application definitions (:ref:`application.definitions`) are the two key components of the NeXus data model. A base class represents a set of concepts, (meta)data (categorical or numerical)which specify details about e.g., scientists, projects, instruments, and other physical devices. NeXus includes also base classes with concepts to document (meta)data of associated computational analyses and data processing steps. Application definitions are constructed from combining such experiment- and research-question-specifically customized base classes. In effect, an application definition is a data contract between a producer and a consumer of (meta)data. Humans or software are the contractual partners. This design has sufficient flexibility to cover any experimental technique and instrumentation, while ensuring rigorous, application-specific structures that can be processed in an automated manner. Representing a panel of scientists with cross-disciplinary expertise, the role of the NIAC ranges from offering support with community consensus building and technical reviewing.

.. _Achievements:

Achievements
############

Within the five years funding of the FAIRmat project, we have achieved a substantiated broadening of the experimental techniques that NeXus covers. This manual details these achievements for each technique and connects to the contents of the official NeXus User Manual (also available `here <https://manual.nexusformat.org/user_manual.html>`_) that has been here compiled into one documentation for making the exploring of NeXus more convenient for users. The contents of the NeXus-FAIRmat proposal have successfully been accepted as a standard after community discussions with the NIAC. Decisions were made public via the `v2025.11 <https://github.com/nexusformat/definitions/releases/tag/v2025.11>`_ and the `v2026.01 <https://github.com/nexusformat/definitions/releases/tag/v2026.01>`_ releases.

For making effective research data management a reality though developing data schemas alone is insufficient. One also needs to prove that these schemas are useful in practice. Therefore, perhaps the greatest resource, of the coordinated
work between the NeXus community and FAIRmat has been the inclusion of experimental datasets in the `NOMAD Laboratory <https://nomad-lab.eu>`_ while assuring these to store along the definitions of the NeXus-FAIRmat proposal.


.. _Outreach:

Outreach to the community
#########################

If you are applying any of the here detailed characterization methods and you are interested in producing FAIR data and accessing the FAIRmat tools, we invite you to try out our proposed structure. If you find any conflicts or inconsistencies, please raise them to us using the comment section (implemented with `Hypothesis <https://web.hypothes.is/>`_) or reporting an issue on the `GitHub repository of the project <https://github.com/FAIRmat-NFDI/nexus_definitions/issues>`_. Feel also very much invited to contact us directly at the `FAIRmat-Team <https://www.fair-di.eu/fairmat/about-fairmat/team-fairmat>`_.


.. _WhichData:

Which data should I convert?
############################

You are free to choose at which point in the workflow you wish to convert the data to NeXus, as its flexibility allows to
describe raw data, pre-processed data and fully processed data. As an entry step, we suggest to use a test dataset
that is fully processed and already published (or, alternatively, of negligible scientific content). These datasets, indeed, require often the most 
extensive metadata description, but are most easily converted to NeXus, with minimal to no impact on the data processing pipeline.

In fact, a low barrier (but high yield!) way to participate to FAIRmat consists in converting only fully processed datasets that 
are used for a publication, and publishing them via FAIRmat only when your manuscript is in press. This makes the task of 
converting to NeXus much more sporadic than fairifying raw data, to the point that it may be even acceptable not to automate it. At the same time, 
it guarantees full control on the data until publication. We are confident that if you take this approach, more appetite will come with eating,
and you will be naturally inclined to gradually integrate FAIRmat structures and tools further in your workflow. 


.. _VersionAlignment:

Alignment of the definitions on the official NIAC repository and its NeXus-FAIRmat fork
#######################################################################################

TODO


