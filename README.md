# RFID triggered AWS Code Pipeline using esp32 + AWS IoT + lambda

# Security note
Although the data from the esp32 to AWS IoT endpoint is secured, and you can keep the IAM policies tight, there is only a simple checking of RFID contents (so it's easy for your card to be cloned) and only a simple check in the lambda function too for the message (so if someone else can publish to that topic then there's no real security around that); at this stage this is more just a simple proof of concept than anything else.

# Video
A demo is available on [YouTube](https://www.youtube.com/watch?v=Z-1sqJSZoOw).

# Required hardware
* RC522 RFID reader
* esp32 board

# Required software
* [Arduino IDE for desktop](https://www.arduino.cc/)
* @miguelbalboa's [Arduino RFID library](https://github.com/miguelbalboa/rfid), this one should be available in from the list of libraries in the Arduino library manager already, if not just download the zip copy of the source from GitHub and import.
* [This Arduino esp32 AWS IoT library](https://github.com/ExploreEmbedded/Hornbill-Examples/tree/master/arduino-esp32/AWS_IOT)

# Hardware setup
## RFID card setup
See [this code](https://github.com/miguelbalboa/rfid/blob/master/examples/ReadAndWrite/ReadAndWrite.ino) for some examples of reading and writing to RFID. [This line](https://github.com/miguelbalboa/rfid/blob/c8b922c8a4c26baf1b66924e925401f6c265dfd4/examples/ReadAndWrite/ReadAndWrite.ino#L95) can be used to specify the data blocks to write, which then must match the corresponding `dataBlock[]` in this code.

## Pin connections

| esp32        | rfid         |
| ------------- |-------------|
| 3(.3)V | VCC |
| GND | GND |
| SCK | SCK |
| MISO | MISO |
| MOSI | MOSI |
| 14 | RST |
| 15 | (N)SS |
| no connection | IRQ |

# Software setup
Set up a thing in AWS IoT, download its certificates (use the 1 click process) and attach a policy to its certificate allowing `iot:connect` to client `rfid-thing` and `iot:*` for topic `topic/rfid`.

Clone the above-mentioned IoT library and copy the certificates into the aws_iot_certficates.c file under the arduino-esp32/AWS_IOT/src directory. The [convert_cert.py](convert_cert.py) python3 script can help you get the formatting correct. Zip the contents of the AWS_IOT directory (i.e. cd into that directory first so you don't have that directory as part of the path in the zip file) and then import that as a zip library into the Arduino IDE.

Set up a lambda function triggered from the RFID topic (SQL: `SELECT * from 'topic/rfid'`) and to its IAM policy grant permissions to allow action `codepipeline:StartPipelineExecution` for required resources.
