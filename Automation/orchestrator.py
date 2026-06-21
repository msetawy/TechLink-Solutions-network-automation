import time
import logging
from netmiko import ConnectHandler

# --- logging setup ---
log = logging.getLogger("net_mon")
log.setLevel(logging.INFO)
fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

if log.hasHandlers():
    log.handlers.clear()

# console stream output handler
sh = logging.StreamHandler()
sh.setFormatter(fmt)
log.addHandler(sh)

# flat file persistent audit log
fh = logging.FileHandler('network_status.log', mode='a')
fh.setFormatter(fmt)
log.addHandler(fh)

# terminal color escape tags
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# console parameter definitions for hq box
hq_node = {
    'device_type': 'cisco_ios_telnet',
    'host': '127.0.0.1',
    'port': '5000',
    'global_delay_factor': 1
}

def get_telemetry_data(conn):
    try:
        routes = conn.send_command("show ip route ospf")
        
        # --- alexandria traffic forwarding path ---
        alx_paths = []
        if "GigabitEthernet1/0" in routes: alx_paths.append("Primary (Gi1/0)")
        if "GigabitEthernet2/0" in routes: alx_paths.append("Backup (Gi2/0)")
        
        if len(alx_paths) >= 1:
            alx_fwd = f"{GREEN}{alx_paths[0]} IS LIVE{RESET}"
        else:
            alx_fwd = f"{RED}NO ACTIVE ROUTE{RESET}"

        # --- giza traffic forwarding path ---
        giz_paths = []
        if "GigabitEthernet3/0" in routes: giz_paths.append("Primary (Gi3/0)")
        if "GigabitEthernet4/0" in routes: giz_paths.append("Backup (Gi4/0)")
        
        if len(giz_paths) >= 1:
            giz_fwd = f"{GREEN}{giz_paths[0]} IS LIVE{RESET}"
        else:
            giz_fwd = f"{RED}NO ACTIVE ROUTE{RESET}"
                
        return alx_fwd, giz_fwd
        
    except Exception:
        return "ERR", "ERR"

def main():
    log.info("=== WAN TRACKING ENGINE ONLINE ===")
    try:
        # persistent terminal session holder
        session = ConnectHandler(**hq_node)
        session.enable()
        
        # monitoring cycle loops continuously
        while True:
            alx_act, giz_act = get_telemetry_data(session)
            
            log.info("[LIVE TELEMETRY TRAFFIC MAP]")
            log.info(f" -> ALEX Branch Forwarding -> {alx_act}")
            log.info(f" -> GIZA Branch Forwarding -> {giz_act}\n")
            
            # periodic interval wait window
            time.sleep(30) 
            
    except KeyboardInterrupt:
        log.info("Monitor killed by operator.")
    except Exception as err:
        log.error(f"Execution loop failed: {err}")
    finally:
        # close handle sockets safely
        try:
            session.disconnect()
        except:
            pass

if __name__ == '__main__':
    main()