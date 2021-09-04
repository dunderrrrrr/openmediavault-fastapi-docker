# FastAPI for OpenMediaVault - docker


This API is based on [orrpan/python-openmediavault](https://github.com/orrpan/python-openmediavault) and [tiangolo/fastapi](https://github.com/tiangolo/fastapi).


![](https://i.imgur.com/NQytJ89.png)
___

**ovm-fastapi** is an api connected to your existing [OpenMediaVault](https://www.openmediavault.org/) nas or server. With this api you will be able to read:

* Host - cpu load, memory etc.
* Volumes - size, status
* Disks - temps, smart-status
* Raids - devices, status
* Fans - temperature
* Temps - temperature
* Services - all enabled services

* Detailed data:
	* Detailed storage
	* Detailed host
___

### Installation

First, make sure you edit and copy `settings.sample.py` to fit your needs.  
```
$ cp settings.sample.py settings.py
$ nano settings.py
```

To start the container with docker-compose:
```
$ docker-compose up -d
```

Your application will start on [http://yourhost:8000](http://yourhost:8000).   
Docs and redoc can be fould at [http://yourhost:8000/redoc](http://yourhost:8000/redoc) and [http://yourhost:8000/docs](http://yourhost:8000/docs).

---

Or you can build it yourself and start the container manually:
```
$ docker build --tag openmediavault-fastapi .
[...]
$ docker run -d -p 8000:8000 openmediavault-fastapi
```

Or create a virtualenv and run uvicorn:
```
$ mkvirtualenv omv-fastapi
$ pip install -r requirements.txt
$ uvicorn main:app --reload --host 0.0.0.0 --port 8000
````

___

### Paths

```
{
   "path":"/openapi.json",
   "name":"openapi"
},
{
   "path":"/docs",
   "name":"swagger_ui_html"
},
{
   "path":"/docs/oauth2-redirect",
   "name":"swagger_ui_redirect"
},
{
   "path":"/redoc",
   "name":"redoc_html"
},
{
   "path":"/",
   "name":"main"
},
{
   "path":"/host",
   "name":"host"
},
{
   "path":"/volumes",
   "name":"volumes"
},
{
   "path":"/disks",
   "name":"disks"
},
{
   "path":"/raids",
   "name":"raids"
},
{
   "path":"/fans",
   "name":"fans"
},
{
   "path":"/temps",
   "name":"temps"
},
{
   "path":"/services",
   "name":"services"
},
{
   "path":"/detailed_storage",
   "name":"volumes"
},
{
   "path":"/detailed_host",
   "name":"volumes"
}
```
