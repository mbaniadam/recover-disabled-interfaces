## Network Interface Recovery Tool
This Python script helps network administrators find and recover disabled network interfaces on Cisco devices due to MAC address violation errors. It uses the Netmiko library to establish SSH connections to network devices and perform the necessary operations.
### Prerequisites
Before using this tool, ensure you have the following:

- Python 3.x installed on your local machine.
- The Netmiko library installed (pip install netmiko).
- Access to the network devices with valid SSH credentials.
- Cisco devices running the IOS operating system.


### Usage
To use the tool, follow these steps:

Ensure you've updated the device information in the main.py file.

Run the script:
```console
python main.py
```
The script will attempt to connect to the specified network devices and find interfaces that are in an "err-disabled" state due to MAC address violation.

If err-disabled interfaces are found, the script will attempt to recover them by clearing port security sticky entries, shutting down the interface, and then bringing it back up.

The script will provide detailed output for each recovered interface, or it will notify you if there are no err-disabled interfaces caused by MAC address violations.
