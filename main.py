from settings import omvuser, omvpasswd, omvhost, omvport
from omv.omv import Openmediavault
from fastapi import FastAPI
import requests, json

tags_metadata = [
    {
        "name": "host",
        "description": "OpenMediaVault host data and services.",
    },
    {
        "name": "storage",
        "description": "OpenMediaVault volume, disk and raid data.",
    },
    {
        "name": "health",
        "description": "OpenMediaVault health data, fans and temperature.",
    },

]

api = Openmediavault(omvhost, omvport, omvuser, omvpasswd, True)
app = FastAPI(openapi_tags=tags_metadata)

@app.get("/")
def main():
    url_list = [
        {
            "path": route.path,
            "name": route.name
        }
        for route in app.routes
    ]
    return url_list


@app.get("/host", tags=["host"])
def host():
    return_data = {
        "status_code": 200,
        "response": {
            "hostname": str(api.utilisation.hostname),
            "version": str(api.utilisation.version),
            "processor": str(api.utilisation.processor),
            "kernel": str(api.utilisation.kernel),
            "uptime": str(api.utilisation.up_time),
            "cpu_load": str(api.utilisation.cpu_total_load) + "%",
            "cpu_load_1min": str(api.utilisation.cpu_1min_load) + "%",
            "cpu_load_5min": str(api.utilisation.cpu_5min_load) + "%",
            "cpu_load_15min": str(api.utilisation.cpu_15min_load) + "%",
            "memory_total": str(api.utilisation.memTotal) + " KB",
            "memory_free": str(api.utilisation.memFree) + " KB",
            "memory_used": str(api.utilisation.memUsed) + " KB",
            "config_dirty": str(api.utilisation.configDirty),
            "rebootRequired": str(api.utilisation.rebootRequired),
            "pkgUpdatesAvailable": str(api.utilisation.pkgUpdatesAvailable)
        }
    }
    return (return_data)

@app.get("/volumes", tags=["storage"])
def volumes():
    volumes = api.storage.volumes
    volume_data = []
    for volume in volumes:
        vol = {}
        vol['id'] = str(volume)
        vol['status'] = str(api.storage.volume_status(volume))
        vol['device_type'] = str(api.storage.volume_device_type(volume))
        vol['mounted'] = str(api.storage._volume_mounted(volume))
        vol['size_total'] = str(api.storage.volume_size_total(volume))
        vol['size_used'] = str(api.storage.volume_size_used(volume))
        vol['size_used_p'] = str(api.storage.volume_percentage_used(volume)) + "%"
        vol['temp_avg'] = str(api.storage.volume_disk_temp_avg(volume))
        vol['temp_max'] = str(api.storage.volume_disk_temp_max(volume))
        volume_data.append(vol)
    return_data = {
        "status_code": 200,
        "response": volume_data
    }
    return (return_data)

@app.get("/disks", tags=["storage"])
def disks():
    disks = api.storage.disks
    disk_data = []
    for disk in disks:
        dis = {}
        dis['id'] = str(disk)
        dis['name'] = str(api.storage.disk_name(disk))
        dis['smart_status'] = str(api.storage.disk_smart_status(disk))
        dis['temp'] = str(api.storage.disk_temp(disk))
        disk_data.append(dis)
    return_data = {
        "status_code": 200,
        "response": disk_data
    }
    return (return_data)

@app.get("/raids", tags=["storage"])
def raids():
    raids = api.storage.raids
    raid_data = []
    for raid in raids:
        rai = {}
        rai['id'] = str(raid)
        rai['raid_name'] = str(api.storage.raid_name(raid))
        rai['raid_devices'] = str(api.storage.raid_devices(raid))
        raid_data.append(rai)
    return_data = {
        "status_code": 200,
        "response": raid_data
    }
    return (return_data)

@app.get("/fans", tags=["health"])
def fans():
    fans = api.health.fan
    fan_data = []
    for fan in fans:
        fa = {}
        fa['id'] = str(fan)
        fa['fan_speed'] = str(api.health.fan_value(fan))
        fan_data.append(fa)
    return_data = {
        "status_code": 200,
        "response": fan_data
    }
    return (return_data)

@app.get("/temps", tags=["health"])
def temps():
    temps = api.health.temp
    temp_data = []
    for temp in temps:
        tem = {}
        tem['id'] = str(temp)
        tem['temperature'] = str(api.health.temp_value(temp))
        temp_data.append(tem)
    return_data = {
        "status_code": 200,
        "response": temp_data
    }
    return (return_data)

@app.get("/detailed_storage", tags=["storage"])
def volumes():
    detailed_storage = api.storage.detailed_storage
    return_data = {
        "status_code": 200,
        "response": detailed_storage
    }
    return(return_data)

@app.get("/detailed_host", tags=["storage"])
def volumes():
    detailed_host = api.utilisation.detailed_host
    return_data = {
        "status_code": 200,
        "response": detailed_host
    }
    return(return_data)

@app.get("/services", tags=["host"])
def services():
    services_data = api.services.service
    return_data = {
        "status_code": 200,
        "response": services_data
    }
    return(return_data)
