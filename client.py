import logging

import grpc
import temperature_pb2
import temperature_pb2_grpc


def send_temperature_entry(stub, temperatureMeasurement):
    temperature_entry = stub.TemperatureMeasurementStats(temperatureMeasurement)
    print("[recording = %s, persisted = %s]" % (temperature_entry.recording, temperature_entry.recording))



def get_temperature_entry(stub):
    send_temperature_entry(stub, temperature_pb2.TemperatureMeasurement(temperatureRecording=100))

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = temperature_pb2_grpc.TemperatureRecordingStub(channel)
        get_temperature_entry(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()