Graphs & Tables
===============

These are the graphs of selected locations in the US.

.. jinja:: file_base
   :debug:

   .. toctree::
      :maxdepth: 2
      :caption: Contents:
   {% for loc in locations %}
      ../graphs_autoX/{{ loc -}}
   {% endfor %}
