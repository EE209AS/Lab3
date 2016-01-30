import subprocess 

p = subprocess.Popen(['ls', '-al'])
(out, err) = p.communicate();
print out
