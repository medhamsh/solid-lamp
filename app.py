''' Importing fabric to execute commands and collect
information of the execution into python objects for
further evaluation '''

from fabric.api import *

''' Defining the my_hosts variable reading from the 
separate hosts file. This is used as a decorator to
run the tasks. Now the decorator @hosts(my_hosts) 
can be specified to execute the task on those hosts '''


with open('hostsfile.txt')as f:
    my_hosts = f.read().splitlines()


''' Task to get the disk utilization on any host,
per user and collect them into a computable object
and utilize the object later for sorting and other
use cases.''' 

def space_per_user():
    result = run('''find /local -type f -printf '%u %k\n' | awk '{ \ 
                                        arr[$1] += $2 \ 
                                    } END { \ 
                                        for ( i in arr ) { \ 
                                            print i": "arr[i]"K" \ 
                                        } \
                                    }' \
                                    ''')
    result = result.splitlines()
    return result
      
''' Applying the task decorator and performing the space_per_user
 method on the list of hosts from the text file. The output is given
as a dict and to be sorted later for computational purpose'''

@task
def check_space_on_machines():
    with settings(
       hide('running', 'warnings', 'stdout', 'stderr'),
       warn_only = True
    ):
       result = execute(space_per_user, hosts=my_hosts)
       print(result)
