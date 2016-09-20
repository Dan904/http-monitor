import boto.ec2

def getInstPL():
    conn = boto.ec2.connect_to_region("us-west-2",profile_name='pluto')
    reservations = conn.get_all_instances()
    instances = [i for r in reservations for i in r.instances]
    return instances



def getInst():
    conn = boto.ec2.connect_to_region("us-west-2")
    reservations = conn.get_all_instances()
    instances = [i for r in reservations for i in r.instances]
    return instances

