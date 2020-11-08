.. -*- coding: utf-8 -*-

.. organize section decoration according to the Python's Style Guide
   for documenting as given here:
   https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#sections

   # with overline, for parts
   * with overline, for chapters
   =, for sections
   -, for subsections
   ^, for subsubsections
   ", for paragraphs

   We start assuming our "top level" is a chapter

*******************************
Tables and Plots, Updated Daily
*******************************

This site shows time series plots and summary tables of Wuhan
Coronavirus (a.k.a., Covid-19) data for selected jurisdictions.

The subject data includes confirmed cases and deaths as reported by
:ref:`Johns Hopkins CCSE <method-data-source>`.  It also includes
information :ref:`estimated <esimating-recovered>` from that core
data, Recovered and Active cases.

.. toctree::
   :maxdepth: 2

   methodology/index
   locs/index

	      
Reference
---------

* :ref:`genindex`
* :ref:`search`
