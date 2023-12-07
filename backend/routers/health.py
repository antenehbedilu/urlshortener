from fastapi import APIRouter, status

#create an instance of APIRouter
router = APIRouter(
    prefix='/api', #set the prefix for all routes under this router
    tags=['HealthChecks'] #assign tags to the router for documentation purposes
)

#endpoint for health check
@router.get('/health', status_code=status.HTTP_200_OK)
def health():
    return {'status': 'OK'}
