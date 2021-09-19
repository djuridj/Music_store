### How to start the app:
#### Start Elasticsearch
1. download and open the ES folder
2. run ES - `.\bin\elasticsearch.bat`

#### Start Django app (audio files are missing, so it's not possible to stream music until those files are reuploaded)
1. clone and open the app folder
2. make migrations `python3 manage.py makemigrations`
3. run the app - `python3 manage.py runserver`

#### PIP's needed
##### Rest is installed but not used atm
`pip install djangorestframework`
##### Markdown support for the browsable API.
`pip install markdown`
##### filters needed for advanced search
`pip install django-filter`
##### Used for BPM calculations
`pip install librosa`
##### Used for song durations
`python3 -m pip install mutagen`
##### Python imaging library
`python3 -m pip install --upgrade Pillow`
##### Templates rendering
`pip install django-widget-tweaks`



### BUGS
1. Dark mode works only when clicked on the button. When you change or refresh the page, it turns back to light mode.
2. Sorting on home page is not working well when toggling between card/list and sort options.
3. Album format concept is completely ignored in ordering of the albums.
4. Some of the song model fields could be added or filled in automatically, for example lyrics and key words
5. Automated fields in Song model - BPM and durration, work only if the file is already uploaded and you edit and save the Song.
