servers=("server1", "server2", "server3")
for server in servers:
    print(f'configure_monitoring_agent {server}')