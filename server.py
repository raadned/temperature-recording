from concurrent import futures
import logging
import grpc
import sys

sys.path.insert(0, './proto')
from proto import temperature_pb2_grpc, temperature_pb2


class TemperatureServicer(temperature_pb2_grpc.TemperatureRecordingServicer):

    def TemperatureMeasurementRecord(self, recording, context):
        print('Received %s' % recording)
        return temperature_pb2.TemperatureEntry(recording=recording.temperatureRecording, persisted=True)

    def TemperatureMeasurementAvg(self, recordings_iterator, context):

        min = float('inf')
        max = float('-inf')
        count = 0
        sum = 0

        for recording in recordings_iterator:
            count += 1
            sum += count
            max = recording.temperatureRecording if recording.temperatureRecording > max else max
            min = recording.temperatureRecording if recording.temperatureRecording < min else min

        return temperature_pb2.TemperatureMeasurementStats(numEntries=count, minTmp=min, maxTmp=max, avgTmp=(sum / max))



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    temperature_pb2_grpc.add_TemperatureRecordingServicer_to_server(TemperatureServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
