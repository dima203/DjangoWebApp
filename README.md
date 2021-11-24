# DjangoWebApp

## Contents

1. [Installation](#Installation)       
2. [Cofiguration](#Configuration)   
3. [Run Server](#RunServer)

## <a name="Installation"></a> Installation

!!! You must have `Python 3.x` installed !!! 

1. Clone this repositories:    
```bash
git clone https://github.com/dima203/DjangoWebApp.git
```
2. Install Docker Compose:    
    https://docs.docker.com/compose/install/

## <a name="Configuration"></a> Configuration   

1. Open project catalog:    
```bash
cd DjangoWebApp
```
2. Create enviroment variables file "env_variables":      
```
DJANGO_DEBUG=""
DJANGO_SECRET_KEY="YOUR_SECRET_KEY"
```
3. Create project:    
```bash
docker-compose run web django-admin startproject test
```
4. Delete catalog test.       
5. Make migrations:
```bash
docker-compose run web python manage.py makemigrations
```
6. Migrate:
```bash
docker-compose run web python manage.py migrate
```
7. Create superuser:    
```bash
docker-compose run web python manage.py createsuperuser
```
8. Collect staticfiles:     
```bash
docker-compose run web python manage.py collectstatic
```

## <a name="RunServer"></a> Run Server      

1. Run server:      
```bash
docker-compose up
```
