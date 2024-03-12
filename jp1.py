import sys
import oci
import argparse
from terminaltables import AsciiTable
all_instance_metadata = [];
parser = argparse.ArgumentParser(
    prog = "python3 blogpost.py",
    description = "List name, OCID, lifecycle state and public IP for every compute VM in a compartment"
)
parser = argparse.ArgumentParser(
    prog = "python3 blogpost.py",
    description = "List name, OCID, lifecycle state and public IP for every compute VM in a compartment"
)
 
parser.add_argument(
    "compartment_ocid",
    help="the compartment OCID to be scanned"
)
 
args = parser.parse_args()
compartment_ocid = args.compartment_ocid
 
config = oci.config.from_file()
oci.config.validate_config(config)
 
compute_client = oci.core.ComputeClient(config)
try:
    vm_instances = compute_client.list_instances(
        compartment_id = compartment_ocid
   ).data
except oci.exceptions.ServiceError as s:
    print(f"ERR: failed to obtain a list of compute VM instances due to '{s.message}'")
    sys.exit(1)
 
if len(vm_instances) == 0:
    print (f"ERR: no compute VMs found in compartment {compartment_ocid}")
    sys.exit(2)
 
 
# network client
virtual_network_client = oci.core.VirtualNetworkClient(config)
 
for vm in vm_instances:
 
    # this dict stores the relevant instance details
    instance_info = {
        "display_name": vm.display_name,
        "id": vm.id,
        "lifecycle_state": vm.lifecycle_state,
        "public_ips": [ ]
    }
# skip terminated instances
    if vm.lifecycle_state == "TERMINATED":
        continue
 
    # get the VM's vNIC attachements. You could add a check for an error in this
    # call but this isn't done for the sake of readability.
    vnic_attachments = compute_client.list_vnic_attachments(
        compartment_id=vm.compartment_id,                                                                                                                                                                           
        instance_id=vm.id
    ).data
 
    all_instance_metadata.append(instance_info)
table_data = [
    [ "Display Name", "Lifecycle Status", "Public IPs", "Oracle Cloud ID"]
]
 
 
for row in all_instance_metadata:
    table_data.append(
        [row["display_name"],row["lifecycle_state"], row["public_ips"], row["id" ]]
    )
 
# step 5: print the table
print(AsciiTable(table_data).table)