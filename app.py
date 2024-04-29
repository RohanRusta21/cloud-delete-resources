from flask import Flask, render_template, request, redirect, url_for
import boto3

app = Flask(__name__)

# AWS credentials and region
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'YOUR_AWS_REGION'

# Initialize Boto3 clients
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key, region_name=region_name)
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key, region_name=region_name)
# Add more clients for other AWS services as needed


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/services')
def list_services():
    # List available AWS services
    services = ['EC2', 'S3']  # Add more services here

    return render_template('services.html', services=services)


@app.route('/delete', methods=['POST'])
def delete_service():
    service_name = request.form['service']
    service_id = request.form['id']

    if service_name == 'EC2':
        ec2.terminate_instances(InstanceIds=[service_id])
    elif service_name == 'S3':
        s3.delete_bucket(Bucket=service_id)
    # Add more delete operations for other services

    return redirect(url_for('list_services'))


if __name__ == '__main__':
    app.run(debug=True)
