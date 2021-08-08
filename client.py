import logging

import grpc
import sys
sys.path.insert(0, './proto')
from proto import temperature_pb2_grpc, temperature_pb2


def send_temperature_entry(stub, temperatureMeasurement):
    temperature_entry = stub.TemperatureMeasurementStats(temperatureMeasurement)
    print("[recording = %s, persisted = %s]" % (temperature_entry.recording, temperature_entry.persisted))



def get_temperature_entry(stub):
    send_temperature_entry(stub, temperature_pb2.TemperatureMeasurement(temperatureRecording=99))

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = temperature_pb2_grpc.TemperatureRecordingStub(channel)
        get_temperature_entry(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()