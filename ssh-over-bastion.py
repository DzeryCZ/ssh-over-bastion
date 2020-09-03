#!/usr/bin/python3

import os, sys, getopt, yaml

ARG_CONFIG_FILE = 'config_file'
ARG_IDENTITY_FILE = 'identity_file'
ARG_SERVER_NAME = 'server_name'
SSH_SERVER_USERNAME = 'ubuntu'

def main(argv):
    parameters = parse_argv(argv)
    configuration = yaml.load(parameters[ARG_CONFIG_FILE], Loader=yaml.FullLoader)
    server_configuration = configuration[parameters[ARG_SERVER_NAME]]

    certificate_file = parameters[ARG_IDENTITY_FILE]
    bastion_ip = server_configuration['bastion']
    server_ip = server_configuration['bastion']
    ssh_to_server(certificate_file, bastion_ip, server_ip)


def ssh_to_server(certificate_file: str, bastion_ip: str, server_ip: str):
    command = 'ssh -i %s -J %s@%s %s@%s' % (certificate_file, SSH_SERVER_USERNAME, bastion_ip, SSH_SERVER_USERNAME, server_ip)
    os.system(command)


def parse_argv(argv):
    parameters = {}

    try:
        opts, args = getopt.getopt(argv,'c:i:',['config='])
    except getopt.GetoptError:
        print_help()

    for opt, arg in opts:
        if opt == '-h':
            print_help()
        elif opt in ('-c', '--config'):
            parameters[ARG_CONFIG_FILE] = open(arg, 'r')
        elif opt == '-i':
            parameters[ARG_IDENTITY_FILE] = arg

    if len(args) >= 1:
        parameters[ARG_SERVER_NAME] = args[0]
    else:
        print_help()

    if len(parameters) < 3:
        print_help()

    return parameters


def print_help():
    print('')
    print('Usage: ssh-over-bastion.py [OPTIONS] SERVER_NAME')
    print('')
    print('Options:')
    print('\t-c, --config\tPath to configuration file in YAML format')
    print('\t-i\t\tSSH identity_file')
    sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
