import subprocess
import os
import sys


def list_vms():
# assigning variables
    count = 0
    vm_dict = dict()
    names = list()
    uuids = list()
    c_names = list()
    c_uuids = list()
# collecting and parsing cmd output
    vms = subprocess.check_output(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "list", "vms"])
    vms = vms.decode()
    vms = vms.replace("\r", "")
    vms = vms.split("\n")
    print(vms)
    for i in vms:
        count += 1
        if i == "":
            continue
        i = i.replace("}", "")
        i = i.split("{")
        i[0] = i[0].strip()
        i[0] = i[0].strip('"')
        vm_dict[count] = {"Name" : i[0], "UUID" : i[1]}
    print(vm_dict)
#    print(len(vms))
#    print(vms)
#    if len(vms) % 4 == 0:
#        print(vms)
## spliting up decoded vms output
#    else:
#        if len(vms) > 3:
#            vms_len = len(vms)
#            vms_len = vms_len / 3
#            start = 0
#            stop = 2
## backup of above if statement in the event that there is only one vm currently listed
#        else:
#            vms_len = len(vms)
#            vms_len = vms_len / 3
#            start = 0
#            stop = 2
## separating names from vms into their own list
#    while vms_len > 0:
#        vms_len -= 1
#        names.append(vms[start:stop])
#        start += 3
#        stop += 3
## separating uuids from vms into their own list
#    for i in vms:
#        if "1" in i:
#            uuids.append(i)
## clean up names
#    for name in names:
#        name = " ".join(name)
#        name = name.strip('"')
#        c_names.append(name)
## clean up uuids
#    for uuid in uuids:
#        uuid = uuid.strip("{")
#        uuid = uuid.strip("}")
#        c_uuids.append(uuid)
## creating dictionary from names and uuid lists with the name as the key
#    print(c_names, c_uuids, vm_dict)
##    for i in range(len(c_names)):
##        vm_dict[i + 1] = {"Name" : c_names[i], "UUID" : c_uuids[i]}
## returning complete dictionary
#    return vm_dict


def create_snapshot(vm_name, snapshot_name):
    output = subprocess.check_output(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "snapshot", vm_name, "take", snapshot_name, "--description", "Snapshot taken by Python script"])
# decode and clean up output
    output = output.decode()
    output = output.replace("\r", "")
# isolate uuid from output
    start = (int(output.find(":"))) + 2
    uuid = output[start: -1]
    return uuid


def list_snapshots(vm_name, snapshot_name):
# collecting and parsing cmd output
    vm_snapshots = subprocess.check_output(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "snapshot", vm_name, "list"])
    vm_snapshots = vm_snapshots.decode()
    vm_snapshots = vm_snapshots.replace("\r", "")
    vm_snapshots = vm_snapshots.split("\n")
# clean up output
    for i in vm_snapshots:
        if snapshot_name in i:
            start = (int(i.find("("))) + 1
            stop = int(i.find(")"))
            snapshot_uuid = i[start: stop]
            snapshot_uuid = snapshot_uuid.split()
            snapshot_uuid = {snapshot_uuid[0].strip(":") : snapshot_uuid[1]}
    return snapshot_uuid


def run_script(name):
    os.system("python " + name + ".py")


def egg_chk(string):
    string = string.lower()
    string = string.strip(",")
    string = string.strip(".")
    if "try to take over the world" in string:
        return True
    if "same thing we do every night" in string:
        return True
    if "pinky" in string:
        return True


def egg():
    with open("lyrics.txt") as lyrics:
        lyrics = lyrics.readlines()
        for i in lyrics:
            i = i.strip("\n")
            print(i)

list_vms()
