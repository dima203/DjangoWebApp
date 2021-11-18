# DjangoWebApp

## Contents

1. [Installation](#Installation)    
    1.1 [Linux](#InstallationLinux)    
    1.2 [Windows](#InstallationWindows)    
2. [Cofiguration](#Configuration)   

## <a name="Installation"></a> Installation

!!! You must have `Python 3.x` installed !!! 

### <a name="InstallationLinux"></a> Linux

1. Clone this repositories:    
```bash
    git clone https://github.com/dima203/DjangoWebApp.git
```
2. Install virtual enviroment:
```bash
    pip install virtualenv
```
3. Create new enviroment in application catalog:
```bash
    cd DjangoWebApp
    python3 -m venv env
```
4. Activate enviroment:
```bash
    source env/bin/activate
```
5. Install all requirements:
```bash
    pip install -r requirements.txt
```

### <a name="InstallationWindows"></a> Windows

1. Clone this repositories:    
```cmd
    git clone https://github.com/dima203/DjangoWebApp.git
```
2. Install virtual enviroment:
```cmd
    pip install virtualenv
```
3. Create new enviroment in application catalog:
```cmd
    cd DjangoWebApp
    python3 -m venv env
```
4. Activate enviroment:
```cmd
    env\Scripts\activate.bat
```
5. Install all requirements:
```cmd
    pip install -r requirements.txt
```

## <a name="Configuration"></a> Configuration

1. Make database migrations:    
```
    python manage.py makemigrations
```
2. Migrate:    
```
    python manage.py migrate
```
3. Create super user:    
```
    python manage.py createsuperuser
```
4. Start server:    
```
    python manage.py runserver
```
