.. discuss the first four columns .. no, because of true ups

.. _method-data-source:

Data Source
-----------

The data is sourced from the John's Hopkins github repository found
here::

    git@github.com:CSSEGISandData/COVID-19.git

in the time series directory path
``csse_covid_19_data/csse_covid_19_time_series``.  This directory
contains two CSV source files used in this analysis, one for Confirmed
Cases and one for Deaths.  The time series has a row for each
jurisdiction, mostly counties, with a column for each date since the
beginning of the epidemic.  There are additional columns providing
metadata like jurisdiction and its latitude and longitude. In the case
of the Deaths file, there is a column with the population of the
jurisdiction.  That is the source of the population statistic used in
the plots and tables.

.. jinja:: DataSource
   :debug:

   **Dataset's latest date**
      *{{ asof_date }}*

   **Git commit id for this dataset**
      *{{ commit_id }}*

   **Site Update Timestamp -- Pacific time**
      *{{ timestamp }}*

Data Limitations
^^^^^^^^^^^^^^^^

The data is aggregated from many sources and the details of gathering
and posting the specific data items may vary from one jurisdiction to
another.

Also, many jurisdictions have experienced issues with their data
gathering and posting.  The extent to which they have corrected their
historical issues may well be variable.  

For example, the `Orange County covid website`__ had long warned of
issues with the CalREDIE reporting system; while those issues appear
to have been cured on 8/12/20, the extent to which prior values are
corrected is unknown.

__ https://occovid19.ochealthinfo.com/coronavirus-in-oc

Another example is :doc:`San Antonio, TX </locs_autoX/BexarTX>`.
For Daily Cases and Daily Deaths, there appears to be an outlier
datapoint in mid and late July, repectively.  Those appear to be more
of a reporting artifact than a reflection of the activity for the
specific day.
