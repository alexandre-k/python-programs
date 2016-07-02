import threading, subprocess, re, logging, time

global ip

ip = ['111.111.111', '172.217.25.238', '206.190.36.45', '98.138.253.109', '98.139.183.24']
#addresses = ('149.210.217.' + str(number) for number in range(1,254))

def ping(ip_address):
    global result
    logging.basicConfig(
            level = logging.DEBUG,
            format = '[%(levelname)s] %(threadName)-10s %(message)s'
            )
    cmd = "ping -c2 -q " + ip_address
    logging.debug('Started at ' + time.strftime("%H:%M:%S"))
    proc = subprocess.Popen(cmd.split(' '), stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    result, failure = proc.communicate()
    #logging.debug('Stopped')
    if result:
        try:
            loss = re.search(r'(?P<loss>\d+\.\d+%)(?: packet loss)', result.decode(encoding='utf-8')).group('loss')
        except:
            print("error regex")
    if failure:
        print('X NG: Error while pinging ' + ip_address, str(failure.decode(encoding='utf-8')))
        #print(failure + " while pinging " + ip_address)
    else:
        print("O OK: " + loss + " of loss while pinging " + ip_address)

def main():
    print('Enter a pause value:')
    sleep_value = input()
    while True:
        for address in ip:
            pinger = threading.Thread(name="ping", target=ping, args=(address,))
            result = pinger.start()
        time.sleep(int(sleep_value))


if __name__ == "__main__":
    main()
