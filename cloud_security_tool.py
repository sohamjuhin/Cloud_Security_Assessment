import boto3

# Function to check security configurations of AWS resources
def check_security_configurations():
    # Initialize AWS clients
    ec2_client = boto3.client('ec2')
    rds_client = boto3.client('rds')

    # Check EC2 security groups
    print("=== EC2 Security Groups ===")
    response = ec2_client.describe_security_groups()
    for group in response['SecurityGroups']:
        print("Security Group ID:", group['GroupId'])
        print("Group Name:", group['GroupName'])
        print("VPC ID:", group['VpcId'])
        print("Ingress Rules:", group['IpPermissions'])
        print("Egress Rules:", group['IpPermissionsEgress'])
        print("---")

    # Check RDS instances
    print("=== RDS Instances ===")
    response = rds_client.describe_db_instances()
    for instance in response['DBInstances']:
        print("DB Instance Identifier:", instance['DBInstanceIdentifier'])
        print("DB Instance Endpoint:", instance['Endpoint'])
        print("DB Security Groups:", instance['DBSecurityGroups'])
        print("---")

# Usage example
check_security_configurations()
