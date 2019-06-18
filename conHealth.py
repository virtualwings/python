# --------------------------------------------
# script to check the docker container health:
# --------------------------------------------
import subprocess
nl = subprocess.check_output('docker ps -a -q', shell=True)
nnl = nl.splitlines()
for i in nnl:
cid = i.decode('utf-8')

cmd1 = "docker inspect -f '{{.Name}}' %s" %(cid)
cmd2 = "docker inspect -f '{{.State.Running}}' %s" %(cid)
cmd3 = "docker inspect -f '{{.State.StartedAt}}' %s" %(cid)

cn = subprocess.check_output(cmd1,shell=True).decode('utf-8')
cs = subprocess.check_output(cmd2,shell=True).decode('utf-8')
cst = subprocess.check_output(cmd3,shell=True).decode('utf-8')

if str(cs).strip() == "'true'":
 print ('INFO: Container ' + str(cn).strip() + " is running")
else:
 print ('CRITICAL: Container ' + str(cn).strip() + " is not running from " + str(cst).strip())
