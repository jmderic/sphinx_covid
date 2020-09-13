.. jinja:: <loc>
   :header_char: =
   :debug:

   {{ web_name }}
   {{ options.header_char * web_name|length }}

   {% if web_name != web_detail %}
   This page is advertised as {{ web_name }} for easy recognition, but
   the actual jurisdiction for which the data is presented is
   {{ web_detail }}.
   {% endif %}

   {% if web_name != web_detail -%}
   **Population, {{ web_detail }}**
   {%- else %}
   **Population**
   {%- endif %}
     *{{ Pop }}*

   .. table:: Current Case Data
      :align: center

      +-------------+---------+---------+-----------+-----------+
      |             |         | {{- day_hdr -}} |
      +-------------+---------+---------+-----------+-----------+
      |             |  Total  |  Cases  | 7 day avg | 8 day EMA |
      +=============+=========+=========+===========+===========+
      |    Cases    | {{- case.tot -}} | {{- case.day -}} | {{- case.abk -}} | {{- case.ema -}} |
      +-------------+---------+---------+-----------+-----------+
      | per 100,000 | {{- case.tot_p100 -}} | {{- case.day_p100 -}} | {{- case.abk_p100 -}} | {{- case.ema_p100 -}} |
      +-------------+---------+---------+-----------+-----------+

   .. table:: Peak Case Data
      :align: center

      +-------------+----------+-----------+-----------+
      |             |   Peak   | 7 day avg | 8 day EMA |
      +=============+==========+===========+===========+
      |    Cases    | {{- case_pk.day -}} | {{- case_pk.abk -}} | {{- case_pk.ema -}} |
      +-------------+----------+-----------+-----------+
      | per 100,000 | {{- case_pk.day_p100 -}} | {{- case_pk.abk_p100 -}} | {{- case_pk.ema_p100 -}} |
      +-------------+----------+-----------+-----------+
      |    Date     | {{- case_pk.day_date -}} | {{- case_pk.abk_date -}} | {{- case_pk.ema_date -}} |
      +-------------+----------+-----------+-----------+

   .. note::

      On most browsers you can right click on any of the plots below
      and select "Open image in new tab".  This will give you a larger
      plot at which to look.  The plots use the SVG format so they
      scale very well.

   .. image:: /images_autoX/{{images.Cases}}

   .. table:: Current Death Data
      :align: center

      +-------------+---------+---------+-----------+-----------+
      |             |         | {{- day_hdr -}} |
      +-------------+---------+---------+-----------+-----------+
      |             |  Total  |  Deaths | 7 day avg | 8 day EMA |
      +=============+=========+=========+===========+===========+
      |    Deaths   | {{- death.tot -}} | {{- death.day -}} | {{- death.abk -}} | {{- death.ema -}} |
      +-------------+---------+---------+-----------+-----------+
      | per 100,000 | {{- death.tot_p100 -}} | {{- death.day_p100 -}} | {{- death.abk_p100 -}} | {{- death.ema_p100 -}} |
      +-------------+---------+---------+-----------+-----------+

   .. table:: Peak Death Data
      :align: center

      +-------------+----------+-----------+-----------+
      |             |   Peak   | 7 day avg | 8 day EMA |
      +=============+==========+===========+===========+
      |    Deaths   | {{- death_pk.day -}} | {{- death_pk.abk -}} | {{- death_pk.ema -}} |
      +-------------+----------+-----------+-----------+
      | per 100,000 | {{- death_pk.day_p100 -}} | {{- death_pk.abk_p100 -}} | {{- death_pk.ema_p100 -}} |
      +-------------+----------+-----------+-----------+
      |    Date     | {{- death_pk.day_date -}} | {{- death_pk.abk_date -}} | {{- death_pk.ema_date -}} |
      +-------------+----------+-----------+-----------+

   .. image:: /images_autoX/{{images.Deaths}}

   .. table:: Active Case Data
      :align: center

      +-------------+----------+----------+
      |             |   Peak   | Current  |
      +=============+==========+==========+
      |    Active   | {{- active_pk.day -}} | {{- active.day -}} |
      +-------------+----------+----------+
      | per 100,000 | {{- active_pk.day_p100 -}} | {{- active.day_p100 -}} |
      +-------------+----------+----------+
      |    Date     | {{- active_pk.day_date -}} | {{- active.day_date -}} |
      +-------------+----------+----------+

   .. image:: /images_autoX/{{images.Active}}
