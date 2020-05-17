# Task 1

write a short series of shell commands in a single line, to list out the process that belong to "root" and print out the PID, owner and name of the proces. [See more examples](http://man7.org/linux/man-pages/man1/ps.1.html)

```bash
ps axo pid,command,user | grep root
```
