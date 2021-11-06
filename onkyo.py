import paramiko, time

router = 'IP'
password = 'PASS'
username = 'USER'
print('Connecting to %s' % router)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(router, username=username, password=password)
print('Successfully connected to %s' % router)

remote_conn = ssh.invoke_shell()
time.sleep(0.1)
remote_conn.send('\n!1PWRQSTN\n')  # I only want output from this command.
time.sleep(0.1)
output1 = remote_conn.recv(1000)
print('1 ' + output1.decode("utf-8"))
time.sleep(0.1)
remote_conn.send('\n!1MVLQSTN\n')
output2 = remote_conn.recv(1000)
print('2 ' + output2.decode("utf-8"))
time.sleep(0.1)
remote_conn.send('\n!1MVL2A\n')
output3 = remote_conn.recv(1000)
print('3 ' + output3.decode("utf-8"))
time.sleep(0.1)
remote_conn.send('\n!1PWRQSTN\n')
output4 = remote_conn.recv(1000)
print('4 ' + output4.decode("utf-8"))
