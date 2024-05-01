
# from flask import Flask, render_template, request, redirect, url_for
# import boto3

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/set_credentials', methods=['POST'])
# def set_credentials():
#     # Get AWS credentials and region from submitted form
#     aws_access_key_id = request.form['access_key']
#     aws_secret_access_key = request.form['secret_key']
#     region_name = request.form['region']

#     # Redirect to services page with credentials and region as query string parameters
#     return redirect(url_for('list_services', access_key=aws_access_key_id,
#                             secret_key=aws_secret_access_key, region=region_name))

# @app.route('/services')
# def list_services():
#     # Get AWS credentials, region, and selected service from query string
#     aws_access_key_id = request.args.get('access_key')
#     aws_secret_access_key = request.args.get('secret_key')
#     region_name = request.args.get('region')
#     selected_service = request.args.get('service')

#     # Initialize resources as an empty list
#     resources = []

#     # Initialize Boto3 client for the selected service with the provided credentials and region
#     if selected_service == 's3':
#         client = boto3.client('s3', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         resources = [bucket['Name'] for bucket in client.list_buckets()['Buckets']]
#     elif selected_service == 'iot_topic_rules':
#         client = boto3.client('iot', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         paginator = client.get_paginator('list_topic_rules')
#         response_iterator = paginator.paginate()
#         for response in response_iterator:
#             resources.extend(rule['ruleName'] for rule in response['rules'])
#     elif selected_service == 'dynamodb':
#         client = boto3.resource('dynamodb', aws_access_key_id=aws_access_key_id,
#                                 aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         resources = [table.name for table in client.tables.all()]
#     elif selected_service == 'ec2':
#         client = boto3.client('ec2', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         resources = [instance['InstanceId'] for reservation in client.describe_instances()['Reservations']
#                      for instance in reservation['Instances']]
#     elif selected_service == 'iot_policies':
#         client = boto3.client('iot', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         try:
#             response = client.list_policies()
#             resources = [policy['policyName'] for policy in response.get('policies', [])]
#         except ClientError as e:
#             error_message = f"Error listing IoT policies: {e}"
#             print(error_message)

#     # Render the services.html template with the list of resources and other parameters
#     return render_template('services.html', resources=resources,
#                            selected_service=selected_service,
#                            access_key=aws_access_key_id,
#                            secret_key=aws_secret_access_key,
#                            region=region_name)

# @app.route('/delete_resource', methods=['POST'])
# def delete_resource():
#     # Get AWS credentials, region, selected service, resource name, and action from form data
#     aws_access_key_id = request.form['access_key']
#     aws_secret_access_key = request.form['secret_key']
#     region_name = request.form['region']
#     selected_service = request.form['selected_service']
#     resource_name = request.form['resource_name']
#     action = request.form['action']

#     # Initialize Boto3 client for the selected service with the provided credentials and region
#     client = None
#     if selected_service == 's3':
#         client = boto3.client('s3', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         if action == 'empty':
#             # Empty the bucket first
#             bucket = boto3.resource('s3').Bucket(resource_name)
#             bucket.objects.all().delete()
#         elif action == 'delete':
#             # Delete the bucket
#             client.delete_bucket(Bucket=resource_name)
#     elif selected_service == 'iot_topic_rules':
#         client = boto3.client('iot', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         client.delete_topic_rule(ruleName=resource_name)
#     elif selected_service == 'dynamodb':
#         client = boto3.client('dynamodb', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         client.delete_table(TableName=resource_name)
#     elif selected_service == 'ec2':
#         # You can't directly delete an EC2 instance using Boto3; you may want to stop or terminate the instance instead.
#         pass
#     elif selected_service == 'iot_policies':
#         client = boto3.client('iot', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         client.delete_policy(policyName=resource_name)

#     # Redirect back to the list_services route to refresh the list of resources
#     return redirect(url_for('list_services', access_key=aws_access_key_id,
#                             secret_key=aws_secret_access_key, region=region_name,
#                             service=selected_service))

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for
# import boto3

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/set_credentials', methods=['POST'])
# def set_credentials():
#     # Get AWS credentials and region from submitted form
#     aws_access_key_id = request.form['access_key']
#     aws_secret_access_key = request.form['secret_key']
#     region_name = request.form['region']

#     # Redirect to services page with credentials and region as query string parameters
#     return redirect(url_for('list_services', access_key=aws_access_key_id,
#                             secret_key=aws_secret_access_key, region=region_name))

# @app.route('/services')
# def list_services():
#     # Get AWS credentials, region, and selected service from query string
#     aws_access_key_id = request.args.get('access_key')
#     aws_secret_access_key = request.args.get('secret_key')
#     region_name = request.args.get('region')
#     selected_service = request.args.get('service')

#     # Initialize resources as an empty list
#     resources = []

