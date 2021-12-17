# Project Programming for Big Data
# Walk-in-Clinic

Walk in Clinic is a web-based application which will allow a clinic staff to handle their operations.
This application will accelerate the workflows and also it is a solutions to better connect patients and healthcare providers.

We have separate apps for both front-end and back-end
our SQLite Database file resides with in Walk-In-Clinic-BackEnd 


## Installation

* Install [node.js](https://nodejs.org/en/download/) v14.15.0
* Install [django](https://docs.djangoproject.com/en/4.0/topics/install/)
* Clone the Repository
* Open the cloned folder in terminal
* Use the [npm](https://www.npmjs.com/package/npm) package manager to install the required libraries

* For Front-End app (Walk-In-Clinic-FrontEnd) 
```bash
npm install --force
```

```bash
npm install -g angular-cli@12.1.2
```

```bash
ng build 
```

```bash
ng server 
```

* For Back-end API (Walk-In-Clinic-BackEnd) 
* Django APi setup

```bash
C:\Walk-In-Clinic-Backend>myenv\Scripts\activate
```
```bash
(myenv) C:\Walk-In-Clinic-Backend\cd DjangoAPI
```
```bash
(myenv) C:\Walk-In-Clinic-Backend\cd DjangoAPI
```
```bash
(myenv) C:\Walk-In-Clinic-Backend\DjangoAPI>python manage.py runserve
```
* Django Migration commands
```bash
(myenv) C:\Walk-In-Clinic-Backend\DjangoAPI>python manage.py makemigrations WalkinClinicApp
```
```bash
(myenv) C:\Walk-In-Clinic-Backend\DjangoAPI>python manage.py migrate WalkinClinicApp
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
