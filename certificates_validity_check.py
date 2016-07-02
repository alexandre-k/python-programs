'''A script whose purpose is to print the expiration date of certificates stored on the BIG IP load balancers.
It prints at the beginning the machine's name. Since I had to write it from a default install of python 2.7,
no non-default modules are used. For convenience, data is exported in a csv file
'''
import commands,re,os,csv

def get_virtname():
    print "Retrieving virtual servers"
    virtservers = commands.getoutput('ssh username@machine virtual list all')
    virtserver_list = virtservers.split('virtual')

    #file = open('virtuallist.txt', 'r')
    #virtserver_list = file.read()
    print "Looking for virtual servers and their ssl profile associated..."
    virt_ssl_search = re.compile(r'(?:^\s)(?P<vname>[a-zA-Z0-9\-\.\_]+)(?:.*?)(destination\s)(?P<vip>[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9a-z]+|2001:[0-9a-z:]*:[\.0-9a-z]+)(?:.*?)(?P<sslprofile>[a-zA-Z0-9\-\.]+-clientssl)',
    re.DOTALL)
    #Isolate virtual servers where there is a profile clientssl
    vservers_ssl_list = []
    for vserver in virtserver_list:
        if 'clientssl' in vserver:
            vservers_ssl_list = vservers_ssl_list + virt_ssl_search.findall(vserver)

    #From the virtual servers isolated, create a dictionary
    servers_ssl = {}
    for each_tuple in vservers_ssl_list:
        servers_ssl[each_tuple[0]] = {'destination': each_tuple[2],'ssl': each_tuple[3]}
    return servers_ssl

def get_ssl_profiles(servers_ssl):
    print "Retrieving the list of clientssl profiles..."
    ssl_profile_list = commands.getoutput('ssh username@machine profile clientssl list all')
    #file = open('ssllist.txt','r')
    #ssl_list = file.read()
    cert_search = re.compile(r'(?:profile clientssl\s)([a-zA-Z0-9-.]+)(?:.*?)(cert\s\")([a-zA-Z0-9\.\-\_]+crt)', re.DOTALL)

    print "Looking for certificates in use..."
    used_certs = cert_search.findall(ssl_profile_list)

    print "Associating the certificates in use for each virtual servers"
    for each_tuple in used_certs:
        for each_key in servers_ssl.keys():
            if servers_ssl[each_key]['ssl'] == each_tuple[0]:
                servers_ssl[each_key]['cert'] = each_tuple[2]

# For confirmation, not useful anymore
#    for vip in servers_ssl:
#        print vip
#        print servers_ssl[vip]

    return servers_ssl

def get_cert_dates(servers_ssl):
    cert_list = open('certs_list.txt', 'a')
    cert_list.write('!bash\n')
    for each_vserver in servers_ssl:
        cert_list.write('openssl x509 -enddate -noout -in /config/ssl/ssl.crt/' + servers_ssl[each_vserver]['cert'] + '\n')
    cert_list.close()
    result = commands.getoutput('cat certs_list.txt | ssh username@machine')
    date_search = re.compile('(?:After=)(?P<date>\w+\s\d+\s\d+:\d+:\d+\s\d+)')
    enddate = date_search.findall(result)
    count = 0
    for each_vserver in servers_ssl:
        servers_ssl[each_vserver]['enddate'] = enddate[count]
        count+=1
    return servers_ssl

def print_in_csv(servers_ssl):
    csvfile = open('certificates.csv', 'w')
    csvwriter = csv.writer(csvfile)
    machine_name = commands.getoutput('ssh username@machine system list')
    csvwriter.writerow(["Machine: " + re.search(r'(?:hostname).*?([a-z0-9A-Z\.-_]+)', machine_name).group(1)])
    csvwriter.writerow(['Virtual Server', 'SSL Profile Name', 'Certificate', 'Expiration Date'])

    for each_vserver in sorted(servers_ssl, key=servers_ssl.get, reverse=True):
        csvwriter.writerow([each_vserver,
                            servers_ssl[each_vserver]['ssl'],
                            servers_ssl[each_vserver]['cert'],
                            servers_ssl[each_vserver]['enddate']])
    print "**************************************************"
    os.remove('certs_list.txt')
    csvfile.close()

def main():
    virtserver_list = get_virtname()
    virtservers_with_certs = get_ssl_profiles(virtserver_list)
    certs_expiration = get_cert_dates(virtservers_with_certs)
    print_in_csv(certs_expiration)

if __name__ == "__main__":
    main()