#     # Initialize Boto3 client for the selected service with the provided credentials and region
#     if selected_service == 'iot_topic_rules':
#         client = boto3.client('iot', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         paginator = client.get_paginator('list_topic_rules')
#         response_iterator = paginator.paginate()
#         for response in response_iterator:
#             resources.extend(rule['ruleName'] for rule in response['rules'])
#     elif selected_service == 'dynamodb':
#         client = boto3.resource('dynamodb', aws_access_key_id=aws_access_key_id,
#                                 aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         resources = [table.name for table in client.tables.all()]
#     elif selected_service == 'iot_policies':
#         client = boto3.client('iot', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         try:
#             response = client.list_policies()
#             resources = [policy['policyName'] for policy in response.get('policies', [])]
#         except ClientError as e:
#             error_message = f"Error listing IoT policies: {e}"
#             print(error_message)

#     # Render the services.html template with the list of resources and other parameters
#     return render_template('services.html', resources=resources,
#                            selected_service=selected_service,
#                            access_key=aws_access_key_id,
#                            secret_key=aws_secret_access_key,
#                            region=region_name)

# @app.route('/delete_resource', methods=['POST'])
# def delete_resource():
#     # Get AWS credentials, region, selected service, resource name, and action from form data
#     aws_access_key_id = request.form['access_key']
#     aws_secret_access_key = request.form['secret_key']
#     region_name = request.form['region']
#     selected_service = request.form['selected_service']
#     resource_name = request.form['resource_name']
#     action = request.form['action']

#     # Initialize Boto3 client for the selected service with the provided credentials and region
#     client = None
#     if selected_service == 'iot_topic_rules':
#         client = boto3.client('iot', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         client.delete_topic_rule(ruleName=resource_name)
#     elif selected_service == 'dynamodb':
#         client = boto3.client('dynamodb', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         client.delete_table(TableName=resource_name)
#     elif selected_service == 'iot_policies':
#         client = boto3.client('iot', aws_access_key_id=aws_access_key_id,
#                               aws_secret_access_key=aws_secret_access_key, region_name=region_name)
#         client.delete_policy(policyName=resource_name)

#     # Redirect back to the list_services route to refresh the list of resources
#     return redirect(url_for('list_services', access_key=aws_access_key_id,
#                             secret_key=aws_secret_access_key, region=region_name,
#                             service=selected_service))

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import boto3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_credentials', methods=['POST'])
def set_credentials():
    # Get AWS credentials and region from submitted form
    aws_access_key_id = request.form['access_key']
    aws_secret_access_key = request.form['secret_key']
    region_name = request.form['region']

    # Redirect to services page with credentials and region as query string parameters
    return redirect(url_for('list_services', access_key=aws_access_key_id,
                            secret_key=aws_secret_access_key, region=region_name))

@app.route('/services')
def list_services():
    # Get AWS credentials, region, and selected service from query string
    aws_access_key_id = request.args.get('access_key')
    aws_secret_access_key = request.args.get('secret_key')
    region_name = request.args.get('region')
    selected_service = request.args.get('service')

    # Initialize resources as an empty list
    resources = []

    # Initialize Boto3 client for the selected service with the provided credentials and region
    if selected_service == 'iot_topic_rules':
        client = boto3.client('iot', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        paginator = client.get_paginator('list_topic_rules')
        response_iterator = paginator.paginate()
        for response in response_iterator:
            resources.extend(rule['ruleName'] for rule in response['rules'])
    elif selected_service == 'dynamodb':
        client = boto3.resource('dynamodb', aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        resources = [table.name for table in client.tables.all()]
    elif selected_service == 'iot_policies':
        client = boto3.client('iot', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        try:
            response = client.list_policies()
            resources = [policy['policyName'] for policy in response.get('policies', [])]
        except ClientError as e:
            error_message = f"Error listing IoT policies: {e}"
            print(error_message)

    # Render the services.html template with the list of resources and other parameters
    return render_template('services.html', resources=resources,
                           selected_service=selected_service,
                           access_key=aws_access_key_id,
                           secret_key=aws_secret_access_key,
                           region=region_name)

@app.route('/delete_resource', methods=['POST'])
def delete_resource():
    # Get AWS credentials, region, selected service, resource name, and action from form data
    aws_access_key_id = request.form['access_key']
    aws_secret_access_key = request.form['secret_key']
    region_name = request.form['region']
    selected_service = request.form['selected_service']
    resource_name = request.form['resource_name']
    action = request.form['action']

    # Initialize Boto3 client for the selected service with the provided credentials and region
    client = None
    if selected_service == 'iot_topic_rules':
        client = boto3.client('iot', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        client.delete_topic_rule(ruleName=resource_name)
    elif selected_service == 'dynamodb':
        client = boto3.client('dynamodb', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        client.delete_table(TableName=resource_name)
    elif selected_service == 'iot_policies':
        client = boto3.client('iot', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        client.delete_policy(policyName=resource_name)

    # Redirect back to the list_services route to refresh the list of resources
    return redirect(url_for('list_services', access_key=aws_access_key_id,
                            secret_key=aws_secret_access_key, region=region_name,
                            service=selected_service))

if __name__ == '__main__':
    app.run(debug=True)

