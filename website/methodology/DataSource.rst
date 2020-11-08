.. discuss the first four columns .. no, because of true ups

.. _method-data-source:

Data Source
-----------

The data is sourced from the John's Hopkins github repository found
here

    https://github.com/CSSEGISandData/COVID-19

in the time series directory path
`csse_covid_19_data/csse_covid_19_time_series
<https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series>`_.
This directory contains two CSV source files used in this analysis,
one for `Confirmed Cases
<https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv>`_
and one for `Deaths
<https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv>`_.
The time series has a row for each jurisdiction, mostly counties, with
a column for each date since the beginning of somewhat systematic
epidemic data gathering, Jan 22, 2020.  There are additional columns
providing metadata like jurisdiction features including ISO and FIPS
naming as well as latitude and longitude. In the case of the `Deaths
<https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv>`_.
file, there is a metadata column with the population of the
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
another.  The `Hopkins github site
<https://github.com/CSSEGISandData/COVID-19>`_ details many of these
issues.

Also, many jurisdictions have experienced issues with their data
gathering and posting.  Further, the gathering and posting protocols
have evolved on a per jurisdiction basis. The extent to which
jurisdictions have corrected their historical issues and their
protocol changes is variable.

For example, the `Orange County covid website`__ had long warned of
issues with the CalREDIE reporting system; while those issues appear
to have been cured as of 8/12/20, the extent to which prior values are
corrected is unknown.

__ https://occovid19.ochealthinfo.com/coronavirus-in-oc

Another set of examples is common to :doc:`San Antonio, TX
</locs_autoX/BexarTX>` and :doc:`Manhattan (NYC), NY
</locs_autoX/NewYorkNY>` and potentially several/many more as we add
jurisdictions:

    For Daily Cases and/or Daily Deaths, there are one or more outlier
    datapoints.  The outlier appears to be more of a reporting
    artifact than a reflection of the activity for the specific day.
    Feel free to tweet any corrections to this observation.
