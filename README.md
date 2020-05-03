# watson-project
Django API with IBM watson integration

prerequisite:
DJANGO_SECRET_KEY=`b(!7!3w7*mr1$w=eyxpupu&50q-0@()l-w@q36x70cavo_(1fw`
WATSON_API_KEY=`watson-api-key-value`
WATSON_COLLECTION_ID=`watson-collection-id`
WATSON_CONFIGURATION_ID=`watson-configuration-id`
WATSON_ENVIRONMENT_ID=`watson-environment-id`
WATSON_SERVICE_BASE_URL=`https://api.eu-gb.discovery.watson.cloud.ibm.com`

put all this variable value into .envvars file.
How to run application:
* Run `docker-compose up --build admin`
* To hit the end-point:
0.0.0.0:8000/integration/