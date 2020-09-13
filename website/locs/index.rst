Jurisdiction Reports
====================

.. Show/hide part of text (question/answer) in sphinx file
   https://stackoverflow.com/questions/59679797/show-hide-part-of-text-question-answer-in-sphinx-file

.. jinja:: file_base
   :debug:

   .. toctree::
      :maxdepth: 2
      :Caption: Tables and plots for selected locations in the US:

   {% for loc in locations %}
      ../locs_autoX/{{ loc -}}
   {% endfor %}

