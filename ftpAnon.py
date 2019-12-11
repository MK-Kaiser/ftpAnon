#!/usr/bin/env python3

import ftplib, argparse

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'a@b.com')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Successful')
        ftp.quit()
        return True
        
    except Exception as e:
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed')
        return False
        
def main():
    parser = argparse.ArgumentParser(description='uses pxssh from pexpect to ssh brute forcing')
    parser.add_argument('-t', '--tgt', dest='tgtHost', type=str, required=False, help='provide a target url, or address example: www.website.com')
    parser.add_argument('-v', '--version', dest='ver', required=False, action='store_true', help='display version number.')
    args = parser.parse_args()
    if args.ver:
        print("anonLogin ftp version 0.1")
        exit()    
    hostname = args.tgtHost
    anonLogin(hostname)

if __name__ == '__main__':
    main()
