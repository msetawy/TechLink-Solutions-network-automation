from netmiko import ConnectHandler
import devices

# --- CORE ROUTER CONFIG PACKAGES ---

hq_configs = [
    'hostname HQ-Router',
    'interface GigabitEthernet0/0',
    ' ip address 10.10.1.1 255.255.255.252',
    ' no shutdown',
    'interface GigabitEthernet1/0',
    ' ip address 192.168.12.1 255.255.255.252',
    ' no shutdown',
    'interface GigabitEthernet2/0',
    ' ip address 192.168.13.1 255.255.255.252',
    ' no shutdown',
    'interface GigabitEthernet3/0',
    ' ip address 192.168.22.1 255.255.255.252',
    ' no shutdown',
    'interface GigabitEthernet4/0',
    ' ip address 192.168.23.1 255.255.255.252',
    ' no shutdown',
    'interface Loopback0',
    ' ip address 1.1.1.1 255.255.255.255',
    'router ospf 1',
    ' router-id 1.1.1.1',
    ' network 1.1.1.1 0.0.0.0 area 0',
    ' network 10.10.1.0 0.0.0.3 area 0',
    ' network 192.168.12.0 0.0.0.3 area 0',
    ' network 192.168.13.0 0.0.0.3 area 0',
    ' network 192.168.22.0 0.0.0.3 area 0',
    ' network 192.168.23.0 0.0.0.3 area 0',
]

alex_configs = [
    'hostname BR1-Alex-Router',
    'interface GigabitEthernet0/0',
    ' ip address 10.11.1.1 255.255.255.252',
    ' no shutdown',
    'interface GigabitEthernet1/0',
    ' ip address 192.168.12.2 255.255.255.252',
    ' no shutdown',
    'interface GigabitEthernet2/0',
    ' ip address 192.168.13.2 255.255.255.252',
    ' ip ospf cost 50',
    ' no shutdown',
    'interface Loopback0',
    ' ip address 2.2.2.2 255.255.255.255',
    'router ospf 1',
    ' router-id 2.2.2.2',
    ' network 2.2.2.2 0.0.0.0 area 0',
    ' network 10.11.1.0 0.0.0.3 area 0',
    ' network 192.168.12.0 0.0.0.3 area 0',
    ' network 192.168.13.0 0.0.0.3 area 0',
]

giza_configs = [
    'hostname BR2-Giza-Router',
    'interface GigabitEthernet0/0',
    ' ip address 10.12.1.1 255.255.255.252',
    ' no shutdown',
    'interface GigabitEthernet1/0',
    ' ip address 192.168.22.2 255.255.255.252',
    ' no shutdown',
    'interface GigabitEthernet2/0',
    ' ip address 192.168.23.2 255.255.255.252',
    ' ip ospf cost 50',
    ' no shutdown',
    'interface Loopback0',
    ' ip address 3.3.3.3 255.255.255.255',
    'router ospf 1',
    ' router-id 3.3.3.3',
    ' network 3.3.3.3 0.0.0.0 area 0',
    ' network 10.12.1.0 0.0.0.3 area 0',
    ' network 192.168.22.0 0.0.0.3 area 0',
    ' network 192.168.23.0 0.0.0.3 area 0',
]

# --- MULTILAYER SWITCH CONFIG PACKAGES (vIOS-L2 Standard Syntax) ---

hq_mls_configs = [
    'hostname HQ-ML-Switch',
    'ip routing',
    'vlan 10',
    ' name MGMT',
    'vlan 20',
    ' name USERS',
    'interface GigabitEthernet0/0',
    ' no switchport',
    ' ip address 10.10.1.2 255.255.255.252',
    ' no shutdown',
    'interface GigabitEthernet0/1',
    ' switchport mode access',
    ' switchport access vlan 10',
    ' no shutdown',
    'interface GigabitEthernet0/2',
    ' switchport mode access',
    ' switchport access vlan 20',
    ' no shutdown',
    'interface vlan 10',
    ' ip address 10.10.10.1 255.255.255.0',
    ' no shutdown',
    'interface vlan 20',
    ' ip address 10.10.20.1 255.255.255.0',
    ' no shutdown',
    'ip dhcp excluded-address 10.10.10.1 10.10.10.10',
    'ip dhcp pool CAIRO_MGMT',
    ' network 10.10.10.0 255.255.255.0',
    ' default-router 10.10.10.1',
    ' dns-server 8.8.8.8',
    'ip dhcp excluded-address 10.10.20.1 10.10.20.10',
    'ip dhcp pool CAIRO_USERS',
    ' network 10.10.20.0 255.255.255.0',
    ' default-router 10.10.20.1',
    ' dns-server 8.8.8.8',
    'router ospf 1',
    ' network 10.10.1.0 0.0.0.3 area 0',
    ' network 10.10.10.0 0.0.0.255 area 0',
    ' network 10.10.20.0 0.0.0.255 area 0',
]

