(setq comint-process-echoes t)

;;; update emacs' exec-path after you do pipenv shell
;;; run the result of this shell command in the *scratch* buffer
;;; echo "(add-to-list 'exec-path \"$(pipenv --venv)/bin\")"
;;; e.g.,
(add-to-list 'exec-path "/home/mark/.local/share/virtualenvs/sphinx_covid-Ri6Ep0nH/bin")

(setq electric-indent-mode nil)
