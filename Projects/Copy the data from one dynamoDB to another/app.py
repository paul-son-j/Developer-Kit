import boto3




class DynamoDBDataCopier:
    def __init__(self, old_table_name, new_table_name):
        self.dynamodb = boto3.resource("dynamodb")
        self.old_table = self.dynamodb.Table(old_table_name)
        self.new_table = self.dynamodb.Table(new_table_name)

    def copy_data(self):
        scan_kwargs = {}
        with self.new_table.batch_writer() as batch:
            while True:
                response = self.old_table.scan(**scan_kwargs)
                for item in response["Items"]:
                    batch.put_item(Item=item)

                if "LastEvaluatedKey" not in response:
                    break

                scan_kwargs["ExclusiveStartKey"] = response["LastEvaluatedKey"]

        print("✅ Data copy complete")


if __name__ == "__main__":
    copier = DynamoDBDataCopier("apim-alla-1811", "devconsole-internal-qa2")
    copier.copy_data()
