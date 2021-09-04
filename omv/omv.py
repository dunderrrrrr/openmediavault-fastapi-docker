"""Module containing multiple classes to interact with openmediavault
based on StaticCube https://github.com/StaticCube/python-synology"""
# -*- coding:utf-8 -*-
import requests
import urllib3


class FormatHelper(object):
    """Class containing various formatting functions"""
    @staticmethod
    def bytes_to_readable(num):
        """Converts bytes to a human readable format"""
        if num < 512:
            return "0 Kb"
        elif num < 1024:
            return "1 Kb"

        for unit in ['', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb']:
            if abs(num) < 1024.0:
                return "%3.1f%s" % (num, unit)
            num /= 1024.0
        return "%.1f%s" % (num, 'Yb')

    @staticmethod
    def bytes_to_megabytes(num):
        """Converts bytes to megabytes"""
        var_mb = num / 1024.0 / 1024.0

        return round(var_mb, 1)

    @staticmethod
    def bytes_to_gigabytes(num):
        """Converts bytes to gigabytes"""
        var_gb = num / 1024.0 / 1024.0 / 1024.0

        return round(var_gb, 1)

    @staticmethod
    def bytes_to_terrabytes(num):
        """Converts bytes to terrabytes"""
        var_tb = num / 1024.0 / 1024.0 / 1024.0 / 1024.0

        return round(var_tb, 1)

class OmvUtilization(object):
    """Class containing Utilisation data"""
    def __init__(self, raw_input):
        self._data = None
        self.update(raw_input)

    def update(self, raw_input):
        """Allows updating Utilisation data with raw_input data"""
        if raw_input is not None:
            self._data = {}
            for val in raw_input:
                self._data["hostname"] = raw_input['hostname']
                self._data["version"] = raw_input['version']
                self._data["processor"] = raw_input['cpuModelName']
                self._data["kernel"] = raw_input['kernel']
                self._data["time"] = raw_input['time']
                self._data["uptime"] = raw_input['uptime']
                self._data["loadAverage"] = raw_input['loadAverage']
                self._data["cpuUsage"] = raw_input['cpuUsage']
                self._data["memTotal"] = raw_input['memTotal']
                self._data["memFree"] = raw_input['memFree']
                self._data["memUsed"] = raw_input['memUsed']
                self._data["configDirty"] = raw_input['configDirty']
                self._data["rebootRequired"] = raw_input['rebootRequired']
                self._data["pkgUpdatesAvailable"] = raw_input['pkgUpdatesAvailable']

    @property
    def detailed_host(self):
        """Returns all host data of openmediavault"""
        if self._data is not None:
            return (self._data)

    @property
    def hostname(self):
        """Hostname of openmediavault"""
        if self._data is not None:
            return self._data["hostname"]

    @property
    def memTotal(self):
        """memTotal of openmediavault"""
        if self._data is not None:
            return self._data["memTotal"]

    @property
    def memFree(self):
        """memFree of openmediavault"""
        if self._data is not None:
            return self._data["memFree"]

    @property
    def memUsed(self):
        """memUsed of openmediavault"""
        if self._data is not None:
            return self._data["memUsed"]

    @property
    def kernel(self):
        """kernel of openmediavault"""
        if self._data is not None:
            return self._data["kernel"]

    @property
    def processor(self):
        """processor of openmediavault"""
        if self._data is not None:
            return self._data["processor"]

    @property
    def pkgUpdatesAvailable(self):
        """pkgUpdatesAvailable of openmediavault"""
        if self._data is not None:
            return self._data["pkgUpdatesAvailable"]

    @property
    def version(self):
        """version of openmediavault"""
        if self._data is not None:
            return self._data["version"]

    @property
    def rebootRequired(self):
        """rebootRequired of openmediavault"""
        if self._data is not None:
            return self._data["rebootRequired"]

    @property
    def configDirty(self):
        """configDirty of openmediavault"""
        if self._data is not None:
            return self._data["configDirty"]

    @property
    def up_time(self):
        """Get uptime"""
        if self._data is not None:
            return self._data["uptime"]

    # @property
    # def cpu_other_load(self):
    #     """'Other' percentage of the total cpu load"""
    #     if self._data is not None:
    #         return self._data["cpu"]["other_load"]

#     @property
#     def cpu_user_load(self):
#         """'User' percentage of the total cpu load"""
#         if self._data is not None:
#             return self._data["cpu"]["user_load"]

    # @property
    # def cpu_system_load(self):
    #     """'System' percentage of the total cpu load"""
    #     if self._data is not None:
    #         return self._data["cpu"]["system_load"]

    @property
    def cpu_total_load(self):
        """Total CPU load for openmediavault"""
        if self._data is not None:
            return self._data["cpuUsage"]

    def _get_cpu_avg_load(self):
        """Get avg load and parse"""
        if self._data is not None:
            #return self._data["loadAverage"].split(', ')
            return self._data["loadAverage"]

    @property
    def cpu_1min_load(self):
        """Average CPU load past minute"""
        #return self._get_cpu_avg_load()[0]
        return self._get_cpu_avg_load()['1min']

    @property
    def cpu_5min_load(self):
        """Average CPU load past 5 minutes"""
        #return self._get_cpu_avg_load()[1]
        return self._get_cpu_avg_load()['5min']

    @property
    def cpu_15min_load(self):
        """Average CPU load past 15 minutes"""
        #return self._get_cpu_avg_load()[2]
        return self._get_cpu_avg_load()['15min']

    @property
    def memory_real_usage(self):
        """Get mem usage"""
        if self._data is not None:
            return self._data["memUsed"]

class OmvStorage(object):
    """Class containing Storage data"""
    def __init__(self, raw_input):
        self._data = None
        self.update(raw_input)

    def update(self, raw_input):
        """Allows updating Utilisation data with raw_input data"""
        if raw_input is not None:
            self._data = raw_input

    @property
    def detailed_storage(self):
        """Returns all data in storage"""
        if self._data is not None:
            return(self._data)

    @property
    def volumes(self):
        """Returns all available volumes"""
        if self._data is not None:
            volumes = []
            for volume in self._data["volumes"]:
                volumes.append(volume["devicefile"])
            return volumes

    def _get_volume(self, volume_devicefile):
        """Returns a specific volume"""
        if self._data is not None:
            for volume in self._data["volumes"]:
                if volume["devicefile"] == volume_devicefile:
                    return volume

    def volume_status(self, volume):
        """Status of the volume (clean etc.)"""
        volume = self._get_volume(volume)
        raid = self._get_raid(volume["devicefile"])
        if volume is not None and raid is not None:
            return raid["state"]

    def volume_device_type(self, volume):
        """Returns the volume type (RAID1, RAID2, etc)"""
        volume = self._get_volume(volume)
        try:
            raid = self._get_raid(volume["devicefile"])
            if volume is not None and raid is not None:
                return raid["level"]
        except KeyError:
            pass
        return None

    def _volume_mounted(self, volume):
        """Returns boolean if mounted"""
        volume = self._get_volume(volume)
        if volume is not None:
            return volume["mounted"]
        return False

    def volume_size_total(self, volume, human_readable=True):
        """Total size of volume"""
        volume = self._get_volume(volume)
        if volume is not None and self._volume_mounted(volume["devicefile"]):
            return_data = int(volume["size"])
            if human_readable:
                return FormatHelper.bytes_to_readable(
                    return_data)
            else:
                return return_data

    def volume_size_used(self, volume, human_readable=True):
        """Total used size in volume"""
        volume = self._get_volume(volume)
        if volume is not None and self._volume_mounted(volume["devicefile"]):
            return_data = int(int(volume["size"])-int(volume["available"]))
            if human_readable:
                return FormatHelper.bytes_to_readable(
                    return_data)
            else:
                return return_data

    def volume_percentage_used(self, volume):
        """Total used size in percentage for volume"""
        volume = self._get_volume(volume)
        if volume is not None:
            total = int(volume["size"])
            used = int(int(volume["size"])-int(volume["available"]))

            if used is not None and used > 0 and \
               total is not None and total > 0:
                return round((float(used) / float(total)) * 100.0, 1)

    def volume_disk_temp_avg(self, volume):
        """Average temperature of all disks making up the volume"""
        volume = self._get_volume(volume)
        if volume is not None:
            if self.volume_device_type(volume["devicefile"]) is None:
                return self.disk_temp(volume["parentdevicefile"])

            vol_disks = self._get_raid(volume["devicefile"])
            if vol_disks is not None:
                total_temp = 0
                total_disks = 0

                for vol_raid in vol_disks["devices"]:
                    disk_temp = self.disk_temp(vol_raid[0:-1])
                    if disk_temp is not None:
                        total_disks += 1
                        total_temp += disk_temp

                if total_temp > 0 and total_disks > 0:
                    return int(round(total_temp / total_disks, 0))

    def volume_disk_temp_max(self, volume):
        """Maximum temperature of all disks making up the volume"""
        volume = self._get_volume(volume)
        if volume is not None:
            if self.volume_device_type(volume["devicefile"]) is None:
                return self.disk_temp(volume["parentdevicefile"])

            vol_disks = self._get_raid(volume["devicefile"])
            if vol_disks is not None:
                max_temp = 0

                for vol_raid in vol_disks["devices"]:
                    disk_temp = self.disk_temp(vol_raid[0:-1])
                    if disk_temp is not None and disk_temp > max_temp:
                        max_temp = disk_temp

                return max_temp

    @property
    def raids(self):
        """Returns all available raids"""
        if self._data is not None:
            raids = []
            for raid in self._data["raid"]:
                raids.append(raid["devicefile"])
            return raids

    def _get_raid(self, raid_devicefile):
        """Returns a specific raid"""
        if self._data is not None:
            for raid in self._data["raid"]:
                if raid["devicefile"] == raid_devicefile:
                    return raid

    def raid_name(self, raid):
        """The name of this raid"""
        raid = self._get_raid(raid)
        if raid is not None:
            return raid["name"]

    def raid_devices(self, raid):
        """The devices of this raid"""
        raid = self._get_raid(raid)
        if raid is not None:
            devices = []
            for device in raid["devices"]:
                devices.append(device)
            return devices

    def devicefile_from_raid(self, disk):
        """Get raid of disk"""
        for raid in self.raids:
            for device in self.raid_devices(raid):
                if device[0:-1] == disk["devicefile"]:
                    return raid

        return raid

    @property
    def disks(self):
        """Returns all available (internal) disks"""
        if self._data is not None:
            disks = []
            for disk in self._data["smart"]:
                disks.append(disk["devicefile"])
            return disks

    def _get_disk(self, disk_devicefile):
        """Returns a specific disk"""
        if self._data is not None:
            for disk in self._data["smart"]:
                if disk["devicefile"] == disk_devicefile:
                    return disk

    def disk_name(self, disk):
        """The name of this disk"""
        disk = self._get_disk(disk)
        if disk is not None:
            return disk["model"]

    def disk_smart_status(self, disk):
        """Status of disk according to S.M.A.R.T)"""
        disk = self._get_disk(disk)
        if disk is not None:
            return disk["overallstatus"]

    def disk_temp(self, disk):
        """Returns the temperature of the disk"""
        disk = self._get_disk(disk)
        if disk is not None:
            try:
                return int(disk["temperature"][0:-2])
            except ValueError:
                pass
            else:
                return int(disk["temperature"])
        return None

class OmvHealth(object):
    """Class containing health data"""
    def __init__(self, raw_input):
        self._data = None
        self.update(raw_input)

    def update(self, raw_input):
        """Allows updating health data with raw_input data"""
        if raw_input is not None:
            self._data = raw_input

    @property
    def temp(self):
        """Returns all available temperatures"""
        if self._data is not None:
            temps = []
            for temp in self._data:
                if "temperature" in temp["name"]:
                    temps.append(temp["index"])
            return temps

    def _get_temp(self, temp_index):
        """Returns a specific temperature device"""
        if self._data is not None:
            for temp in self._data:
                if temp["index"] == temp_index:
                    return temp

    def temp_value(self, temp):
        """Returns a specific temperature"""
        temp = self._get_temp(temp)
        if temp is not None:
            return temp["value"]

    @property
    def fan(self):
        """Returns all available fan speeds"""
        if self._data is not None:
            fans = []
            for fan in self._data:
                if "Fan" in fan["name"]:
                    fans.append(fan["index"])
            return fans

    def _get_fan(self, fan_index):
        """Returns a specific fan speed device"""
        if self._data is not None:
            for fan in self._data:
                if fan["index"] == fan_index:
                    return fan

    def fan_value(self, fan):
        """Returns a specific fan"""
        fan = self._get_fan(fan)
        if fan is not None:
            return fan["value"]

class OmvServices(object):
    def __init__(self, raw_input):
        self._data = None
        self.update(raw_input)

    def update(self, raw_input):
        if raw_input is not None:
            self._data = raw_input

    @property
    def service(self):
        """Returns all available crons"""
        return(self._data)

class Openmediavault():
    # pylint: disable=too-many-arguments,too-many-instance-attributes
    """Class containing the main openmediavault functions"""
    def __init__(self, omv_ip, omv_port, username, password,
                 use_https=False, debugmode=False):
        # Store Variables
        self.username = username
        self.password = password

        # Class Variables
        # self.access_token = None
        self.cookies = {}
        self._utilisation = None
        self._storage = None
        self._health = None
        self._services = None
        self._debugmode = debugmode
        self._use_https = use_https

        # Define Session
        self._session_error = False
        self._session = None

        # Build Variables
        if self._use_https:
            # https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
            # disable SSL warnings due to the auto-genenerated cert
            urllib3.disable_warnings()

            self.api_url = "https://%s:%s/rpc.php" % (omv_ip, omv_port)
        else:
            self.api_url = "http://%s:%s/rpc.php" % (omv_ip, omv_port)
    # pylint: enable=too-many-arguments,too-many-instance-attributes

    def _debuglog(self, message):
        """Outputs message if debug mode is enabled"""
        if self._debugmode:
            print("DEBUG: " + message + "\n")

    def _construct_packet(self, service, method, params="null"):
        """Construct message string."""
        return '{"service":"%s","method":"%s","params":%s}' % \
            (service, method, params)

    def _login(self):
        """Build and execute login request"""
        credentials = '{"username":"%s","password":"%s"}' % \
            (self.username, self.password)
        login_packet = self._construct_packet("session", "login", credentials)

        result = self._execute_post_url(login_packet)

        # Parse Result if valid
        if result is not None:
            self.cookies = result.cookies
            self._debuglog("Authentication Succesfull, cookie: " +
                           str(self.cookies))
            return True
        else:
            self._debuglog("Authentication Failed")
            return False

    def _logout(self):
        """Build and execute logout request"""
        logout_packet = self._construct_packet("session", "logout")

        result = self._execute_post_url(logout_packet)

        # Parse Result if valid
        if result is not None:
            self._debuglog("Logout Succesfull")
            return True
        else:
            self._debuglog("Logout Failed")
            return False

    def _post_url(self, data, retry_on_error=True):
        """Function to handle sessions for a GET request"""
        # Check if we failed to request the url or need to login
        if self.cookies is None or \
           self._session is None or \
           self._session_error:
            # Clear Access Token en reset session error
            # self.access_token = None
            self.cookies = None
            self._session_error = False

            # First Reset the session
            if self._session is not None:
                self._session = None
            self._debuglog("Creating New Session")
            self._session = requests.Session()

            # disable SSL certificate verification
            if self._use_https:
                self._session.verify = False

            # We Created a new Session so login
            if self._login() is False:
                self._session_error = True
                self._debuglog("Login Failed, unable to process request")
                return

        # Now request the data
        response = self._execute_post_url(data)
        if (self._session_error or response is None) and retry_on_error:
            self._debuglog("Response: " + str(response))
            self._debuglog("Error occured, retrying...")
            self._post_url(data, False)

        return response

    def _execute_post_url(self, data):
        """Function to execute and handle a GET request"""
        # Prepare Request
        self._debuglog(
            "Requesting URL: '" + self.api_url + "', msg: '" + data + "'")
        # Execute Request
        try:
            resp = self._session.post(
                self.api_url, cookies=self.cookies, data=data, verify=False)
            self._debuglog("Request executed: " + str(resp.status_code))

            if resp.status_code == 200:
                # We got a response
                json_data = resp.json()
                self._debuglog("Response (200): " + str(json_data))
                if self.cookies is None and resp.ok:
                    if json_data["response"]["authenticated"]:
                        self._debuglog("Succesfull returning login data")
                        self._debuglog("Login: " + str(json_data))
                        return resp
                elif json_data['error'] is None:
                    self._debuglog("Succesfull returning data")
                    self._debuglog("Data returned: " + str(json_data))
                    return json_data
                else:
                    if json_data["error"]["code"] in \
                            {0, 105, 106, 107, 119, 5000, 5001}:
                        self._debuglog("Session error: " +
                                       str(json_data["error"]["code"]))
                        self._session_error = True
                    else:
                        self._debuglog("Failed: " + resp.text)
            else:
                # We got a 404 or 401
                self._debuglog("Error: 404 or 401")
                return None
        # pylint: disable=bare-except
        except KeyError:
            self._debuglog("Error: KeyError")
            return None
        # pylint: enable=bare-except

    def update(self):
        """Updates the various instanced modules"""
        if self._utilisation is not None:
            packet = self._construct_packet("System", "getInformation")
            self._utilisation.update(self._post_url(packet)["response"])
        if self._storage is not None:
            json_response = {}
            json_response['volumes'] = \
                self._post_url(self._construct_packet(
                    "FileSystemMgmt", "enumerateFilesystems"))["response"]

            json_response['smart'] = \
                self._post_url(self._construct_packet(
                    "Smart", "enumerateDevices"))["response"]

            json_response['raid'] = \
                self._post_url(self._construct_packet(
                    "RaidMgmt", "enumerateDevices"))["response"]

            json_response['disk'] = \
                self._post_url(self._construct_packet(
                    "DiskMgmt", "enumerateDevices"))["response"]

            self._storage.update(json_response)
        if self._health is not None:
            packet = self._construct_packet("Health", "getHealthInfo")
            self._health.update(self._post_url(packet)["response"])

        if self._service is not None:
            packet = self._construct_packet("service", "getStatus")
            self._service.update(self._post_url(packet)["response"])


    @property
    def utilisation(self):
        """Getter for various Utilisation variables"""
        if self._utilisation is None:
            packet = self._construct_packet("System", "getInformation")
            self._utilisation = OmvUtilization(
                self._post_url(packet)["response"])
        return self._utilisation

    @property
    def storage(self):
        """Getter for various Storage variables"""
        if self._storage is None:
            json_response = {}
            json_response['volumes'] = \
                self._post_url(self._construct_packet(
                    "FileSystemMgmt", "enumerateFilesystems"))["response"]

            json_response['smart'] = \
                self._post_url(self._construct_packet(
                    "Smart", "enumerateDevices"))["response"]

            json_response['raid'] = \
                self._post_url(self._construct_packet(
                    "RaidMgmt", "enumerateDevices"))["response"]

            json_response['disk'] = \
                self._post_url(self._construct_packet(
                    "DiskMgmt", "enumerateDevices"))["response"]

            self._storage = OmvStorage(json_response)
        return self._storage

    @property
    def health(self):
        """Getter for various Storage variables"""
        if self._health is None:
            packet = self._construct_packet("Health", "getHealthInfo")
            self._health = OmvHealth(self._post_url(packet)["response"])
        return self._health

    @property
    def services(self):
        """Getter for various services variables"""
        if self._services is None:
            packet = self._construct_packet("services", "getStatus")
            self._services = OmvServices(self._post_url(packet)["response"])
        return self._services
