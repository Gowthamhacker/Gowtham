import json

def process_iot_data(event, context):
    #

    try:
        iot_data = json.loads(event['body'])  
        print("Received IoT data: ", iot_data)
        
        
        response = {
            "statusCode": 200,
            "body": json.dumps({"message": "IoT data processed successfully."})
        }
        return response

    except Exception as e:
        # Handle errors or exceptions here.
        print("Error processing IoT data:", str(e))
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error"})
        }
        return response


