.. _Spm-Structure:

===============================
Scanning Probe Microscopy
===============================

.. index::
   SpmAppDef

.. _SpmAppDef:

Application Definition
######################

    :ref:`NXspm`:
       An application definition for scanning Probe Microscopy domain experiments. 
       The :ref:`NXspm` in herited from the :ref:`NXsensor_scan` is considered as
       a as general structure for all SPM experiments.
    :ref:`NXsts`:
         The application definition NXsts for Scanning Tunneling Spectroscopy is 
         proxy to be used for STS experiments and it is inherited from the :ref:`NXspm`.
         The :ref:`NXsts` is an alias of the :ref:`NXspm` application definition.
    :ref:`NXstm`:
         An application definition for Scanning Tunneling Microscopy experiments 
         inherited from the :ref:`NXspm`.
    :ref:`NXafm`:
         An application definition for Atomic Force Microscopy experiments inherited
         from the :ref:`NXspm`.

.. _SpmNewBC:

Base Classes
############

    :ref:`NXlockin`:
    A base class to describe lock-in amplifier instrument.

    :ref:`NXspm_bias_spectroscopy`:
    A base class to describe bias spectroscopy measurement to measure I/V curve in STS expriment.

    :ref:`NXspm_cantilever`:
    A base class to characterize cantilever used in AFM experiments.
    
    :ref:`NXspm_cantilever_config`:
    A base class to describe cantilever configuration in AFM experiments.

    :ref:`NXspm_cantilever_oscillator`:
    A base class to describe cantilever oscillator in AFM experiments.

    :ref:`NXphase_lock_loop`:
    A base class to describe phase lock loop in AFM experiments.

   :ref:`NXspm_piezo_sensor`:
    A base class to describe piezo sensor in SPM experiments.

    :ref:`NXpiezo_config_spm`:
    A base class to describe piezo configuration in SPM experiments.

    :ref:`NXspm_piezo_sensor`:
    A base class to describe piezo sensor in SPM experiments.

    :ref:`NXspm_piezoelectric_material`:
    A base class to draw piezoelectric material properties used in cantilever tip.

    :ref:`NXspm_positioner`:
    A base class to describe PID positioner in SPM experiments.

    :ref:`NXspm_scan_control`:
   A base class to characterize the movement of scan probe in a multi-dimensional phase space. 

    :ref:`NXspm_scan_pattern`:
   A base class to define the pattern of a scan in a given scan region.

    :ref:`NXspm_scan_region`:
   A base class to define the phase space or sub-phase space for scan in SPM experiments.

    :ref:`NXspm_temperature_sensor`:
   A base class to describe temperature sensor in SPM experiments.
