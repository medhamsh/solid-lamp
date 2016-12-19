''' Importing fabric to execute commands and collect
information of the execution into python objects for
further evaluation '''

from fabric.api import hosts, run, env

''' Defining the my_hosts variable reading from the 
separate hosts file. This is used as a decorator to
run the tasks. Now the decorator @hosts(my_hosts) 
can be specified to execute the task on those hosts '''


with open('hostsfile.txt')as f:
    my_hosts = f.read().splitlines()


''' Task to get the disk utilization on those hosts,
per user and collect them into a computable object
and utilize the object later for sorting and other
use cases. Apply the hosts decorator to execute on
the hosts.'''

@hosts(my_hosts)
def space_per_user():
    run("find /tmp/local -type f -printf '%u %k\n' | awk '{\ 
                                        arr[$1] += $2\ 
                                    } END {\ 
                                        for ( i in arr ) {\ 
                                            print i": "arr[i]"K"\ 
                                        }\
                                    }'")
       
