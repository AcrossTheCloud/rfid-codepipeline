#!/usr/bin/env
import boto3
import json
client = boto3.client('codepipeline')

def main(event, context):
    if event['user'] == 'matthew':
        client.start_pipeline_execution(name='msf-reach-dev')
