.. _FairmatCover:

=======================
FAIRmat-NeXus Proposal
=======================

.. index::
   AimsContextualization
   Achievements
   Outreach
   VersionAlignment


.. _AimsContextualization:

Aims and contextualization
##########################

Organizing (meta)data for materials characterization calls for a mastering of formatting varieties and data volume handling while assuring semantic interpretability, validity, and keeping inaccuracies documented and controlled. Data schemas and file formats are the tools that enable a structured and semantically annotated storage and processing of research data. Frequently, these tools organize entities effectively as graph-based representations.
In practice, experimentalists need to navigate a tool landscape that is heterogeneous with different levels of (meta)data and information granularity,
different formatting, and differing semantic concepts. This reduces interoperability when working with the same data across different software tools
be this for research data management and documentation or data processing.

`NeXus <https://www.nexusformat.org/>`_ is a project for standardizing the formatting of (meta)data schema. NeXus is rooted in the condensed matter physics. The development of NeXus is coordinated by the `NeXus International Advisory Committee (NIAC) <https://www.nexusformat.org/NIAC.html>`_.

The FAIRmat-NeXus proposal is an interdisciplinary data-science- and semantic-technology-driven standardization project that extends NeXus beyond its original scope, which has been the standardization of neutron, x-ray, and muon experiments. The extensions from the FAIRmat-NeXus proposal cover the materials-science-branch of electron microscopy (EM), photoemission spectroscopy (PES), optical spectroscopy, standards for the field of atom probe tomography and related field-ion microscopy (atom probe microscopy), and contributed definitions for scanning probe microscopy. The FAIRmat proposal to NeXus is an effort by the community of scientists of the `FAIRmat consortium <https://www.fairmat-nfdi.eu/fairmat/about-fairmat/consortium-fairmat>`_. As a project which aims at creating an infrastructure for experimental data to be findable, accessible, interoperable, and reusable (FAIR) in the fields of condensed-matter physics and the chemical physics of solids, FAIRmat has adopted NeXus as the common format.

NeXus defines a set of data schemas. These define terms (concepts) with a controlled vocabulary and defined further semantic relations between concepts, including definitions for specifying details how (meta)data instances should be recorded for file based storage. NeXus definitions are version-controlled. Software tools are provided by members of the NIAC and the FAIRmat consortium for checking and verifying if specific instances of NeXus files are compliant with the specific versioned schema definitions. The file format most commonly used with NeXus is the Hierarchical Data Format (`HDF5 <https://www.hdfgroup.org/solutions/hdf5/>`_) but using other file formats is also possible.

Base classes (:ref:`base.class.definitions`) and application definitions (:ref:`application.definitions`) are the two key components of the NeXus data model. A base class represents a set of concepts, (meta)data (categorical or numerical) which specify details about e.g., scientists, projects, instruments, and other physical devices. NeXus includes also base classes with concepts to document (meta)data of associated computational analyses and data processing steps. Application definitions are constructed from combining such experiment- and research-question-specific base classes. In effect, an application definition is a data contract between a producer and a consumer of (meta)data. Humans or software are the contractual partners. This design has sufficient flexibility to cover any experimental technique and instrumentation, while ensuring rigorous, application-specific structures that can be processed in an automated manner. Representing a panel of scientists with cross-disciplinary expertise, the role of the NIAC ranges from offering support with community consensus building and technical reviewing.


.. _Achievements:

Achievements
############

Within the five years funding of the FAIRmat project, we have achieved a substantiated broadening of the experimental techniques that NeXus covers. This manual details these achievements for each technique and connects to the contents of the official NeXus User Manual (`see <https://manual.nexusformat.org/user_manual.html>`_). Here, we compile both efforts into one documentation for making the exploring of NeXus more convenient for users. The content of the FAIRmat-NeXus proposal has been successfully accepted as a standard, after several community discussions at international meetings with the NIAC. Decisions were made public with the `v2025.11 <https://github.com/nexusformat/definitions/releases/tag/v2025.11>`_ and the `v2026.01 <https://github.com/nexusformat/definitions/releases/tag/v2026.01>`_ releases.

However, developing data schemas alone is insufficient for making research data management an effective reality. Instead, also examples are required that prove these schemas turn out useful in practice and production environments. Therefore, perhaps the greatest resource of the coordinated work between the NeXus community and the FAIRmat consortium has been the inclusion of experimental datasets in the `NOMAD Laboratory <https://nomad-lab.eu>`_ while assuring that these store along the definitions of the FAIRmat-NeXus proposal.


.. _Outreach:

Outreach to the community
#########################

If you apply any of the characterization methods described here and are interested in producing FAIR data and using the FAIRmat tools, we invite you to try out our proposed data structure. If you find any conflicts or inconsistencies, please create an issue on the `GitHub repository of the project <https://github.com/FAIRmat-NFDI/nexus_definitions/issues>`_ or leave note in the comment section (that is implemented with `Hypothesis <https://web.hypothes.is/>`_). Feel also very much invited to contact us directly at the `FAIRmat-Team <https://www.fair-di.eu/fairmat/about-fairmat/team-fairmat>`_.


.. _VersionAlignment:

Conceptual alignment of the official NIAC repository and its FAIRmat-NeXus fork
###############################################################################

NeXus definitions are version controlled. Different GitHub repositories exists where these versions are stored: One is the `official NeXus repository <https://github.com/nexusformat/definitions>`_ that is maintained by the NIAC. Another one, representing a fork of this NIAC repository, is the `FAIRmat nexus_definitions repository <https://github.com/FAIRmat-NFDI/nexus_definitions>`_. As FAIRmat we assure to keep the `fairmat branch of the nexus_definitions <https://github.com/FAIRmat-NFDI/nexus_definitions/tree/fairmat>`_ branch up-to-date with the `main branch of the official definitions <https://github.com/nexusformat/definitions/tree/main>`_ that is being maintained by the NIAC. Updates will be synced to bring back content from official releases issued by the NIAC. This assures that each version of the definitions from the FAIRmat-NeXus proposal remains as closely as possibly semantically aligned with a version published by the NIAC. At the same time this approach ensures that the development speed and update cycles of FAIRmat and the NIAC can be different and do not block each other. Maintaining and minimizing though semantic mismatch is key. It is possible that specific application definitions and base classes of the FAIRmat-NeXus proposal may contain additional concepts that have not yet been brought back or standardized by the NIAC. We avoid though a relaxing of requirement constraints for concepts within in the FAIRmat definitions when compared to the closest matching versions of these concepts in the official definitions. Occasionally, additional optional concepts for specific FAIRmat definitions may extend the official definitions.


