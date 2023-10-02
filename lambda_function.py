import boto3
import base64
import json

sagemaker_runtime = boto3.client('sagemaker-runtime')
ENDPOINT_NAME = "sagemakerのエンドポイント"


def lambda_hundler(event, context):
    # ログ出力
    print("Received event:", event)

    # 画像のデコード
    body_data = json.loads(event["body"])
    image_data = body_data["image"]
    new_image_data = base64.b64decode(image_data)

    # エンドポイントの呼び出し
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        Body=new_image_data,
        ContentType='application/x-image'
    )

    result = response['Body'].read().decode('utf-8')
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }
