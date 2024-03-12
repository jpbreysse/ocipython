import oci
from oci.object_storage import ObjectStorageClient
from oci.object_storage.models import CreateBucketDetails


# Initialize some variables with your own env 
'''
    OCI_CONFIG: Path to the config file of oci. Normally in '~/.oci/config'
    COMPARMENT_OCID: The comparment_ocid where to create the resources
'''
OCI_CONFIG = '~/.oci/config'
COMPARMENT_OCID = 'jp1.py ocid1.compartment.oc1..aaaaaaaao7hj3a6vn2qmis6g6iifqs2givwb2376mo2cfabtrobj63agrplq'


'''
    OBJECT_STORAGE_NAMESPACE: Use your object storage namespace
    BUCKET_NAME: A bucket name that you want to create
'''
OBJECT_STORAGE_NAMESPACE = 'archive'
BUCKET_NAME='oci-sample-bucket'


# The config object is needed to create all the clients
config = oci.config.from_file(OCI_CONFIG)

# Create the ObjectStorageClient
object_storage_client = ObjectStorageClient(config)
