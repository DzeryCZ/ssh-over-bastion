# SSH to multiple servers over bastion

## SSH to server over bastion
```bash
ssh -i ./path/to/private/certificate -J ubuntu@ip-of-bastion ubuntu@ip-of-server
```

## SSH to multiple servers over bastion

- Install dependencies
    ```bash
    pip3 install -r ./requirements.txt
    ```
- Given a configuration in `config.yaml` with structure
    ```yaml
    server1:
        ip: 192.168.0.1
        bastion: 212.186.105.45
    serverN:
        ip: 192.168.0.2
        bastion: 212.186.105.45
    ```
- We can use a simple python helper like this
    ```bash
    bastion-ssh.py -i ./path/to/private/certificate -c ./path/to/config/file name-of-server
    ```
