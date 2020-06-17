# CasaSuggest

Setup Information

* Install venv 
`python3 -m pip install venv`
  
* Clone the git repository into this repository. Change directory into the same

* Initialize virtual env
 `python3 -m venv .`
 
* Activate virtual environment
 `source bin/activate`
 
* Install Django, Django Rest framework and Psycopg2 and Cors
```
  python3 -m pip install django
  python3 -m pip install djangorestframework
  python3 -m pip install psycopg2-binary
  python3 -m pip install django-cors-headers

```
* change directory into the CasaSuggest folder
* Run Migration
` python3 manage.py migrate CasaSuggestApp`
* Start Server
` python3 manage.py runserver 8080`


The service should now be available in PORT 8080. 

I've created a method for Campaign creation alone which can be tested by making the following URL call. 

```
curl --request POST \
  --url http://localhost:8080/api/campaign \
  --header 'content-type: application/json' \
  --data '{
	"tenantId": "1" ,
  "buId": "1",
 	"casaCampaignId": "1"
}'
```



