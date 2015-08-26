
## Broker settings
BROKER_URL			= 'amqp://guest:guest@localhost:5672//'

## Backend settings
CELERY_RESULT_BACKEND		= 'rpc://'
CELERY_RESULT_PERSISTENT	= False

## List of modules to import when celery starts
CELERY_IMPORTS			= ('node.tasks', )

## Time and date settings
CELERY_ENABLE_UTC		= True
CELERY_TIMEZONE			= 'Europe/Zurich'


