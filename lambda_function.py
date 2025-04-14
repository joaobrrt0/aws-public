import json
import boto3
from botocore.exceptions import ClientError

#iniciando o cliente do DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')  # Tabela do DynamoDB

def lambda_handler(event, context):
    method = event['httpMethod']
    
    if method == 'POST':
        return create_user(event)
    elif method == 'GET':
        return get_user(event)
    elif method == 'PUT':
        return update_user(event)
    elif method == 'DELETE':
        return delete_user(event)
    else:
        return {
            'statusCode': 405,
            'body': json.dumps('Method Not Allowed')
        }

#função para criar um novo usuário
def create_user(event):
    try:
        body = json.loads(event['body'])
        user_id = body['user_id']
        name = body['name']
        email = body['email']
        
        #inserindo no DynamoDB
        table.put_item(
            Item={
                'user_id': user_id,
                'name': name,
                'email': email
            }
        )
        
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'User created successfully'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f"Error: {e.response['Error']['Message']}"})
        }

#função para obter um usuário
def get_user(event):
    try:
        user_id = event['pathParameters']['id']
        response = table.get_item(Key={'user_id': user_id})
        
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'User not found'})
            }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f"Error: {e.response['Error']['Message']}"})
        }

#função para atualizar um usuário
def update_user(event):
    try:
        body = json.loads(event['body'])
        user_id = event['pathParameters']['id']
        name = body.get('name')
        email = body.get('email')
        
        #atualizando no DynamoDB
        update_expression = 'set '
        expression_values = {}
        
        if name:
            update_expression += 'name = :name, '
            expression_values[':name'] = name
        if email:
            update_expression += 'email = :email, '
            expression_values[':email'] = email
        
        update_expression = update_expression.rstrip(', ')
        
        table.update_item(
            Key={'user_id': user_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'User updated successfully'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f"Error: {e.response['Error']['Message']}"})
        }

#função para deletar um usuário
def delete_user(event):
    try:
        user_id = event['pathParameters']['id']
        
        #deletando do DynamoDB
        table.delete_item(Key={'user_id': user_id})
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'User deleted successfully'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f"Error: {e.response['Error']['Message']}"})
        }
