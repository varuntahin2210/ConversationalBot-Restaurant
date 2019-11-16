About the project
==================
The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.

The bot takes the following inputs from the user:
1. City: Take the input from the customer as a text field. It works only in Tier-1 and Tier-2 cities, while for tier-3 cities, it should reply back with something like "We do not operate in that area yet".. The bot can also identify common synonyms of city names, such as Bangalore/Bengaluru, Mumbai/Bombay etc.
2. Cuisine Preference: Take the cuisine preference from the customer. The bot list out the following six cuisine categories (Chinese, Mexican, Italian, American, South Indian & North Indian) and the customer can select any one out of that. 
3. Average budget for two people: Price range (average budget for two people) is segmented into three price categories: lesser than 300, 300 to 700 and more than 700. The bot ask the user to select one of the three price categories.

While showing the results to the user, the bot displays the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). 

Finally, the bot ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot ask for user’s email id and then send it over email. Else, just reply with a 'goodbye' message. The mail contains following details for each restaurant:
1. Restaurant Name
2. Restaurant locality address
3. Average budget for two people
4. Zomato user rating

Library Versions required for this project
===========================================
absl-py==0.8.1
APScheduler==3.6.1
astor==0.8.0
attrs==19.2.0
Automat==0.7.0
beautifulsoup4==4.8.0
bleach==1.5.0
blinker==1.4
boto3==1.5.20
botocore==1.8.50
certifi==2019.9.11
chardet==3.0.4
Click==7.0
cloudpickle==0.5.2
colorama==0.4.1
coloredlogs==10.0
colorhash==1.0.2
ConfigArgParse==0.13.0
constantly==15.1.0
cycler==0.10.0
cymem==1.31.2
cytoolz==0.9.0.1
decorator==4.4.0
dill==0.2.9
docopt==0.6.2
docutils==0.15.2
duckling==1.8.0
en-core-web-md==2.0.0
fakeredis==0.10.3
fbmessenger==5.6.0
Flask==1.1.1
Flask-Cors==3.0.8
Flask-Mail==0.9.1
future==0.16.0
gast==0.3.2
gevent==1.2.2
graphviz==0.8.4
greenlet==0.4.15
grpcio==1.24.1
h5py==2.10.0
html5lib==0.9999999
humanfriendly==4.18
hyperlink==17.3.1
idna==2.6
incremental==17.5.0
itsdangerous==1.1.0
jieba==0.39
Jinja2==2.10.3
jmespath==0.9.4
JPype1==0.6.2
jsonpickle==0.9.6
jsonschema==2.6.0
Keras==2.1.5
Keras-Applications==1.0.8
Keras-Preprocessing==1.1.0
klein==17.10.0
Markdown==3.1.1
MarkupSafe==1.1.1
matplotlib==2.1.0
mattermostwrapper==2.1
mkl-fft==1.0.14
mkl-random==1.1.0
mkl-service==2.3.0
msgpack==0.6.2
msgpack-numpy==0.4.4.3
msgpack-python==0.5.4
murmurhash==0.28.0
networkx==2.3
numpy==1.17.2
packaging==17.1
pandas==0.25.1
pathlib==1.0.1
plac==0.9.6
preshed==1.0.1
protobuf==3.10.0
PyHamcrest==1.9.0
PyJWT==1.7.1
pykwalify==1.6.0
pyparsing==2.4.2
pyreadline==2.1
PySocks==1.7.1
python-crfsuite==0.9.6
python-dateutil==2.8.0
python-telegram-bot==10.1.0
pytz==2019.3
PyYAML==3.12
rasa-core==0.10.1
rasa-nlu==0.12.3
redis==2.10.6
regex==2017.4.5
requests==2.18.4
ruamel.yaml==0.15.100
s3transfer==0.1.13
scikit-learn==0.19.1
scipy==1.1.0
simplejson==3.13.2
six==1.12.0
sklearn-crfsuite==0.3.6
slackclient==1.3.2
soupsieve==1.9.3
spacy==2.0.11
tabulate==0.8.5
tensorboard==1.8.0
tensorflow==1.8.0
termcolor==1.1.0
thinc==6.10.3
toolz==0.10.0
tqdm==4.19.5
twilio==6.31.1
Twisted==19.7.0
typing==3.6.2
tzlocal==2.0.0
ujson==1.35
urllib3==1.22
websocket-client==0.54.0
Werkzeug==0.16.0
wincertstore==0.2
wrapt==1.10.11
zope.interface==4.6.0