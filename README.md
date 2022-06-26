## Introduction
 - [HTML/CSS template used in this project](https://www.free-css.com/free-css-templates/page276/adward)
 - Comments and code is written semi Polish, so it is easier for me to explain code to my GF  
 - This is website prototype for my girlfirend's math school, she will start up in the future  😆
 - To inspect website, download .pdf file located in project files
## FAQ

#### Do photos on site show prawdziwych założycieli szkoły i nauczycieli?

No, these are stock photos.

## Features

-contact form sendig messages to school's email 


## Added to settings.py 

For sending mail (gmail):

`EMAIL_USE_TLS = True`

`EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'`

`EMAIL_HOST = 'smtp.gmail.com'`

`EMAIL_PORT = '587'`

`EMAIL_HOST_USER = '' `

`EMAIL_HOST_PASSWORD = ''` 

PASSWORD GENERATED at https://myaccount.google.com/apppasswords
 TWO-STEP VERIFICATION SHOULD BE TURNED ON
  (GMAIL TURN OFF THE ACCESS OPTIONS FOR EXTERNAL APPLICATIONS
FROM MAY 2022)