alex_mls_configs = [
    'hostname BR1-ML-Switch',
    'ip routing',
    'vlan 10',
    ' name MGMT',
    'vlan 20',
    ' name USERS',
    'interface GigabitEthernet0/0',
    ' no switchport',
    ' ip address 10.11.1.2 255.255.255.252',
    ' no shutdown',
    'interface GigabitEthernet0/1',
    ' switchport mode access',
    ' switchport access vlan 10',
    ' no shutdown',
    'interface GigabitEthernet0/2',
    ' switchport mode access',
    ' switchport access vlan 20',
    ' no shutdown',
    'interface vlan 10',
    ' ip address 10.11.10.1 255.255.255.0',
    ' no shutdown',
    'interface vlan 20',
    ' ip address 10.11.20.1 255.255.255.0',
    ' no shutdown',
    'ip dhcp excluded-address 10.11.10.1 10.11.10.10',
    'ip dhcp pool ALEX_MGMT',
    ' network 10.11.10.0 255.255.255.0',
    ' default-router 10.11.10.1',
    ' dns-server 8.8.8.8',
    'ip dhcp excluded-address 10.11.20.1 10.11.20.10',
    'ip dhcp pool ALEX_USERS',
    ' network 10.11.20.0 255.255.255.0',
    ' default-router 10.11.20.1',
    ' dns-server 8.8.8.8',
    'router ospf 1',
    ' network 10.11.1.0 0.0.0.3 area 0',
    ' network 10.11.10.0 0.0.0.255 area 0',
    ' network 10.11.20.0 0.0.0.255 area 0',
]

giza_mls_configs = [
    'hostname BR2-ML-Switch',
    'ip routing',
    'vlan 10',
    ' name MGMT',
    'vlan 20',
    ' name USERS',
    'interface GigabitEthernet0/0',
    ' no switchport',
    ' ip address 10.12.1.2 255.255.255.252',
    ' no shutdown',
    'interface GigabitEthernet0/1',
    ' switchport mode access',
    ' switchport access vlan 10',
    ' no shutdown',
    'interface GigabitEthernet0/2',
    ' switchport mode access',
    ' switchport access vlan 20',
    ' no shutdown',
    'interface vlan 10',
    ' ip address 10.12.10.1 255.255.255.0',
    ' no shutdown',
    'interface vlan 20',
    ' ip address 10.12.20.1 255.255.255.0',
    ' no shutdown',
    'ip dhcp excluded-address 10.12.10.1 10.12.10.10',
    'ip dhcp pool GIZA_MGMT',
    ' network 10.12.10.0 255.255.255.0',
    ' default-router 10.12.10.1',
    ' dns-server 8.8.8.8',
    'ip dhcp excluded-address 10.12.20.1 10.12.20.10',
    'ip dhcp pool GIZA_USERS',
    ' network 10.12.20.0 255.255.255.0',
    ' default-router 10.12.20.1',
    ' dns-server 8.8.8.8',
    'router ospf 1',
    ' network 10.12.1.0 0.0.0.3 area 0',
    ' network 10.12.10.0 0.0.0.255 area 0',
    ' network 10.12.20.0 0.0.0.255 area 0',
]

def push_config(node_param, config_list):
    try:
        print(f"Connecting to port {node_param['port']}...")
        session = ConnectHandler(**node_param)
        session.enable()
        # Clean config pass without tracking prompt status flags
        session.send_config_set(config_list)
        session.disconnect()
        print(f"Port {node_param['port']} configured successfully.\n")
    except Exception as err:
        print(f"Error provisioning port {node_param['port']}: {err}")

def run():
    print("=== INITIALIZING INVENTORY DEPLOYMENT ===")
    push_config(devices.hq_router, hq_configs)
    push_config(devices.alex_router, alex_configs)
    push_config(devices.giza_router, giza_configs)
    push_config(devices.hq_mls, hq_mls_configs)
    push_config(devices.alex_mls, alex_mls_configs)
    push_config(devices.giza_mls, giza_mls_configs)
    print("=== BASELINE CONFIGURATION COMPLETE ===")

if __name__ == '__main__':
    run()