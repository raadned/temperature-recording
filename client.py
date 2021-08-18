import logging

import grpc
import sys

sys.path.insert(0, './proto')
from proto import temperature_pb2_grpc, temperature_pb2


def send_temperature_entry(stub, temperatureMeasurement):
    temperature_entry = stub.TemperatureMeasurementRecord(temperatureMeasurement)
    print("[recording = %s, persisted = %s]" % (temperature_entry.recording, temperature_entry.persisted))

def get_temperature_stats(stub):
    temperature_entries = generate_temperatures()
    tmp_stats = stub.TemperatureMeasurementAvg(temperature_entries)
    print(tmp_stats)

def generate_temperatures():
    temperature_entries = []
    for tmp in range(0, 36):
        temperature_entries.append(temperature_pb2.TemperatureMeasurement(temperatureRecording=tmp))
    return iter(temperature_entries)

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = temperature_pb2_grpc.TemperatureRecordingStub(channel)
        print("Send temperature entries")
        send_temperature_entry(stub, temperature_pb2.TemperatureMeasurement(temperatureRecording=99))
        send_temperature_entry(stub, temperature_pb2.TemperatureMeasurement(temperatureRecording=101))
        print("Get temperature stats")
        get_temperature_stats(stub)



if __name__ == '__main__':
    logging.basicConfig()
    run()
